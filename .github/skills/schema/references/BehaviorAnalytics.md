# BehaviorAnalytics

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: BehaviorAnalytics | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User keys are `UserName`/`UserPrincipalName`, with actor and target variants. Filter on basic columns first; a large `extend` containing many `column_ifexists()` calls has caused query failures.

| Column | Kusto type |
|---|---|
| TenantId | string |
| SourceRecordId | string |
| TimeGenerated | datetime |
| TimeProcessed | datetime |
| ActivityType | string |
| ActionType | string |
| UserName | string |
| UserPrincipalName | string |
| EventSource | string |
| SourceIPAddress | string |
| SourceIPLocation | string |
| SourceDevice | string |
| DestinationIPAddress | string |
| DestinationIPLocation | string |
| DestinationDevice | string |
| EventVendor | string |
| EventProductVersion | string |
| ActorName | string |
| ActorPrincipalName | string |
| TargetName | string |
| TargetPrincipalName | string |
| Device | string |
| UsersInsights | dynamic |
| DevicesInsights | dynamic |
| ActivityInsights | dynamic |
| SourceSystem | string |
| NativeTableName | string |
| InvestigationPriority | int |
| Type | string |
| _ResourceId | string |
