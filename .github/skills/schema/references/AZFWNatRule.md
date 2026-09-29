# AZFWNatRule

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AZFWNatRule | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| Protocol | string |
| SourceIp | string |
| SourcePort | int |
| DestinationIp | string |
| DestinationPort | int |
| TranslatedIp | string |
| TranslatedPort | int |
| Policy | string |
| RuleCollectionGroup | string |
| RuleCollection | string |
| Rule | string |
| SourceSystem | string |
| Type | string |
| _ResourceId | string |
