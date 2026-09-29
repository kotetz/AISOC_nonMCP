# StorageBlobLogs

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T09:00:00Z
- Observed by search (365d): True
- Source: StorageBlobLogs | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| AccountName | string |
| Location | string |
| Protocol | string |
| OperationName | string |
| AuthenticationType | string |
| StatusCode | string |
| StatusText | string |
| DurationMs | real |
| ServerLatencyMs | real |
| Uri | string |
| CallerIpAddress | string |
| CorrelationId | string |
| SchemaVersion | string |
| OperationVersion | string |
| AuthenticationHash | string |
| RequesterObjectId | string |
| RequesterTenantId | string |
| RequesterAppId | string |
| RequesterAudience | string |
| RequesterTokenIssuer | string |
| RequesterUpn | string |
| AuthorizationDetails | dynamic |
| UserAgentHeader | string |
| ReferrerHeader | string |
| ClientRequestId | string |
| Etag | string |
| ServiceType | string |
| OperationCount | int |
| ObjectKey | string |
| RequestHeaderSize | long |
| RequestBodySize | long |
| ResponseHeaderSize | long |
| ResponseBodySize | long |
| RequestMd5 | string |
| ResponseMd5 | string |
| LastModifiedTime | datetime |
| ConditionsUsed | string |
| ContentLengthHeader | long |
| Category | string |
| TlsVersion | string |
| SasExpiryStatus | string |
| MetricResponseType | string |
| SourceUri | string |
| DestinationUri | string |
| AccessTier | string |
| SourceAccessTier | string |
| RehydratePriority | string |
| EncryptionKeyTypeOfBlob | string |
| RequestRegion | string |
| TrafficClassification | string |
| CopyDestinationArmId | string |
| SourceSystem | string |
| Type | string |
| _ResourceId | string |
