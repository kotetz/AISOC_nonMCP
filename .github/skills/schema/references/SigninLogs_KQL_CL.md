# SigninLogs_KQL_CL

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-28T22:00:00Z
- Observed by search (365d): True
- Source: SigninLogs_KQL_CL | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TimeGenerated | datetime |
| UserPrincipalName | string |
| UserId | string |
| AppDisplayName | string |
| ClientAppUsed | string |
| AuthenticationRequirement | string |
| ConditionalAccessStatus | string |
| RiskLevelAggregated | string |
| RiskState | string |
| RiskDetail | string |
| Location | dynamic |
| IPAddress | string |
| DeviceDetail | dynamic |
| Status | dynamic |
| TenantId | string |
| Type | string |
| _ResourceId | string |
