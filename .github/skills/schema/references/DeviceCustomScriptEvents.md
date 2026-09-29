# DeviceCustomScriptEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: DeviceCustomScriptEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| ActionType | string |
| DeviceId | string |
| DeviceName | string |
| ReportId | long |
| Timestamp | datetime |
| TimeGenerated | datetime |
| InitiatingProcessId | long |
| InitiatingProcessCreationTime | datetime |
| InitiatingProcessCommandLine | string |
| InitiatingProcessParentFileName | string |
| InitiatingProcessParentId | long |
| InitiatingProcessParentCreationTime | datetime |
| InitiatingProcessSHA1 | string |
| InitiatingProcessSHA256 | string |
| InitiatingProcessMD5 | string |
| InitiatingProcessFileName | string |
| InitiatingProcessFolderPath | string |
| InitiatingProcessAccountName | string |
| InitiatingProcessAccountDomain | string |
| InitiatingProcessSignatureStatus | string |
| InitiatingProcessSignerType | string |
| InitiatingProcessAccountSid | string |
| InitiatingProcessAccountUpn | string |
| InitiatingProcessAccountObjectId | string |
| InitiatingProcessFileSize | long |
| InitiatingProcessVersionInfoCompanyName | string |
| InitiatingProcessVersionInfoProductName | string |
| InitiatingProcessVersionInfoProductVersion | string |
| InitiatingProcessVersionInfoInternalFileName | string |
| InitiatingProcessVersionInfoOriginalFileName | string |
| InitiatingProcessVersionInfoFileDescription | string |
| InitiatingProcessSessionId | long |
| IsInitiatingProcessRemoteSession | bool |
| InitiatingProcessRemoteSessionDeviceName | string |
| InitiatingProcessRemoteSessionIP | string |
| InitiatingProcessUniqueId | string |
| ScriptContent | string |
| ScriptContentSHA256 | string |
| RuleName | string |
| RuleLastModificationTime | datetime |
| SourceSystem | string |
| Type | string |
