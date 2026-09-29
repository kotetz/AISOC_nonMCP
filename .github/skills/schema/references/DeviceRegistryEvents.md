# DeviceRegistryEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: DeviceRegistryEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| ActionType | string |
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
| MachineGroup | string |
| PreviousRegistryKey | string |
| PreviousRegistryValueData | string |
| PreviousRegistryValueName | string |
| RegistryKey | string |
| RegistryValueData | string |
| RegistryValueName | string |
| RegistryValueType | string |
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
| SourceSystem | string |
| Type | string |
