# AppRequests

- Snapshot: 2026-09-29
- Observed by search (365d): True
- Source: AppRequests | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| Id | string |
| Source | string |
| Name | string |
| Url | string |
| Success | bool |
| ResultCode | string |
| DurationMs | real |
| PerformanceBucket | string |
| Properties | dynamic |
| Measurements | dynamic |
| OperationName | string |
| OperationId | string |
| OperationLinks | dynamic |
| ParentId | string |
| SyntheticSource | string |
| SessionId | string |
| UserId | string |
| UserAuthenticatedId | string |
| UserAccountId | string |
| AppVersion | string |
| AppRoleName | string |
| AppRoleInstance | string |
| ClientType | string |
| ClientModel | string |
| ClientOS | string |
| ClientIP | string |
| ClientCity | string |
| ClientStateOrProvince | string |
| ClientCountryOrRegion | string |
| ClientBrowser | string |
| ResourceGUID | string |
| IKey | string |
| SDKVersion | string |
| ItemCount | int |
| ReferencedItemId | string |
| ReferencedType | string |
| SourceSystem | string |
| Type | string |
| _ResourceId | string |
