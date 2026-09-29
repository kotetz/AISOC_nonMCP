# AI SOC — Sentinel Investigation Workspace

Microsoft Sentinel MCP を使わず、Log Analytics Query API を直接呼び出してアラート/インシデントを調査するための小さめのAI SOC環境です。SOCの各タスクは VS Code の [Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills)(`SKILL.md`)として実装しています。

## アーキテクチャ

```
Copilot Chat (このワークスペースのAgent Skills)
        │  ターミナルから `aisoc` CLI を実行
        ▼
src/aisoc/  ── 薄いPythonクライアント
        │  azure-identity (DefaultAzureCredential) + azure-monitor-query
        ▼
Azure Monitor Log Analytics Query API (読み取り専用)
        └─ SecurityIncident / SecurityAlert / SigninLogs / DeviceProcessEvents ... 等
```

インシデント・アラート・エンティティも含め、すべて **同じ1つのAPI(Log Analytics Query API)** 経由で取得します。このAPIはデータプレーンの読み取り専用APIであり、書き込み/削除の手段自体が存在しません。KQLクエリは固定テンプレートを持たず、各Skillが調査の文脈に応じてその都度組み立てます。

## セットアップ

1. 対象のLog Analyticsワークスペースに対して、自分のEntra IDアカウントに **Microsoft Sentinel Reader**(または Log Analytics Reader)ロールを割り当ててもらう。
2. `az login` でサインインする(複数テナントがある場合は `az login --tenant <tenant-id>`)。
3. `.env.example` を `.env` にコピーし、`AISOC_WORKSPACE_ID` を設定する。
   - ワークスペースID(customerId GUID)の確認: `az monitor log-analytics workspace list -o table`
4. 依存関係をインストールする(エディタブルインストールで `aisoc` コマンドが使えるようになる):
   ```powershell
   pip install -e .
   ```
5. 動作確認:
   ```powershell
   aisoc query "SecurityIncident | take 1" --hours 24
   ```

## Skill一覧

| コマンド | 種別 | 用途 |
|---|---|---|
| `/incident` | 起点 | 特定のインシデント番号を深掘り調査(概況把握→専門Skillに自動委譲) |
| `/triage` | 起点 | 現在オープンな(New/Active)インシデントを一覧化・優先順位付け |
| `/entity` | 起点 | インシデント化されていないエンティティ(ユーザー/デバイス/IP等)のアドホック調査 |
| `/identity` | 専門 | ユーザー/ID軸の深掘り(サインイン挙動・権限) |
| `/device` | 専門 | デバイス/エンドポイント軸の深掘り(プロセス・永続化・通信) |
| `/ti` | 専門 | IOC(IP/ドメイン/ハッシュ/URL)の脅威インテリジェンス照合 |
| `schema` | 背景知識 | 主要テーブル・列のリファレンス(`user-invocable: false`、必要な時に自動読込のみ) |

起点Skill(`incident`/`triage`/`entity`)と専門Skill(`identity`/`device`/`ti`)はすべて `context: fork` で実行されます。調査中の試行錯誤は親の会話を汚さず、最終結果だけが返ります。`context: fork` を使うには VS Code の設定 `github.copilot.chat.skillTool.enabled` を有効にしてください。

Skillは自然文からも自動的に選ばれます(例:「インシデント#123を調査して」→ `incident` Skillが自動発火)し、`/incident 123` のように明示的にスラッシュコマンドとしても呼べます。

## CLIコマンド (`aisoc`)

```powershell
aisoc query "<KQL>" [--hours 24] [--max-rows 500]
aisoc incident get <incident-number>
aisoc incident alerts <incident-number>
aisoc incident entities <incident-number>
aisoc triage [--hours 720] [--severity High,Medium]
```

## ガードレール(`src/aisoc/guardrails.py`)

- 探索的クエリ(`aisoc query`)の既定の時間範囲は24時間、最大7日にクランプされます。
- インシデント/アラートの厳密一致検索(`aisoc incident ...`)は例外的に最大1年まで遡れます(exact-matchなので低コスト)。
- 1回のクエリで返す行数は既定500行までです。
- サーバータイムアウトは60秒です。
- `.`から始まる制御コマンドは拒否します(本APIはそもそも読み取り専用なので実害はありませんが、念のためです)。

## `cases/` ディレクトリ

各Skillは調査結果を `cases/<incident-number>/` または `cases/adhoc-<entity-value>/` 配下にMarkdownで記録します。テナントの機密情報を含みうるため `.gitignore` 済みで、コミットしないでください。

## テスト

```powershell
pip install -e ".[dev]"
pytest
```

`tests/` はすべて `run_kql` をモックしており、実際のAzure環境へは接続しません。

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
    └── schema/SKILL.md
src/aisoc/                     # 薄いPythonクライアント(CLI)
cases/                         # 調査ごとの記録(gitignore済み)
tests/                         # run_kqlをモックした単体テスト
```
