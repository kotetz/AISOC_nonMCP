# AADRiskyUsers

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AADRiskyUsers | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User key is `UserPrincipalName`.

| Column | Kusto type |
|---|---|
| TenantId | string |
| Id | string |
| IsDeleted | bool |
| IsProcessing | bool |
| RiskDetail | string |
| RiskLastUpdatedDateTime | datetime |
| RiskLevel | string |
| RiskState | string |
| UserDisplayName | string |
| UserPrincipalName | string |
| TimeGenerated | datetime |
| OperationName | string |
| CorrelationId | string |
| SourceSystem | string |
| Type | string |
