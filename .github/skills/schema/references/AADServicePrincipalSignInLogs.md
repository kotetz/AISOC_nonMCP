# AADServicePrincipalSignInLogs

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AADServicePrincipalSignInLogs | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| SourceSystem | string |
| TimeGenerated | datetime |
| OperationName | string |
| OperationVersion | string |
| Category | string |
| ResultType | string |
| ResultSignature | string |
| ResultDescription | string |
| DurationMs | long |
| CorrelationId | string |
| ResourceGroup | string |
| Identity | string |
| Level | string |
| Location | string |
| AppId | string |
| AppOwnerTenantId | string |
| AuthenticationContextClassReferences | string |
| AutonomousSystemNumber | string |
| AuthenticationProcessingDetails | string |
| ClientCredentialType | string |
| ConditionalAccessAudiences | string |
| ConditionalAccessPolicies | string |
| ConditionalAccessPoliciesV2 | dynamic |
| ConditionalAccessStatus | string |
| CreatedDateTime | datetime |
| FederatedCredentialId | string |
| Id | string |
| IPAddress | string |
| LocationDetails | string |
| NetworkLocationDetails | string |
| ResourceDisplayName | string |
| ResourceIdentity | string |
| ResourceOwnerTenantId | string |
| ResourceServicePrincipalId | string |
| ServicePrincipalCredentialKeyId | string |
| ServicePrincipalCredentialThumbprint | string |
| ServicePrincipalId | string |
| ServicePrincipalName | string |
| SessionId | string |
| UniqueTokenIdentifier | string |
| Agent | string |
| UserAgent | string |
| AADTenantId | string |
| Type | string |
