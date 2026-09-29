---
name: ti
description: IP/ドメイン/ハッシュ/URLなどのIOC(indicator of compromise)を、既知の脅威インテリジェンスと照合する。incident/entity Skillから対象にIOCが含まれる場合に使われるほか、「このIP/ハッシュ調べて」のように直接IOCを指定された時にも使う。
argument-hint: "[ioc-type] [value]"
context: fork
---

# IOC / 脅威インテリジェンス照合

対象のIOC(IP/ドメイン/URL/ファイルハッシュ)について、以下を確認する。

## 手順

1. Sentinel内の脅威インテリジェンスと突合する。IOCの種別に応じた列でその場でKQLを組み立てて`aisoc query`で実行する:

   ```
   ThreatIntelIndicators
   | where NetworkIP == "<value>" or DomainName == "<value>" or Url has "<value>" or FileHashValue == "<value>"
   ```

2. 一致した場合は、`Description`, `ThreatType`, `ConfidenceScore`, `Active` などの詳細を確認する。

3. Sentinel組み込みのTI相関アラート(`TI Map * Entity to *` のようなタイトルのアラート)がこのIOCに関連して既に発火していないか、`SecurityAlert`を確認する。

4. Sentinel内で一致が見つからない場合、その旨を明記する。このツールは外部の脅威インテリジェンスサービスには接続しないため、必要であれば分析者に外部サービスでの確認を提案する。

## 出力

- 照合結果(既知の悪性IOCか、Sentinel内では未知か)
- 一致した場合の脅威種別・信頼度
- 関連する既存アラートの有無

## 注意事項

- 書き込み系操作(ブロックリストへの追加等)は一切行わない。
- 外部TIサービスへの照会機能は現状このツールにはない点を正直に伝える。
