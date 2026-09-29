---
name: entity
description: インシデント化されていない、特定のユーザー/デバイス/IP/URL/ハッシュ等のエンティティを起点にアドホックな調査を行う。「このユーザー怪しいので見て」のように、インシデント番号がない依頼に使う。
argument-hint: "[entity-type] [value]"
context: fork
---

# エンティティ起点のアドホック調査

## 手順

1. メッセージからエンティティの種別(アカウント/デバイス/IP/URL/ハッシュ等)と値を特定する。曖昧な場合はユーザーに確認する。

2. エンティティ種別に応じて対応する専門Skillを呼ぶ:
   - アカウント/ユーザー → `identity` Skill
   - デバイス/ホスト → `device` Skill
   - IP/URL/ドメイン/ハッシュ → `ti` Skill

3. 専門Skillの所見をもとに、このエンティティが関わる既存のアラート/インシデントがないか確認する:

   ```powershell
   aisoc query "SecurityAlert | where Entities has '<value>' | project TimeGenerated, AlertName, AlertSeverity | order by TimeGenerated desc" --hours 168
   ```

   関連するインシデントが見つかった場合は `incident` Skillでの深掘りを提案する。

4. 記録:

   [copilot-instructions.md](../../copilot-instructions.md) の「レポート出力」仕様に従い、`cases/adhoc-<entity-value>/` 配下にHTMLレポートを作成する。所見と結論(様子見/要エスカレーション/インシデント化を推奨、等)を記載する。

## 注意事項

- まだインシデントが存在しないケースなので、断定的な結論よりも「次に何を確認すべきか」を明確にすることを優先する。
- 書き込み系操作(アカウント無効化・デバイス隔離等)は一切行わない。提案に留める。
