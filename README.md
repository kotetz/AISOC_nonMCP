# AI SOC — Sentinel Investigation Workspace

Microsoft Sentinel MCP を使わず、Log Analytics Query API を直接呼び出してアラート/インシデントを調査するための小さめのAI SOC環境です。SOCの各タスクは VS Code の [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)(`SKILL.md`)として実装しています。

## ご利用にあたって(重要)

このリポジトリのSkill(`.github/skills/`配下の各`SKILL.md`)や `.github/copilot-instructions.md` は、**特定の1つの環境で観測できた限られたデータ(接続コネクタ、テーブル構成、実際に流れていたログの傾向など)をもとに作成したもの**です。そのため、お使いの環境でそのまま動かしてみて「それらしく動いている」ように見えたとしても、内容を鵜呑みにせず、必ず次のような観点でご自身の環境に照らして確認し、必要に応じて手を加えてからお使いください。

- **接続されているデータコネクタやテーブルが異なる**: Skillが前提としているテーブル(例: `DeviceProcessEvents`、`BehaviorAnalytics` など)が、お使いのワークスペースには存在しない、あるいは列構成が異なる場合があります。`schema` Skillの初期化手順で、まずご自身の環境のスキーマを取り直すことをおすすめします。
- **正常/異常の基準が組織ごとに異なる**: 「不審」として例示しているコマンドやパターンは、あくまで元の環境での一例です。組織で日常的に使う業務アプリや管理ツールを誤って異常と判定したり、逆に組織特有のリスクを見落としたりする可能性があります。
- **データ量や傾向による閾値のずれ**: サンプル件数や集計のしきい値は、元の環境のデータ量を前提に決めています。データ量が大きく異なる環境では、閾値やロジックの調整が必要になることがあります。
- **命名規則やレポート様式の前提**: ファイル名の識別子や重大度の扱いなど、細部は元の運用に合わせた一例です。ご自身のチームの運用に合わせて調整して問題ありません。

これらのSkillや指示書は完成品ではなく、**土台となる出発点**として用意しています。実際に使ってみて気づいた不整合や改善点は、都度 `SKILL.md` や `schema` のリファレンスファイルに反映し、ご自身の環境に合わせて育てていく前提の構成になっています。

## アーキテクチャ

```
Copilot Chat (このワークスペースのAgent Skills)
        │  ターミナルから Invoke-AzOperationalInsightsQuery を直接実行
        ▼
Azure Monitor Log Analytics Query API (読み取り専用)
        └─ SecurityIncident / SecurityAlert / SigninLogs / DeviceProcessEvents ... 等
```

インシデント・アラート・エンティティも含め、すべて **同じ1つのAPI(Log Analytics Query API)** 経由で取得します。このAPIはデータプレーンの読み取り専用APIであり、書き込み/削除の手段自体が存在しません。ラッパースクリプトは用意していません。KQLクエリは固定テンプレートを持たず、各Skillが調査の文脈に応じてその都度組み立て、`Invoke-AzOperationalInsightsQuery`(Az.OperationalInsightsモジュール)に直接渡します。

## セットアップ

1. 対象のLog Analyticsワークスペースに対して、自分のEntra IDアカウントに **Microsoft Sentinel Reader**(または Log Analytics Reader)ロールを割り当ててもらう。
2. 必要なPowerShellモジュールをインストールする:
   ```powershell
   Install-Module Az.Accounts, Az.OperationalInsights -Scope CurrentUser
   ```
3. サインインする(複数テナントがある場合は `Connect-AzAccount -TenantId <tenant-id>`):
   ```powershell
   Connect-AzAccount
   ```
4. `.env.example` を `.env` にコピーし、`AISOC_WORKSPACE_ID` を設定する。
   - ワークスペースID(customerId GUID)の確認: `az monitor log-analytics workspace list -o table`
   - `$env:AISOC_WORKSPACE_ID` としてシェルに読み込んでおく(各Skillはこの環境変数を前提とする)。
5. 動作確認:
   ```powershell
   Invoke-AzOperationalInsightsQuery -WorkspaceId $env:AISOC_WORKSPACE_ID -Query "SecurityIncident | take 1" -Timespan (New-TimeSpan -Hours 24)
   ```

## Skill一覧

| コマンド | 種別 | 用途 |
|---|---|---|
| `/incident` | 起点 | 特定のインシデント番号を深掘り調査(概況把握→専門Skillに自動委譲) |
| `/triage` | 起点 | 現在オープンな(New/Active)インシデントを一覧化・優先順位付け。値を指定しない横断ハント(怪しいユーザー/デバイス/アプリ/メールを探す)の起点にもなる |
| `/entity` | 起点 | インシデント化されていないエンティティ(ユーザー/デバイス/IP/アプリ/メール等)のアドホック調査 |
| `/identity` | 専門 | ユーザー/ID軸の深掘り(サインイン挙動・権限) |
| `/device` | 専門 | デバイス/エンドポイント軸の深掘り(プロセス・永続化・通信) |
| `/ti` | 専門 | IOC(IP/ドメイン/ハッシュ/URL)の脅威インテリジェンス照合 |
| `/app` | 専門 | OAuthアプリ/サービスプリンシパル軸の深掘り(同意状況・サインイン・権限スコープ) |
| `/email` | 専門 | メール/フィッシング軸の深掘り(配信結果・URL/添付ファイル・受信箱ルール改ざん) |
| `schema` | 背景知識 | 主要テーブル・列のリファレンス(`user-invocable: false`、必要な時に自動読込のみ) |

起点Skill(`incident`/`triage`/`entity`)と専門Skill(`identity`/`device`/`ti`/`app`/`email`)はすべて `context: fork` で実行されます。調査中の試行錯誤は親の会話を汚さず、最終結果だけが返ります。`context: fork` を使うには VS Code の設定 `github.copilot.chat.skillTool.enabled` を有効にしてください。

Skillは自然文からも自動的に選ばれます(例:「インシデント#123を調査して」→ `incident` Skillが自動発火)し、`/incident 123` のように明示的にスラッシュコマンドとしても呼べます。

## ガードレール

`.github/copilot-instructions.md` に方針として記載しています(コードでの強制はしていません):

- 探索的クエリの既定の時間範囲は7日間。長期侵害の兆候があれば、ワークスペースの保持期間の上限(90日)まで拡大する。
- クエリ結果が空/エラーの場合は正直に報告し、憶測で断定しない。

## `Reports/` ディレクトリ

各Skillは調査結果を `Reports/` 直下にフラットなHTMLレポートとして記録します。ファイル名にはインシデント番号、エンティティ種別と値、横断ハント対象などの識別子を含めます(詳細は `.github/copilot-instructions.md` の「レポート出力」参照)。テナントの機密情報を含みうるため `.gitignore` 済みで、コミットしないでください。

## ディレクトリ構成

```
.github/
├── copilot-instructions.md   # 全体方針(常時適用)
└── skills/
    ├── incident/SKILL.md
    ├── triage/SKILL.md
    ├── entity/SKILL.md
    ├── identity/SKILL.md
    ├── device/SKILL.md
    ├── ti/SKILL.md
    ├── app/SKILL.md
    ├── email/SKILL.md
    └── schema/SKILL.md
Reports/                       # 調査レポート(gitignore済み、直下にフラット配置)
```

D3.jsはレポートHTML内でCDNから読み込みます(HTMLファイル単体で受け渡しできるようにするため)。
