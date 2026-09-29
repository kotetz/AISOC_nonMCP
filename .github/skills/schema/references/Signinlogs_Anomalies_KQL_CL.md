# Signinlogs_Anomalies_KQL_CL

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-28T21:00:00Z
- Observed by search (365d): True
- Source: Signinlogs_Anomalies_KQL_CL | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| DetectedDateTime | datetime |
| UserPrincipalName | string |
| AnomalyType | string |
| Value | string |
| OS | string |
| BrowserFamily | string |
| RawBrowser | string |
| Country | string |
| City | string |
| State | string |
| CountryNovelty | bool |
| CityNovelty | bool |
| StateNovelty | bool |
| BaselineCountryCount | long |
| BaselineCityCount | long |
| BaselineStateCount | long |
| BaselineSize | long |
| RecentSize | long |
| FirstSeenRecent | datetime |
| ArtifactHits | long |
| BaselineIPList | dynamic |
| BaselineCountryList | dynamic |
| BaselineCityList | dynamic |
| BaselineStateList | dynamic |
| BaselineDeviceList | dynamic |
| BaselineOSList | dynamic |
| BaselineBrowserFamilyList | dynamic |
| BaselineRawBrowserList | dynamic |
| Severity | string |
| TimeGenerated | datetime |
| TenantId | string |
| Type | string |
| _ResourceId | string |
