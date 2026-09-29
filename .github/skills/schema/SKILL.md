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

## 使い方の指針

- テーブル名だけでなく実際の列名は変わりうるため、初めて使うテーブルは `<TableName> | take 1` または `<TableName> | getschema` で確認してから本クエリを組み立てる。
- `dynamic`型の列(`Entities`, `AlertIds`, `Labels`等)は`aisoc`のPythonクライアント側でJSONとしてパース済みで返る。`aisoc query`で生のKQL結果を直接見る場合はJSON文字列のまま返ることがある点に注意する。
