# IdentityInfo

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: IdentityInfo | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User keys are `AccountUPN`/`AccountName`; useful risk and privilege fields include `RiskLevel`, `RiskState`, `InvestigationPriority`, and `AssignedRoles`.

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| AccountName | string |
| AccountDomain | string |
| AccountUPN | string |
| AccountSID | string |
| AccountObjectId | string |
| AccountTenantId | string |
| AccountDisplayName | string |
| GivenName | string |
| Surname | string |
| OnPremisesAccountObjectId | string |
| OnPremisesExtensionAttributes | string |
| OnPremisesDistinguishedName | string |
| Tags | string |
| AccountCreationTime | datetime |
| InvestigationPriority | int |
| InvestigationPriorityPercentile | int |
| RiskLevel | string |
| RiskLevelDetails | string |
| RiskState | string |
| BlastRadius | string |
| GroupMembership | dynamic |
| AssignedRoles | dynamic |
| Department | string |
| EmployeeId | string |
| JobTitle | string |
| RelatedAccounts | dynamic |
| MailAddress | string |
| AdditionalMailAddresses | dynamic |
| Manager | string |
| StreetAddress | string |
| City | string |
| CompanyName | string |
| Country | string |
| State | string |
| Phone | string |
| IsAccountEnabled | bool |
| IsServiceAccount | bool |
| DeletedDateTime | datetime |
| LastSeenDate | datetime |
| UACFlags | string |
| UserState | string |
| UserStateChangedOn | datetime |
| UserType | string |
| ExtensionProperty | dynamic |
| AccountCloudSID | string |
| IsMFARegistered | bool |
| Applications | string |
| ServicePrincipals | dynamic |
| SourceSystem | string |
| UserAccountControl | dynamic |
| ChangeSource | string |
| EntityRiskScore | dynamic |
| SAMAccountName | string |
| Type | string |
