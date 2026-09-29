---
name: triage
description: 現在オープンな(New/Active)Sentinelインシデントを一覧化し、対応優先度を提示する。また、具体的な値を指定せず「怪しいユーザーを探して」「怪しいデバイスを探して」「不審な連携アプリがないか見て」「フィッシングの兆候を探して」「何か異常はないか見て」のように横断探索を依頼された時に使う。
argument-hint: "[severity フィルタ、任意（例: High,Medium）]"
context: fork
---

# キュー優先順位付け

## 手順

依頼内容に応じて、以下のいずれかを開始する。

### インシデントキューのトリアージ

1. 現在オープンなインシデントを取得する(severityランクとアラート数はKQL側で計算してソート):

   ```powershell
   Invoke-AzOperationalInsightsQuery -WorkspaceId $env:AISOC_WORKSPACE_ID -Timespan (New-TimeSpan -Days 30) -Query "SecurityIncident | summarize arg_max(TimeGenerated, *) by IncidentNumber | where Status in ('New', 'Active') | where Severity in ('High', 'Medium') | extend SeverityRank = case(Severity == 'High', 3, Severity == 'Medium', 2, Severity == 'Low', 1, 0), AlertCount = array_length(AlertIds) | order by SeverityRank desc, AlertCount desc"
   ```

   期間やseverityフィルタはメッセージの指示に応じて調整する。指定がなければ既定値(過去30日、全severity)を使う。

2. 結果の重大度・関連アラート数・作成からの経過時間をもとに、上位数件(目安5〜10件)を「優先的に見るべきインシデント」として選ぶ。

3. 選んだ上位インシデントのうち、依頼への回答に必要な最上位1件を `incident` Skillへ委譲して深掘りする。残りは一覧と優先順位の提示に留める。

4. 出力形式:
   - 優先順位付きリスト(番号・タイトル・重大度・ステータス・アラート数)
   - 上位インシデントを選んだ理由を一言で添える
   - 深掘りが必要そうなものを提案する

### ユーザー横断ハント

「怪しいユーザーを探して」のように具体的なアカウント値がない場合は、直近7日間を既定として一次データから候補を抽出する。

1. `AADRiskyUsers` / `AADUserRiskEvents` の高リスクまたは侵害確認済みユーザー、`SigninLogs` / `AADNonInteractiveUserSignInLogs` の異常な失敗・地理・IP・認証方式、`BehaviorAnalytics` の高いInvestigationPriority、`SecurityAlert` のAccountエンティティを横断する。列と型は `../schema/references/<TableName>.md` を直接参照し、環境不一致・ファイル欠落・列エラー時だけ `schema` Skillの初期化・更新手順に従う。
2. リスク状態、重大度、検知数、直近性を根拠に候補を順位付けする。単一のシグナルだけで侵害と断定しない。
3. 上位候補(目安3件、候補が少なければ全件)を `identity` Skillへ委譲し、通常時との比較と関連アラートを深掘りする。
4. `Reports/` 直下に `hunt-users` を含むファイル名で、候補ランキング、根拠、Identity所見、結論、推奨対応、実行した全KQLを含むHTMLレポートを作成する。

### デバイス横断ハント

「怪しいデバイスを探して」のように具体的なデバイス値がない場合は、直近7日間を既定として一次データから候補を抽出する。

1. `SecurityAlert` の `Entities`(dynamic、`mv-expand`してhost/deviceタイプを抽出。値が取れる主手法とする)によるデバイス単位のアラート件数・重大度・関連手法、`BehaviorAnalytics` の `Device`/`SourceDevice`/`DestinationDevice` 列に基づく高い `InvestigationPriority`、`DeviceProcessEvents`/`DeviceCustomProcessEvents` の難読化・資格情報窃取コマンドライン(`-enc`, `FromBase64String`, `mimikatz`, `rubeus`, `sekurlsa`, `dcsync` 等)、`DeviceNetworkEvents` の外部公開IP・非標準ポートへの通信、`DeviceInfo` の `ExposureLevel`/`SensorHealthState` を横断する。`CompromisedEntity` は `Entities` が空/抽出困難な場合の補助的な代替に留める(空の場合を安易に一括りにまとめると、本来特定できるはずのデバイスが埋もれる)。列と型は `../schema/references/<TableName>.md` を直接参照し、環境不一致・ファイル欠落・列エラー時だけ `schema` Skillの初期化・更新手順に従う。
2. `device` Skillの注意事項どおり、難読化コマンドや `rundll32.exe` 件数など単一シグナルだけで疑わしいと判定しない。既知の正常運用コマンドを除外し、アラート件数・重大度、UEBA優先度、外部通信、露出レベルなど複数シグナルの重なりを根拠に候補を順位付けする。
3. 上位候補(目安2〜3件、候補が少なければ全件)を `device` Skillへ委譲し、プロセス・永続化・ネットワーク・ログオン・保護状態を深掘りする。同一侵害者が複数デバイス/アカウントを横断している兆候(同一C2宛先、同一ツールのハッシュ、Pass-the-Hashによる他端末への横展開等)が見つかった場合は、関連デバイスも追加で `device` Skillへ回す。
4. `Device*`系の生テレメトリが0件でも、`SecurityAlert`/`AlertEvidence`側にのみ痕跡が残っている場合がある(コネクタ/保持設定起因の可能性)。生テレメトリが空であることを「活動なし」と即断せず、限界として明記する。
5. `Reports/` 直下に `hunt-devices` を含むファイル名で、候補ランキング、根拠、Device所見、攻撃チェーン(該当する場合)、結論、推奨対応、実行した全KQLを含むHTMLレポートを作成する。

### OAuthアプリ/クラウドアプリ横断ハント

「不審な連携アプリがないか見て」のように具体的なアプリ値がない場合は、直近7日間を既定として一次データから候補を抽出する。

1. `OAuthConsentSignals_KQL_CL` の同意直後サインイン(`DeltaMinutes`が極端に短い)、`AuditLogs` の高リスクスコープへの同意操作、`CloudAppEvents` の `IsAnonymousProxy`/`IsAdminOperation`/`UncommonForUser`、`AADServicePrincipalSignInLogs`/`MicrosoftServicePrincipalSignInLogs` の異常なサインイン失敗・地理を横断する。列と型は `../schema/references/<TableName>.md` を直接参照し、環境不一致・ファイル欠落・列エラー時だけ `schema` Skillの初期化・更新手順に従う。
2. `app` Skillの注意事項どおり、マルチテナントアプリや匿名プロキシ経由というだけで悪性と断定しない(正規のSaaS連携でも該当し得る)。同意グラントの異常性、サインイン挙動、クラウドアプリ活動の逸脱が複数重なることを根拠に候補を順位付けする。
3. 上位候補(目安3件、候補が少なければ全件)を `app` Skillへ委譲し、深掘りする。
4. `Reports/` 直下に `hunt-apps` を含むファイル名で、候補ランキング、根拠、App所見、結論、推奨対応、実行した全KQLを含むHTMLレポートを作成する。

### メール/フィッシング横断ハント

「フィッシングの兆候を探して」のように具体的な送信者/メール値がない場合は、直近7日間を既定として一次データから候補を抽出する。

1. `EmailEvents` の `ThreatTypes`/`DeliveryAction`/`ConfidenceLevel`、`EmailAttachmentInfo`/`EmailUrlInfo` の脅威判定、`UrlClickEvents` の `IsClickedThrough`(実際にクリックされたか)、`EmailPostDeliveryEvents` の事後隔離、`OfficeActivity` の `New-InboxRule`/`Set-InboxRule`/`Set-Mailbox` 等の受信箱ルール・転送改ざんを横断する。列と型は `../schema/references/<TableName>.md` を直接参照し、環境不一致・ファイル欠落・列エラー時だけ `schema` Skillの初期化・更新手順に従う。
2. `email` Skillの注意事項どおり、`ThreatTypes`が空であることを安易に「安全」と解釈しない。受信箱ルール変更は正当な理由でも発生するため、脅威判定・実クリック・受信箱ルール改ざんなど複数シグナルの重なりを根拠に候補を順位付けする。
3. 上位候補(目安3件、候補が少なければ全件)を `email` Skillへ委譲し、深掘りする。
4. `Reports/` 直下に `hunt-emails` を含むファイル名で、候補ランキング、根拠、Email所見、結論、推奨対応、実行した全KQLを含むHTMLレポートを作成する。

## 注意事項

- 大量のインシデントがヒットする場合、全件を深掘りしようとせず、まず一覧と優先順位の提示に留める。
- テストデータらしきタイトル(例: "testing", "test_" など)が混じることがある。明らかにテスト/デモ由来と思われるものはその旨を注記しつつ、断定はユーザー確認に委ねる。
