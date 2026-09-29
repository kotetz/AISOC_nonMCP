# AZFWNetworkRuleAggregation

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AZFWNetworkRuleAggregation | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| Protocol | string |
| SourceIp | string |
| DestinationIp | string |
| DestinationPort | int |
| Action | string |
| ActionReason | string |
| Policy | string |
| RuleCollectionGroup | string |
| RuleCollection | string |
| Rule | string |
| IsDefaultRule | bool |
| NetworkRuleCount | int |
| SourceSystem | string |
| Type | string |
| _ResourceId | string |
