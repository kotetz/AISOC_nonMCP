# DeviceLogonEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: DeviceLogonEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: Logged-on user is `AccountName`; use `InitiatingProcessAccountUpn` when a UPN is required.

| Column | Kusto type |
|---|---|
| TenantId | string |
| AccountDomain | string |
| AccountName | string |
| AccountSid | string |
| ActionType | string |
| AdditionalFields | dynamic |
| AppGuardContainerId | string |
| DeviceId | string |
| DeviceName | string |
| FailureReason | string |
| InitiatingProcessAccountDomain | string |
| InitiatingProcessAccountName | string |
| InitiatingProcessAccountObjectId | string |
| InitiatingProcessAccountSid | string |
| InitiatingProcessAccountUpn | string |
| InitiatingProcessCommandLine | string |
| InitiatingProcessFileName | string |
| InitiatingProcessFolderPath | string |
| InitiatingProcessId | long |
| InitiatingProcessIntegrityLevel | string |
| InitiatingProcessMD5 | string |
| InitiatingProcessParentFileName | string |
| InitiatingProcessParentId | long |
| InitiatingProcessSHA1 | string |
| InitiatingProcessSHA256 | string |
| InitiatingProcessTokenElevation | string |
| IsLocalAdmin | bool |
| LogonId | long |
| LogonType | string |
| MachineGroup | string |
| Protocol | string |
| RemoteDeviceName | string |
| RemoteIP | string |
| RemoteIPType | string |
| RemotePort | int |
| ReportId | long |
| Timestamp | datetime |
| TimeGenerated | datetime |
| InitiatingProcessParentCreationTime | datetime |
| InitiatingProcessCreationTime | datetime |
| InitiatingProcessFileSize | long |
| InitiatingProcessVersionInfoCompanyName | string |
| InitiatingProcessVersionInfoFileDescription | string |
| InitiatingProcessVersionInfoInternalFileName | string |
| InitiatingProcessVersionInfoOriginalFileName | string |
| InitiatingProcessVersionInfoProductName | string |
| InitiatingProcessVersionInfoProductVersion | string |
| InitiatingProcessSessionId | long |
| IsInitiatingProcessRemoteSession | bool |
| InitiatingProcessRemoteSessionDeviceName | string |
| InitiatingProcessRemoteSessionIP | string |
| InitiatingProcessUniqueId | string |
| SourceSystem | string |
| Type | string |
