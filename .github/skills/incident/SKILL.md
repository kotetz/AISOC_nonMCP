---
name: incident
description: 指定したMicrosoft Sentinelのインシデント番号を深掘り調査し、True Positive/False Positive/Benign Positiveの判定と推奨対応をまとめる。「インシデント#123を調査して」のように具体的なインシデント番号を挙げて調査を依頼された時に使う。
argument-hint: "[incident-number]"
context: fork
---

# インシデント深掘り調査

このSkillが呼ばれたメッセージに含まれるインシデント番号(IncidentNumber)を対象とする。

## 手順

1. **概況把握**(このSkill自身が行う一般的なパート)

   ```powershell
   # インシデント本体
   Invoke-AzOperationalInsightsQuery -WorkspaceId $env:AISOC_WORKSPACE_ID -Timespan (New-TimeSpan -Days 365) -Query "SecurityIncident | where IncidentNumber == <number> | order by TimeGenerated desc | take 1"
   ```

   結果の `AlertIds`(dynamic配列)を使って関連アラートを取得する:

   ```powershell
   # 関連アラート + エンティティ種別ごとの集計(mv-expandでKQL側で展開する)
   Invoke-AzOperationalInsightsQuery -WorkspaceId $env:AISOC_WORKSPACE_ID -Timespan (New-TimeSpan -Days 365) -Query "SecurityAlert | where SystemAlertId in (<AlertIdsをカンマ区切りで>) | project TimeGenerated, AlertName, AlertSeverity, Tactics, ProductName, Entities | order by TimeGenerated desc"
   ```

   エンティティの内訳(Account/Host/IP/URL/FileHash等)は、上記結果の`Entities`列(JSON文字列)を`mv-expand`+`parse_json`でKQL側で展開・集計すると楽:

   ```
   SecurityAlert | where SystemAlertId in (<AlertIds>) | mv-expand e = parse_json(Entities) | summarize Values=make_set(coalesce(tostring(e.Name), tostring(e.HostName), tostring(e.Address), tostring(e.Url), tostring(e.FileName))) by EntityType = tostring(e.Type)
   ```

   タイトル・重大度・ステータス・関連アラート数・エンティティの内訳を把握する。

2. **専門Skillへの自動委譲**(深掘りパート。該当するものだけ呼ぶ)

   - エンティティに Account が含まれる → `identity` Skillを呼ぶ(対象アカウントを渡す)
   - エンティティに Host が含まれる → `device` Skillを呼ぶ(対象ホストを渡す)
   - エンティティに IP / URL / FileHash が含まれる → `ti` Skillを呼ぶ(対象IOCを渡す)
   - 複数種別が含まれる場合は該当するSkillをすべて呼び、戻ってきた所見を集約する

3. **横展開の確認**

   専門Skillの所見から得られたエンティティ値を使い、同じエンティティが他のインシデントにも登場していないか、その場でKQLを組み立てて確認する。例:

   ```powershell
   Invoke-AzOperationalInsightsQuery -WorkspaceId $env:AISOC_WORKSPACE_ID -Timespan (New-TimeSpan -Hours 168) -Query "SecurityAlert | where Entities has '<value>' | project TimeGenerated, AlertName, AlertSeverity, SystemAlertId | order by TimeGenerated desc"
   ```

4. **記録**

   [copilot-instructions.md](../../copilot-instructions.md) の「レポート出力」仕様に従い、`Reports/` 直下にインシデント番号を含むファイル名でHTMLレポートを作成する。最低限、次を含める:
   - インシデント概要(タイトル/重大度/ステータス/作成日時)
   - 各専門Skillの所見サマリ
   - 判定: True Positive / False Positive / Benign Positive / 調査継続
   - 推奨対応

## 注意事項

- テーブルの列がわからない場合は `schema` Skillの内容を参照する。
