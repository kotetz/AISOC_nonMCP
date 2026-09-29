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
   aisoc incident get <number>
   aisoc incident alerts <number>
   aisoc incident entities <number>
   ```

   タイトル・重大度・ステータス・関連アラート数・エンティティの内訳(Account/Host/IP/URL/FileHash等)を把握する。

2. **専門Skillへの自動委譲**(深掘りパート。該当するものだけ呼ぶ)

   - エンティティに Account が含まれる → `identity` Skillを呼ぶ(対象アカウントを渡す)
   - エンティティに Host が含まれる → `device` Skillを呼ぶ(対象ホストを渡す)
   - エンティティに IP / URL / FileHash が含まれる → `ti` Skillを呼ぶ(対象IOCを渡す)
   - 複数種別が含まれる場合は該当するSkillをすべて呼び、戻ってきた所見を集約する

3. **横展開の確認**

   専門Skillの所見から得られたエンティティ値を使い、同じエンティティが他のインシデントにも登場していないか `aisoc query` でその場でKQLを組み立てて確認する。例:

   ```
   SecurityAlert | where Entities has "<value>" | project TimeGenerated, AlertName, AlertSeverity, SystemAlertId | order by TimeGenerated desc
   ```

4. **記録**

   [copilot-instructions.md](../../copilot-instructions.md) の「レポート出力」仕様に従い、`cases/<number>/` 配下にHTMLレポートを作成する。最低限、次を含める:
   - インシデント概要(タイトル/重大度/ステータス/作成日時)
   - 各専門Skillの所見サマリ
   - 判定: True Positive / False Positive / Benign Positive / 調査継続
   - 推奨対応

## 注意事項

- 書き込み系操作(コメント追加・ステータス変更・クローズ等)は一切行わない。
- クエリ結果が空の場合は「データなし」と正直に報告し、憶測で断定しない。
- テーブルの列がわからない場合は `schema` Skillの内容を参照する。
- すべての `aisoc` コマンドはリポジトリルートで `pip install -e .` 済みであることを前提とする。
