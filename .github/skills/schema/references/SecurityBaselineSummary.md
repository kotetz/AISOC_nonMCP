# SecurityBaselineSummary

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-28T19:00:00Z
- Observed by search (365d): True
- Source: SecurityBaselineSummary | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| SourceSystem | string |
| MG | string |
| ManagementGroupName | string |
| SourceComputerId | string |
| TimeGenerated | datetime |
| SubscriptionId | string |
| ResourceGroup | string |
| ResourceProvider | string |
| Resource | string |
| ResourceId | string |
| ResourceType | string |
| ComputerEnvironment | string |
| Computer | string |
| BaselineId | string |
| BaselineType | string |
| OSName | string |
| AssessmentId | string |
| TotalAssessedRules | int |
| PercentageOfPassedRules | int |
| CriticalFailedRules | int |
| WarningFailedRules | int |
| InformationalFailedRules | int |
| Type | string |
| _ResourceId | string |
