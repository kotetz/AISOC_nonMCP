# AI SOC ワークスペース — 全体方針

このワークスペースは Microsoft Sentinel のアラート/インシデント調査を行うための環境です。個別の調査手順は `.github/skills/` 配下の各Skill(`incident`, `triage`, `entity`, `identity`, `device`, `ti`, `schema`)に委ねますが、以下の原則は全Skill・全会話に共通して適用します。

## 原則

1. **読み取り専用**: すべてのデータアクセスは `Invoke-AzOperationalInsightsQuery`(Az.OperationalInsightsモジュール)を直接呼び、Azure Monitor Log Analytics Query APIでKQLを実行します。書き込み・削除・インシデントのクローズ・コメント追加等は一切行いません。このAPI自体がデータプレーンの読み取り専用APIであり、書き込み手段が存在しない設計です。ラッパースクリプトは用意していません。
2. **クエリはその都度組み立てる**: KQLクエリを固定ファイルとして持たず、調査の文脈に応じてその都度組み立てます。テーブル/列がわからない場合は `schema` Skill(自動読込)を参照してください。
3. **ガードレールに従う、ただし長期侵害の兆候があれば期間を拡大する**: `-Timespan (New-TimeSpan -Hours <N>)` の既定は7日間(`-Hours 168`)。次のような長期侵害を示唆する兆候が見つかった場合は、ワークスペースの保持期間の上限である90日間(`-Hours 2160`)まで遡り、侵害の開始時期を特定すること: Identity Protectionで`confirmedCompromised`等のリスク状態が付与されている/DCSync・Kerberoasting・資格情報窃取ツール(Mimikatz, SharpKatz, Kekeo, Rubeus等)関連のアラート/説明のつかない特権変更・SID History操作・不審なアカウント作成。90日を超える期間はワークスペースのログ保持期間外でありこのツールでは調査できない(真に長期のdwell time調査が必要な場合は別途Sentinel data lake等との統合を検討する、現状はスコープ外)。
4. **調査記録を残す**: 各インシデント/エンティティの調査結果は下記「レポート出力」の形式に従い、`cases/<識別子>/` 配下に記録します。
5. **推測で断定しない**: クエリ結果が空、またはエラーの場合はその旨を正直に報告し、憶測で「異常なし」と結論付けないでください。
6. **専門Skillを再利用する**: ユーザー/デバイス/IOCの深掘りが必要な場合は、ゼロからKQLを考えるのではなく `identity` / `device` / `ti` Skillに委譲してください。これらは着眼点(何を疑うべきか)を含んでいます。

## レポート出力

調査結果は **単一の自己完結型HTMLファイル** として `cases/<識別子>/` 配下に出力します。すべてのSkill(`incident`, `triage`, `entity`)に共通の仕様です。固定のレンダリングスクリプト/テンプレートエンジンは用意していません。調査ごとに内容も見せ方も変わるため、都度この仕様に沿ってHTMLを直接組み立てます。

- **ファイル名**: `yyyy_mm_dd_<調査の特徴を表す短い説明(英数字・ハイフン区切り)>.html`(例: `2026_09_29_domain-controller-persistence.html`)。日付は調査を実施した日。
- **配色**: 白背景を基本とし、アクセントカラーは青・グレー系の落ち着いた色調でまとめる(例: 見出し `#1565c0` 系、背景アクセント `#37474f`/`#607d8b` 系)。警告色(赤・オレンジ等)は重大度バッジなど本当に注意を引きたい箇所に限定して使う。
- **可視化**: SVGおよびD3.jsを使い、調査内容に応じて意味のある図を最低1つ含める(例: アラート/イベントのタイムライン、関連エンティティの言及回数を示す棒グラフ、攻撃チェーンの図解など)。装飾目的だけの図は不要。
- **D3.jsの読み込み**: リポジトリ直下の [assets/d3.v7.min.js](../assets/d3.v7.min.js) を、レポートの配置場所からの相対パスで `<script src="../../assets/d3.v7.min.js"></script>` のように参照する。CDNには依存しない(オフラインでも閲覧できるようにするため)。
- **構成の目安**: ヘッダー(タイトル・重大度・ステータス・判定バッジ)/ 概要 / タイムラインや関連エンティティなどの可視化 / 専門Skillごとの所見 / 推奨対応(提案のみである旨を明記) / 留意事項・調査の限界 / **調査に使用したKQL一覧**(必須、末尾) / フッター(生成日時)。
- 通常のインシデント調査は `cases/<incident-number>/`、エンティティ起点のアドホック調査は `cases/adhoc-<entity-value>/` に配置する。
- **調査に使用したKQL一覧(必須)**: レポートの末尾に、調査中に実際に実行したKQLクエリをすべて掲載する。各クエリには、目的を示す一言の見出しと、使用した `-Hours` を添える。単に「結果を要約した」だけでなく、他の分析者が同じ調査をなぞって再現できるようにするための監査証跡であり、省略しない。

## 環境

- 対象ワークスペースIDは `.env` の `AISOC_WORKSPACE_ID` で設定します(`.env.example` を参照)。
- 認証は `Connect-AzAccount` 済みのEntra IDアカウントを使用します(`Az.Accounts` / `Az.OperationalInsights`)。テナントを切り替える場合は `Connect-AzAccount -TenantId <tenant-id>` を実行してください。
- クエリの基本形:
  ```powershell
  Invoke-AzOperationalInsightsQuery -WorkspaceId $env:AISOC_WORKSPACE_ID -Query "<KQL>" -Timespan (New-TimeSpan -Hours <N>)
  ```
- セットアップ手順は [README.md](../README.md) を参照してください。
