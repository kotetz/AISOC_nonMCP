# AWSCloudTrail

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AWSCloudTrail | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User keys are `UserIdentityUserName`/`SessionIssuerUserName`; use `UserIdentityArn`/`SessionIssuerArn` when the name is embedded in an ARN.

| Column | Kusto type |
|---|---|
| TimeGenerated | datetime |
| AwsEventId | string |
| EventVersion | string |
| EventSource | string |
| EventTypeName | string |
| EventName | string |
| UserIdentityType | string |
| UserIdentityPrincipalid | string |
| UserIdentityArn | string |
| UserIdentityAccountId | string |
| UserIdentityInvokedBy | string |
| UserIdentityAccessKeyId | string |
| UserIdentityUserName | string |
| SessionMfaAuthenticated | bool |
| SessionCreationDate | datetime |
| SessionIssuerType | string |
| SessionIssuerPrincipalId | string |
| SessionIssuerArn | string |
| SessionIssuerAccountId | string |
| SessionIssuerUserName | string |
| AWSRegion | string |
| SourceIpAddress | string |
| UserAgent | string |
| ErrorCode | string |
| ErrorMessage | string |
| RequestParameters | string |
| ResponseElements | string |
| AdditionalEventData | string |
| AwsRequestId | string |
| AwsRequestId_ | string |
| Resources | string |
| APIVersion | string |
| ReadOnly | bool |
| RecipientAccountId | string |
| ServiceEventDetails | string |
| SharedEventId | string |
| VpcEndpointId | string |
| ManagementEvent | bool |
| TenantId | string |
| SourceSystem | string |
| OperationName | string |
| Category | string |
| EC2RoleDelivery | string |
| TlsVersion | string |
| CipherSuite | string |
| ClientProvidedHostHeader | string |
| IpProtocol | string |
| SourcePort | string |
| DestinationPort | string |
| CidrIp | string |
| UserIdentityUserId | string |
| UserIdentityStoreArn | string |
| IPAddress_CF | string |
| SubnetMask_CF | int |
| Type | string |
