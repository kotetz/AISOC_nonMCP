---
name: triage
description: 現在オープンな(New/Active)Sentinelインシデントを一覧化し、対応優先度を提示する。また、具体的な値を指定せず「怪しいユーザーを探して」「何か異常はないか見て」のように横断探索を依頼された時に使う。
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

1. `AADRiskyUsers` / `AADUserRiskEvents` の高リスクまたは侵害確認済みユーザー、`SigninLogs` / `AADNonInteractiveUserSignInLogs` の異常な失敗・地理・IP・認証方式、`BehaviorAnalytics` の高いInvestigationPriority、`SecurityAlert` のAccountエンティティを横断する。利用可能なテーブル・列が不明な場合は `schema` Skillを参照する。
2. リスク状態、重大度、検知数、直近性を根拠に候補を順位付けする。単一のシグナルだけで侵害と断定しない。
3. 上位候補(目安3件、候補が少なければ全件)を `identity` Skillへ委譲し、通常時との比較と関連アラートを深掘りする。
4. `Reports/` 直下に `hunt-users` を含むファイル名で、候補ランキング、根拠、Identity所見、結論、推奨対応、実行した全KQLを含むHTMLレポートを作成する。

## 注意事項

- 大量のインシデントがヒットする場合、全件を深掘りしようとせず、まず一覧と優先順位の提示に留める。
- テストデータらしきタイトル(例: "testing", "test_" など)が混じることがある。明らかにテスト/デモ由来と思われるものはその旨を注記しつつ、断定はユーザー確認に委ねる。
