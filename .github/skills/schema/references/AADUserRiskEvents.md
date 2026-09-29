# AADUserRiskEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T08:00:00Z
- Observed by search (365d): True
- Source: AADUserRiskEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User key is `UserPrincipalName`.

| Column | Kusto type |
|---|---|
| TenantId | string |
| Activity | string |
| ActivityDateTime | datetime |
| AdditionalInfo | dynamic |
| CorrelationId | string |
| DetectedDateTime | datetime |
| DetectionTimingType | string |
| Id | string |
| IpAddress | string |
| LastUpdatedDateTime | datetime |
| Location | dynamic |
| RequestId | string |
| RiskDetail | string |
| RiskEventType | string |
| RiskLevel | string |
| RiskState | string |
| Source | string |
| TokenIssuerType | string |
| UserDisplayName | string |
| UserId | string |
| UserPrincipalName | string |
| TimeGenerated | datetime |
| OperationName | string |
| SourceSystem | string |
| Type | string |
