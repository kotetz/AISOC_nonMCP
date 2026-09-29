# AuditLogs

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AuditLogs | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: Actor UPN is under `InitiatedBy.user.userPrincipalName`; target UPN is in the `TargetResources` array. Because `TargetResources[].modifiedProperties` is nested again, prefer a narrow projection and `tostring(...) has ...` before using multiple `mv-expand` operations.

| Column | Kusto type |
|---|---|
| TenantId | string |
| SourceSystem | string |
| TimeGenerated | datetime |
| ResourceId | string |
| OperationName | string |
| OperationVersion | string |
| Category | string |
| ResultType | string |
| ResultSignature | string |
| ResultDescription | string |
| DurationMs | long |
| CorrelationId | string |
| Resource | string |
| ResourceGroup | string |
| ResourceProvider | string |
| Identity | string |
| Level | string |
| Location | string |
| AdditionalDetails | dynamic |
| Id | string |
| InitiatedBy | dynamic |
| LoggedByService | string |
| Result | string |
| ResultReason | string |
| TargetResources | dynamic |
| AADTenantId | string |
| ActivityDisplayName | string |
| ActivityDateTime | datetime |
| AADOperationType | string |
| Type | string |
