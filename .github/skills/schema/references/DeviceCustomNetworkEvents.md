# DeviceCustomNetworkEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: DeviceCustomNetworkEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| ActionType | string |
| AdditionalFields | dynamic |
| AppGuardContainerId | string |
| DeviceId | string |
| DeviceName | string |
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
| InitiatingProcessFileSize | long |
| InitiatingProcessVersionInfoCompanyName | string |
| InitiatingProcessVersionInfoProductName | string |
| InitiatingProcessVersionInfoProductVersion | string |
| InitiatingProcessVersionInfoInternalFileName | string |
| InitiatingProcessVersionInfoOriginalFileName | string |
| InitiatingProcessVersionInfoFileDescription | string |
| LocalIP | string |
| LocalIPType | string |
| LocalPort | int |
| MachineGroup | string |
| Protocol | string |
| RemoteIP | string |
| RemoteIPType | string |
| RemotePort | int |
| RemoteUrl | string |
| ReportId | long |
| TimeGenerated | datetime |
| Timestamp | datetime |
| InitiatingProcessParentCreationTime | datetime |
| InitiatingProcessCreationTime | datetime |
| InitiatingProcessSessionId | long |
| IsInitiatingProcessRemoteSession | bool |
| InitiatingProcessRemoteSessionDeviceName | string |
| InitiatingProcessRemoteSessionIP | string |
| InitiatingProcessUniqueId | string |
| RuleName | string |
| RuleLastModificationTime | datetime |
| SourceSystem | string |
| Type | string |
