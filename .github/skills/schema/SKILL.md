---
name: schema
description: このSentinelワークスペースに接続されているデータソース(テーブル)と主要な列のリファレンス。KQLを組み立てる前に、どのテーブル・列を使うべきか確認する時に使う。
user-invocable: false
---

# ワークスペーススキーマ・リファレンス

`Usage | summarize by DataType` で確認した、このワークスペースの主要な接続済みデータソース(調査時点、データ量の多い順の抜粋)。新しいテーブルを使う前に `<TableName> | getschema` または `<TableName> | take 1` で実際の列を確認すること。列名は環境によって変わりうるため、ここに書かれた列名は目安として扱う。

## ID / Entra ID
- `SigninLogs`, `AADNonInteractiveUserSignInLogs`, `MicrosoftServicePrincipalSignInLogs`, `AADServicePrincipalSignInLogs`, `AADManagedIdentitySignInLogs`
- `AuditLogs`, `AADProvisioningLogs`
- `IdentityInfo`, `IdentityLogonEvents`, `IdentityQueryEvents`, `IdentityDirectoryEvents`(Defender for Identity)
- `BehaviorAnalytics`, `UserPeerAnalytics`(UEBA)
- `AADUserRiskEvents`, `AADRiskyUsers`(Identity Protection)
- `Watchlist`

## エンドポイント (Defender for Endpoint)
- `DeviceProcessEvents`, `DeviceNetworkEvents`, `DeviceFileEvents`, `DeviceRegistryEvents`, `DeviceEvents`, `DeviceImageLoadEvents`, `DeviceLogonEvents`, `DeviceInfo`, `DeviceNetworkInfo`, `DeviceFileCertificateInfo`
- `DeviceCustomImageLoadEvents`, `DeviceCustomFileEvents`, `DeviceCustomScriptEvents`, `DeviceCustomNetworkEvents`, `DeviceCustomProcessEvents` — このワークスペース固有のカスタムテレメトリ(標準MDEスキーマではない)。演習/シミュレーション由来の可能性があるため、標準テーブルにデータがない場合はこちらも確認する。
- `ProtectionStatus`, `SecurityBaseline`, `SecurityBaselineSummary`

## SaaS / クラウドアプリ / メール
- `CloudAppEvents`(Defender for Cloud Apps)
- `OfficeActivity`
- `EmailEvents`, `EmailUrlInfo`, `EmailAttachmentInfo`, `EmailPostDeliveryEvents`, `UrlClickEvents`, `AlertEvidence`, `AlertInfo`(Defender for Office 365)
- `MicrosoftGraphActivityLogs`, `GraphNotificationsActivityLogs`, `CopilotActivity`, `DataverseActivity`
- `MicrosoftPurviewInformationProtection`

## マルチクラウド / ネットワーク
- `AWSCloudTrail`
- `AzureActivity`, `AzureDiagnostics`, `AzureMetrics`
- `AZFWDnsQuery`, `AZFWFlowTrace`, `AZFWNetworkRule`, `AZFWApplicationRule`, `AZFWNatRule`, `AZFWThreatIntel` 等(Azure Firewall)
- `NetworkAccessConnectionEvents`, `NetworkAccessTraffic`(Global Secure Access)

## 脅威インテリジェンス
- `ThreatIntelIndicators`, `ThreatIntelObjects`

## Sentinel本体 / インシデント
- `SecurityIncident` — インシデント本体。主要列: `IncidentNumber`, `Title`, `Severity`, `Status`, `Classification`, `Owner`, `CreatedTime`, `LastModifiedTime`, `AlertIds`(dynamic), `Labels`(dynamic)
- `SecurityAlert` — アラート本体。主要列: `SystemAlertId`, `AlertName`, `AlertSeverity`, `Entities`(dynamic, エンティティのJSON配列), `Tactics`, `Techniques`, `ProductName`
- `SentinelHealth`, `SentinelAudit`, `LAQueryLogs`, `Anomalies`

## その他(このテナント固有)
- `SAPBTPAuditLog_CL`, `SAPLogServ_CL`(SAP連携)
- `IntuneAuditLogs`, `IntuneDevices`, `IntuneDeviceComplianceOrg`
- `*_KQL_CL` という命名の複数のカスタムテーブル(例: `PasswordSprayIPs_KQL_CL`, `Signinlogs_Anomalies_KQL_CL`, `UserAppSigninLocationDailyBaseline_KQL_CL`)は演習/デモ用に事前計算された派生テーブルの可能性が高い。関連しそうな調査の際は存在を確認する価値がある。

## 過去の調査で判明済みの注意点(列の全量列挙はしない、要点のみ)

以下のテーブルは既に複数回のユーザー/ID軸調査で使用済み。**ユーザーを特定する列名がテーブルごとに異なる**点が最大のハマりどころなので、そこだけ明記する。それ以外の列が必要な場合は都度 `getschema` で確認すること(このリストは`getschema`を代替するものではない)。

- `SigninLogs`: ユーザー列は `UserPrincipalName`。`RiskLevelAggregated`/`RiskState`/`RiskDetail`/`IsRisky`などリスク列あり。
- `AADNonInteractiveUserSignInLogs`: ユーザー列は `UserPrincipalName`。ただし `SigninLogs` と違い `RiskLevelAggregated`/`RiskState`/`RiskDetail` は**存在しない**(参照するとBadRequestになった実績あり)。
- `AuditLogs`: 実行者は `InitiatedBy.user.userPrincipalName`、対象は `TargetResources`(dynamic配列)の `userPrincipalName`。`TargetResources[].modifiedProperties` はさらにネストしたdynamic配列で、`mv-expand`を二重にかけると失敗しやすい(実績あり)。`tostring(...)` して `has` で粗く絞る方が安定。
- `IdentityDirectoryEvents`(Defender for Identity): ユーザー列は `AccountUpn`/`AccountName`(対象側は `TargetAccountUpn`)。詳細は `AdditionalFields`(dynamic)。JSON抽出は `extractjson()` ではなく `parse_json()`/`todynamic()` を使う(`extractjson`は存在しない関数名でBadRequestになった実績あり)。
- `BehaviorAnalytics`: ユーザー列は `UserName`/`UserPrincipalName`(行為者 `ActorName`系、対象 `TargetName`系)。`column_ifexists`を多数並べた巨大な`extend`は失敗しやすい(実績あり)。基本列だけでまず絞り込んでから詳細列を足す方が安定。
- `AADUserRiskEvents` / `AADRiskyUsers`: ユーザー列は共通で `UserPrincipalName`。
- `IdentityInfo`: ユーザー列は `AccountUPN`/`AccountName`。`RiskLevel`/`RiskState`/`InvestigationPriority`/`AssignedRoles`などアカウント状態の列が豊富。
- `DeviceLogonEvents`: ユーザー列は `AccountName`(UPNで絞るなら `InitiatingProcessAccountUpn`)。
- `AWSCloudTrail`: ユーザー列は `UserIdentityUserName`/`SessionIssuerUserName`(ARNに名前が含まれる場合は `UserIdentityArn`/`SessionIssuerArn`)。

## 使い方の指針

- テーブル名だけでなく実際の列名は変わりうるため、初めて使うテーブルは `<TableName> | take 1` または `<TableName> | getschema` で確認してから本クエリを組み立てる。
- `dynamic`型の列(`Entities`, `AlertIds`, `Labels`等)は `Invoke-AzOperationalInsightsQuery` の結果ではJSON文字列として返る。KQL側で`mv-expand`/`parse_json`を使って展開・集計するのが簡単な場合が多い。
