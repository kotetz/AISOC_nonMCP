# AzureMetrics

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): False
- Source: Log Analytics Search API, `AzureMetrics | take 1`
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Note: This Basic Logs table is not supported by the standard Query API used by `Invoke-AzOperationalInsightsQuery`.

| Column | Kusto type |
|---|---|
| TenantId | string |
| SourceSystem | string |
| TimeGenerated | datetime |
| ResourceId | string |
| OperationName | string |
| OperationVersion | string |
| Category | string |
| ResultType | string |
| ResultSignature | string |
| ResultDescription | string |
| DurationMs | long |
| CallerIpAddress | string |
| CorrelationId | string |
| Resource | string |
| ResourceGroup | string |
| ResourceProvider | string |
| SubscriptionId | string |
| MetricName | string |
| Total | real |
| Count | real |
| Maximum | real |
| Minimum | real |
| Average | real |
| TimeGrain | string |
| UnitName | string |
| RemoteIPCountry | string |
| RemoteIPLatitude | real |
| RemoteIPLongitude | real |
| MaliciousIP | string |
| IndicatorThreatType | string |
| Description | string |
| TLPLevel | string |
| Confidence | string |
| Severity | int |
| FirstReportedDateTime | string |
| LastReportedDateTime | string |
| IsActive | string |
| ReportReferenceLink | string |
| AdditionalInformation | string |
| Type | string |
| _ResourceId | string |
