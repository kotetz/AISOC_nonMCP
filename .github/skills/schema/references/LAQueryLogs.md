# LAQueryLogs

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: LAQueryLogs | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| CorrelationId | string |
| RecordKind | string |
| AADObjectId | string |
| AADTenantId | string |
| AADEmail | string |
| AADClientId | string |
| ConditionalDataAccess | string |
| QueryTimeRangeStart | datetime |
| QueryTimeRangeEnd | datetime |
| QueryText | string |
| QueryThumbprint | string |
| RequestClientApp | string |
| RequestTarget | string |
| RequestContext | dynamic |
| RequestContextFilters | dynamic |
| ResponseCode | int |
| ResponseRowCount | int |
| ResponseDurationMs | real |
| StatsCPUTimeMs | real |
| StatsDataProcessedKB | real |
| StatsDataProcessedStart | datetime |
| StatsDataProcessedEnd | datetime |
| StatsWorkspaceCount | int |
| StatsRegionCount | int |
| IsBillableQuery | bool |
| ScannedGB | real |
| WorkspaceRegion | string |
| IsWorkspaceInFailover | bool |
| SourceSystem | string |
| Type | string |
| _ResourceId | string |
