# DeviceCustomFileEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: DeviceCustomFileEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| ActionType | string |
| AdditionalFields | dynamic |
| AppGuardContainerId | string |
| DeviceId | string |
| DeviceName | string |
| FileName | string |
| FileOriginIP | string |
| FileOriginReferrerUrl | string |
| FileOriginUrl | string |
| FileSize | long |
| FolderPath | string |
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
| IsAzureInfoProtectionApplied | bool |
| MD5 | string |
| MachineGroup | string |
| PreviousFileName | string |
| PreviousFolderPath | string |
| ReportId | long |
| RequestAccountDomain | string |
| RequestAccountName | string |
| RequestAccountSid | string |
| RequestProtocol | string |
| RequestSourceIP | string |
| RequestSourcePort | int |
| SHA1 | string |
| SHA256 | string |
| SensitivityLabel | string |
| SensitivitySubLabel | string |
| ShareName | string |
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
| RuleName | string |
| RuleLastModificationTime | datetime |
| SourceSystem | string |
| Type | string |
