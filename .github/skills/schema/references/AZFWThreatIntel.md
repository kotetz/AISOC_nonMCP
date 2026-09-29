# AZFWThreatIntel

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T08:00:00Z
- Observed by search (365d): True
- Source: AZFWThreatIntel | getschema
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
| Fqdn | string |
| TargetUrl | string |
| Action | string |
| ThreatDescription | string |
| IsTlsInspected | bool |
| SourceSystem | string |
| Type | string |
| _ResourceId | string |
