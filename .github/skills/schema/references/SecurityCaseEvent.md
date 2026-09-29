# SecurityCaseEvent

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: SecurityCaseEvent | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| RecordId | string |
| AadTenantId | string |
| EntityType | string |
| EntityId | string |
| ParentEntityId | string |
| OperationName | string |
| PropertyNames | dynamic |
| PreviousValues | dynamic |
| NewValues | dynamic |
| EventTime | datetime |
| ModifiedBy | string |
| IsDeleted | bool |
| EntityCreatedTime | datetime |
| SourceSystem | string |
| Type | string |
