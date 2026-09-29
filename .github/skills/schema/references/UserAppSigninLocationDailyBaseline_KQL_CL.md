# UserAppSigninLocationDailyBaseline_KQL_CL

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-28T17:00:00Z
- Observed by search (365d): True
- Source: UserAppSigninLocationDailyBaseline_KQL_CL | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| Day | string |
| AppDisplayName | string |
| UserPrincipalName | string |
| LocationList | dynamic |
| LocationCount | long |
| DistinctSourceIp | long |
| LogonCount | long |
| TimeGenerated | datetime |
| TenantId | string |
| Type | string |
| _ResourceId | string |
