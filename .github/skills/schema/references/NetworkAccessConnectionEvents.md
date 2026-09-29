# NetworkAccessConnectionEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-25T06:00:00Z
- Observed by search (365d): True
- Source: NetworkAccessConnectionEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| TimeGenerated | datetime |
| ConnectionId | string |
| TrafficType | string |
| EventType | string |
| DeviceCategory | string |
| DestinationIp | string |
| DestinationPort | int |
| DestinationFqdn | string |
| SourceIp | string |
| SourcePrivateIp | string |
| RemoteNetworkSourceIp | string |
| SourcePort | int |
| DeviceOperatingSystem | string |
| DeviceOperatingSystemVersion | string |
| AgentVersion | string |
| DeviceId | string |
| ClientDeviceName | string |
| UserId | string |
| UserPrincipalName | string |
| TransportProtocol | string |
| NetworkProtocol | string |
| InitiatingProcessName | string |
| AppId | string |
| PopProcessingRegion | string |
| RemoteNetworkId | string |
| Token3PExpiry | datetime |
| Token3PValidFrom | datetime |
| Token3PIssuedAt | datetime |
| Token3PUniqueId | string |
| SecurityProfileId | string |
| SecurityProfileName | string |
| SecurityProfileVersion | string |
| SecurityPolicyId | string |
| SecurityPolicyName | string |
| SecurityPolicyVersion | string |
| SecurityRuleId | string |
| IsLocal | bool |
| HomeTenantId | string |
| CrossTenantAccessType | string |
| DeviceJoinType | string |
| SourceIpCountryCode | string |
| SourceIpState | string |
| SourceIpStateCode | string |
| SourceIpCity | string |
| SourceIpLatitude | real |
| SourceIpLongitude | real |
| SourceIpAutonomousSystemNumber | string |
| SourceIpCarrier | string |
| PrivateSourceIp | string |
| SecurityPrincipalType | string |
| ForwardingProfileId | string |
| ForwardingProfileName | string |
| SourceSystem | string |
| Type | string |
