# IdentityLogonEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: IdentityLogonEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| Timestamp | datetime |
| ActionType | string |
| Application | string |
| LogonType | string |
| Protocol | string |
| FailureReason | string |
| AccountName | string |
| AccountDomain | string |
| AccountUpn | string |
| AccountSid | string |
| AccountObjectId | string |
| AccountDisplayName | string |
| DeviceName | string |
| DeviceType | string |
| OSPlatform | string |
| IPAddress | string |
| Port | string |
| DestinationDeviceName | string |
| DestinationIPAddress | string |
| DestinationPort | string |
| TargetDeviceName | string |
| TargetAccountDisplayName | string |
| Location | string |
| ISP | string |
| ReportId | string |
| AdditionalFields | dynamic |
| LastSeenForUser | dynamic |
| UncommonForUser | dynamic |
| SourceSystem | string |
| Type | string |
