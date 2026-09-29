# SecurityIncident

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: SecurityIncident | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| IncidentName | string |
| Title | string |
| Description | string |
| Severity | string |
| Status | string |
| Classification | string |
| ClassificationComment | string |
| ClassificationReason | string |
| Owner | dynamic |
| ProviderName | string |
| ProviderIncidentId | string |
| FirstActivityTime | datetime |
| LastActivityTime | datetime |
| FirstModifiedTime | datetime |
| LastModifiedTime | datetime |
| CreatedTime | datetime |
| ClosedTime | datetime |
| IncidentNumber | int |
| RelatedAnalyticRuleIds | dynamic |
| AlertIds | dynamic |
| BookmarkIds | dynamic |
| Comments | dynamic |
| Tasks | dynamic |
| Labels | dynamic |
| IncidentUrl | string |
| AdditionalData | dynamic |
| ModifiedBy | string |
| SourceSystem | string |
| Type | string |
