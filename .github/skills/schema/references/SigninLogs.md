# SigninLogs

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: SigninLogs | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User key is `UserPrincipalName`; risk fields include `RiskLevelAggregated`, `RiskState`, `RiskDetail`, and `IsRisky`.

| Column | Kusto type |
|---|---|
| TenantId | string |
| SourceSystem | string |
| TimeGenerated | datetime |
| ResourceId | string |
| OperationName | string |
| OperationVersion | string |
| Category | string |
| ResultType | string |
| ResultSignature | string |
| ResultDescription | string |
| DurationMs | long |
| CorrelationId | string |
| Resource | string |
| ResourceGroup | string |
| ResourceProvider | string |
| Identity | string |
| Level | string |
| Location | string |
| AlternateSignInName | string |
| AppDisplayName | string |
| AppId | string |
| AuthenticationContextClassReferences | string |
| AuthenticationDetails | string |
| AppliedEventListeners | dynamic |
| AuthenticationMethodsUsed | string |
| AuthenticationProcessingDetails | string |
| AuthenticationRequirement | string |
| AuthenticationRequirementPolicies | string |
| ClientAppUsed | string |
| ConditionalAccessPolicies | dynamic |
| ConditionalAccessStatus | string |
| CreatedDateTime | datetime |
| DeviceDetail | dynamic |
| IsInteractive | bool |
| Id | string |
| IPAddress | string |
| IsRisky | bool |
| LocationDetails | dynamic |
| MfaDetail | dynamic |
| NetworkLocationDetails | string |
| OriginalRequestId | string |
| ProcessingTimeInMilliseconds | string |
| RiskDetail | string |
| RiskEventTypes | string |
| RiskEventTypes_V2 | string |
| RiskLevelAggregated | string |
| RiskLevelDuringSignIn | string |
| RiskState | string |
| ResourceDisplayName | string |
| ResourceIdentity | string |
| ResourceServicePrincipalId | string |
| ServicePrincipalId | string |
| ServicePrincipalName | string |
| Status | dynamic |
| TokenIssuerName | string |
| TokenIssuerType | string |
| UserAgent | string |
| UserDisplayName | string |
| UserId | string |
| UserPrincipalName | string |
| AADTenantId | string |
| UserType | string |
| FlaggedForReview | bool |
| IPAddressFromResourceProvider | string |
| SignInIdentifier | string |
| SignInIdentifierType | string |
| ResourceTenantId | string |
| HomeTenantId | string |
| UniqueTokenIdentifier | string |
| SessionId | string |
| SessionLifetimePolicies | string |
| AutonomousSystemNumber | string |
| AuthenticationProtocol | string |
| CrossTenantAccessType | string |
| AuthenticationAppDeviceDetails | string |
| AuthenticationAppPolicyEvaluationDetails | string |
| ClientCredentialType | string |
| FederatedCredentialId | string |
| GlobalSecureAccessIpAddress | string |
| HomeTenantName | string |
| IncomingTokenType | string |
| IsTenantRestricted | bool |
| IsThroughGlobalSecureAccess | bool |
| OriginalTransferMethod | string |
| TokenProtectionStatusDetails | dynamic |
| AppOwnerTenantId | string |
| ResourceOwnerTenantId | string |
| Agent | dynamic |
| SourceAppClientId | string |
| ConditionalAccessAudiences | string |
| AuthenticatorAppLocation | string |
| ClientSessionId | string |
| RootActorID | string |
| AppliedConditionalAccessPolicies | string |
| RiskLevel | string |
| Type | string |
