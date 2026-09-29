---
name: email
description: メール配信・フィッシング・受信箱ルール改ざんの兆候を調査する。incident/entity Skillからメール/送信者/URL/添付ファイルが関わる調査を委譲された時、または「このメール/送信者怪しいので見て」のように直接指定された時に使う。
argument-hint: "[email 値: NetworkMessageId, 送信者アドレス, 受信者UPN など]"
context: fork
---

# メール/フィッシング軸の調査

対象メール(送信者/受信者/NetworkMessageId/URL/添付ファイル)について、以下の観点を確認する。使用するテーブルが決まったら、`../schema/references/<TableName>.md` の共通スキーマを直接読む。複数テーブルを使う場合は必要なファイルだけを並列に読み、Currentのリファレンスがあるテーブルへ通常調査で`getschema`を実行しない。環境不一致・ファイル欠落・列エラー時は `schema` Skillの初期化・更新手順に従う。

## 着眼点

1. **配信結果と脅威判定**: `EmailEvents`の`ThreatTypes`/`DeliveryAction`/`ConfidenceLevel`/`BulkComplaintLevel`
2. **URL/添付ファイルの危険性**: `EmailUrlInfo`のURLチェーン(`UrlChainId`/`UrlChainPosition`)、`EmailAttachmentInfo`の`ThreatTypes`/`SHA256`
3. **受信者の反応**: `UrlClickEvents`で実際にリンクをクリックしたか(`IsClickedThrough`)、クリック時のIP/アプリ
4. **配信後アクション**: ZAP等による事後隔離・削除(`EmailPostDeliveryEvents`)
5. **受信箱ルール/転送設定の改ざん**: `OfficeActivity`の`Operation`(`New-InboxRule`, `Set-InboxRule`, `Set-Mailbox`等)や`EmailEvents`の`ForwardingInformation`
6. **横展開**: 同一送信者/URL/添付ファイルハッシュが関わる他のアラート/インシデント(`SecurityAlert`)

## 手順

1. 上記テーブルから関連しそうなものを選び、対象期間でKQLを組み立てて実行する。`NetworkMessageId`を軸に`EmailEvents`/`EmailUrlInfo`/`EmailAttachmentInfo`/`EmailPostDeliveryEvents`/`UrlClickEvents`を突合すると、1通のメールを時系列で追いやすい。
2. `ThreatTypes`/`DetectionMethods`が空であることを安易に「安全」と解釈しない(Defender for Office 365側の判定なし/未検知の可能性がある)。受信箱ルール変更は在宅勤務や自動応答設定など正当な理由でも発生するため、単独では断定せず、他の観点と突合する。
3. 呼び出し元(`incident`/`entity` Skill、または直接の対話)に、以下を返す:
   - 確認した観点ごとの結果(異常あり/なし)
   - 総合的な疑わしさの評価
   - 追加で確認すべき点があれば明記

## 注意事項

- `OfficeActivity`は列数が多く汎用的なテーブルのため、`Operation`/`OfficeWorkload`で絞り込んでから調査する。
