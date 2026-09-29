# EmailEvents

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: EmailEvents | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| AttachmentCount | int |
| AuthenticationDetails | string |
| AdditionalFields | dynamic |
| ConfidenceLevel | string |
| Connectors | string |
| DetectionMethods | string |
| DeliveryAction | string |
| DeliveryLocation | string |
| EmailClusterId | long |
| EmailDirection | string |
| EmailLanguage | string |
| EmailAction | string |
| EmailActionPolicy | string |
| EmailActionPolicyGuid | string |
| OrgLevelAction | string |
| OrgLevelPolicy | string |
| InternetMessageId | string |
| NetworkMessageId | string |
| RecipientEmailAddress | string |
| RecipientObjectId | string |
| ReportId | string |
| SenderDisplayName | string |
| SenderFromAddress | string |
| SenderFromDomain | string |
| SenderObjectId | string |
| SenderIPv4 | string |
| SenderIPv6 | string |
| SenderMailFromAddress | string |
| SenderMailFromDomain | string |
| Subject | string |
| ThreatTypes | string |
| ThreatNames | string |
| TimeGenerated | datetime |
| LastEventExecutionTime | datetime |
| Timestamp | datetime |
| UrlCount | int |
| UserLevelAction | string |
| UserLevelPolicy | string |
| BulkComplaintLevel | int |
| LatestDeliveryLocation | string |
| LatestDeliveryAction | string |
| ExchangeTransportRule | string |
| DistributionList | string |
| ForwardingInformation | string |
| Context | string |
| To | dynamic |
| Cc | dynamic |
| ThreatClassification | string |
| RecipientDomain | string |
| EmailSize | int |
| IsFirstContact | bool |
| SourceSystem | string |
| Type | string |
