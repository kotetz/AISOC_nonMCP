---
name: app
description: OAuthアプリ/サービスプリンシパル軸で同意状況・サインイン挙動・権限スコープを調査する。incident/entity Skillからアプリ/サービスプリンシパルが関わる調査を委譲された時、または「このアプリ怪しいので見て」のように直接アプリを指定された時に使う。
argument-hint: "[app 値: AppId, ServicePrincipalId, AppDisplayName など]"
context: fork
---

# OAuthアプリ/クラウドアプリ軸の調査

対象アプリ/サービスプリンシパルについて、以下の観点を確認する。使用するテーブルが決まったら、`../schema/references/<TableName>.md` の共通スキーマを直接読む。複数テーブルを使う場合は必要なファイルだけを並列に読み、Currentのリファレンスがあるテーブルへ通常調査で`getschema`を実行しない。環境不一致・ファイル欠落・列エラー時は `schema` Skillの初期化・更新手順に従う。

## 着眼点

1. **同意グラントの異常**: 新規/異例の同意、サインイン直後の即時同意(`OAuthConsentSignals_KQL_CL`の`DeltaMinutes`が極端に短い)、高リスクなAPI権限スコープへの同意(`AuditLogs`の"Consent to application"系操作)
2. **サインイン挙動**: 失敗率、異常な地理/IP、条件付きアクセスの適用状況(`AADServicePrincipalSignInLogs`, `MicrosoftServicePrincipalSignInLogs`)
3. **クラウドアプリ活動の逸脱**: 匿名プロキシ経由、管理者操作、そのユーザー/テナントにとって普段と異なる操作(`CloudAppEvents`の`IsAnonymousProxy`, `IsAdminOperation`, `UncommonForUser`, `LastSeenForUser`)
4. **アプリの素性**: マルチテナントアプリか(`AppOwnerTenantId`が自テナントと異なる)、パブリッシャー検証の有無
5. **横展開**: 同一アプリ/サービスプリンシパル/AppIdが関わる他のアラート/インシデント(`SecurityAlert`)

## 手順

1. 上記テーブルから関連しそうなものを選び、対象期間でKQLを組み立てて実行する。
2. 同意時刻とサインイン時刻の近接性、他ユーザー/他テナントとの比較で「普段と異なるか」を評価する。単一の特徴(マルチテナント、匿名プロキシ経由等)だけで悪性と断定しない。正規のSaaS連携でも該当し得るため、複数シグナルの重なりで判断する。
3. 呼び出し元(`incident`/`entity` Skill、または直接の対話)に、以下を返す:
   - 確認した観点ごとの結果(異常あり/なし)
   - 総合的な疑わしさの評価
   - 追加で確認すべき点があれば明記

## 注意事項

- `OAuthConsentSignals_KQL_CL`は事前計算された派生テーブルの可能性がある。一次データ(`AuditLogs`, `AADServicePrincipalSignInLogs`)との突合を怠らず、単独で断定に使わない。
