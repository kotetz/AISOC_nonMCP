# IdentityQueryEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: IdentityQueryEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| Timestamp | datetime |
| ActionType | string |
| Application | string |
| QueryType | string |
| QueryTarget | string |
| Query | string |
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
| ReportId | string |
| AdditionalFields | dynamic |
| SourceSystem | string |
| Type | string |
