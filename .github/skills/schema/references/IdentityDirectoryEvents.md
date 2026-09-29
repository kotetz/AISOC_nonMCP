# IdentityDirectoryEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: IdentityDirectoryEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User keys are `AccountUpn`/`AccountName`; target user is `TargetAccountUpn`. Parse `AdditionalFields` with `parse_json()`/`todynamic()`; `extractjson()` is not a valid function in this workspace.

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| Timestamp | datetime |
| ActionType | string |
| Application | string |
| Protocol | string |
| AccountName | string |
| AccountDomain | string |
| AccountUpn | string |
| AccountSid | string |
| AccountObjectId | string |
| AccountDisplayName | string |
| DeviceName | string |
| IPAddress | string |
| Port | string |
| DestinationDeviceName | string |
| DestinationIPAddress | string |
| DestinationPort | string |
| TargetDeviceName | string |
| TargetAccountUpn | string |
| TargetAccountDisplayName | string |
| Location | string |
| ISP | string |
| ReportId | string |
| AdditionalFields | dynamic |
| SourceSystem | string |
| Type | string |
