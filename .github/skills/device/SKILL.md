---
name: device
description: デバイス/エンドポイント軸でプロセス実行・永続化・不審な通信を調査する。incident/entity Skillからホストが関わる調査を委譲された時、または「このデバイスを見て」のように直接デバイスを指定された時に使う。
argument-hint: "[device 値: DeviceName や DeviceId など]"
context: fork
---

# デバイス/エンドポイント軸の調査

対象デバイスについて、以下の観点を確認する。クエリは `Invoke-AzOperationalInsightsQuery -WorkspaceId $env:AISOC_WORKSPACE_ID -Timespan (New-TimeSpan -Hours <N>) -Query "<KQL>"` でその都度組み立てる。使用するテーブルが決まったら、`../schema/references/<TableName>.md` の共通スキーマを直接読む。複数テーブルを使う場合は必要なファイルだけを並列に読み、Currentのリファレンスがあるテーブルへ通常調査で`getschema`を実行しない。環境不一致・ファイル欠落・列エラー時は `schema` Skillの初期化・更新手順に従う。

## 着眼点

1. **プロセス実行チェーン**: 不審な親子プロセス、難読化されたコマンドライン(`DeviceProcessEvents`)
2. **永続化**: スケジュールタスク・レジストリRunキー・サービス登録(`DeviceRegistryEvents`, `DeviceProcessEvents`)
3. **ネットワーク**: 不審な宛先への接続、C2らしき通信パターン(`DeviceNetworkEvents`)
4. **ファイル操作**: 不審な場所への書き込み・実行可能ファイルの生成(`DeviceFileEvents`)
5. **ログオン**: 異常なログオン種別・アカウント(`DeviceLogonEvents`)
6. **保護状態**: AV/EDRの状態やシグネチャの鮮度(`ProtectionStatus`, `SecurityBaseline`)
7. **横展開**: 同一デバイスが関わる他のアラート/インシデント(`SecurityAlert`)

## 手順

1. 上記テーブルから関連しそうなものを選び、対象期間でKQLを組み立てて実行する。
2. プロセスツリーなど時系列で見るべきものは、`TimeGenerated`で並べて流れを追う。
3. 呼び出し元に、以下を返す:
   - 確認した観点ごとの結果(異常あり/なし)
   - 総合的な疑わしさの評価
   - 追加で確認すべき点があれば明記

## 注意事項

- このワークスペースには `DeviceCustom*`(`DeviceCustomProcessEvents`等)という標準MDEスキーマにない独自テーブルも存在するため、通常の`Device*`テーブルにデータがなくても`DeviceCustom*`系を確認する。
- 難読化PowerShellや`rundll32.exe`の実行件数だけで、不審なデバイスと判定しない。DefenderやWindowsの保守処理でも大量に発生するため、既知の正常なコマンドを除外し、High/Mediumアラート、UEBA、具体的な攻撃手法など独立したシグナルと突き合わせる。
