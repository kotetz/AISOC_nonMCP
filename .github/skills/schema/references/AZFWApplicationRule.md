# AZFWApplicationRule

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AZFWApplicationRule | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| Protocol | string |
| SourceIp | string |
| SourcePort | int |
| DestinationPort | int |
| Fqdn | string |
| TargetUrl | string |
| Action | string |
| Policy | string |
| RuleCollectionGroup | string |
| RuleCollection | string |
| Rule | string |
| ActionReason | string |
| IsTlsInspected | bool |
| WebCategory | string |
| IsExplicitProxyRequest | bool |
| SourceSystem | string |
| Type | string |
| _ResourceId | string |
