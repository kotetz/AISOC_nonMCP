---
name: identity
description: ユーザー/ID軸でサインイン挙動・権限・関連アクティビティを調査する。incident/entity Skillからアカウントが関わる調査を委譲された時、または「このユーザーのサインインを見て」のように直接ユーザーを指定された時に使う。
argument-hint: "[account 値: UPN や AccountObjectId など]"
context: fork
---

# ユーザー/ID軸の調査

対象アカウントについて、以下の観点を確認する。クエリは `aisoc query "<KQL>" --hours <N>` でその都度組み立てる(固定テンプレートは使わない)。テーブルの列がわからない場合は `schema` Skillの内容を参照する。調査期間の既定・拡大条件は [copilot-instructions.md](../../copilot-instructions.md) の共通ガードレールに従う。

## 着眼点

1. **サインインの逸脱**: 通常と異なる地理/デバイス/アプリ/IPからのサインインがないか(`SigninLogs`, `AADNonInteractiveUserSignInLogs`)
2. **認証の失敗・弱さ**: レガシー認証、MFA失敗、パスワードスプレーの兆候
3. **権限**: 特権ロールの保有・最近の変更(`AuditLogs`)
4. **リスク判定**: Identity Protectionのリスクレベル(`AADUserRiskEvents`, `AADRiskyUsers`)
5. **振る舞い分析**: 普段と異なる行動パターン(`BehaviorAnalytics`, `UserPeerAnalytics`)
6. **横展開**: 同一アカウントが関わる他のアラート/インシデント(`SecurityAlert`)

## 手順

1. 上記テーブルから関連しそうなものを選び、対象期間でKQLを組み立てて実行する(既定・拡大条件は共通ガードレールに従う)。
2. 得られた所見を「通常時との比較」で評価する(可能なら過去7〜30日のベースラインと比較するクエリも組み立てる)。
3. 呼び出し元(`incident`/`entity` Skill、または直接の対話)に、以下を返す:
   - 確認した観点ごとの結果(異常あり/なし)
   - 総合的な疑わしさの評価
   - 追加で確認すべき点があれば明記

## 注意事項

- 書き込み系操作(パスワードリセット・アカウント無効化等)は一切行わない。提案に留める。
- データが存在しない場合は「データなし」と正直に報告する。
