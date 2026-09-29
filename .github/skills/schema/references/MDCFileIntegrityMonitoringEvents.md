# MDCFileIntegrityMonitoringEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-27T03:00:00Z
- Observed by search (365d): True
- Source: MDCFileIntegrityMonitoringEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| AzureResourceId | string |
| AADTenantID | string |
| Computer | string |
| CloudProvider | string |
| CloudIdentifier | string |
| CloudResourceType | string |
| MonitoredEntityType | string |
| ChangeType | string |
| FileName | string |
| FileType | string |
| FilePath | string |
| FileSize | long |
| OriginalFileName | string |
| OriginalFilePath | string |
| FileMd5 | string |
| FileSha256 | string |
| FileSha1 | string |
| RequestAccountName | string |
| RequestAccountDomain | string |
| RequestAccountSid | string |
| RequestSourceIP | string |
| RequestSourcePort | string |
| RequestSource | string |
| RegistryKey | string |
| RegistryHive | string |
| OldValueData | string |
| OldValueType | string |
| OldValueName | string |
| OldValueFullRegistryKey | string |
| NewValueData | string |
| NewValueType | string |
| NewValueName | string |
| InitiatingProcessId | long |
| InitiatingProcessName | string |
| InitiatingProcessCreationTime | datetime |
| InitiatingProcessSessionId | long |
| InitiatingProcessFirstSeen | datetime |
| InitiatingProcessAccountSid | string |
| InitiatingProcessAccountDomainName | string |
| InitiatingProcessAccountName | string |
| InitiatingProcessImageFileName | string |
| InitiatingProcessImageFilePath | string |
| InitiatingProcessImageFileType | string |
| InitProcImageFileSizeInBytes | long |
| InitProcImageCreationTimeUtc | datetime |
| InitProcImagePeTimestampUtc | datetime |
| InitProcImageLastWriteTimeUtc | datetime |
| InitProcImageLastAccessTimeUtc | datetime |
| InitProcImageLsHash | string |
| InitProcImageMd5 | string |
| InitProcImageSha256 | string |
| InitProcImageSha1 | string |
| InitiatingProcessSource | string |
| InitProcVersionInfoCompanyName | string |
| InitProcVersionInfoProductName | string |
| InitProcVersionInfoProductVersion | string |
| InitProcVersionInfoInternalFileName | string |
| InitProcVersionInfoOriginalFileName | string |
| InitProcVersionInfoFileDescription | string |
| SourceSystem | string |
| Type | string |
