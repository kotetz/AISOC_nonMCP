# AADNonInteractiveUserSignInLogs

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: AADNonInteractiveUserSignInLogs | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes
- Investigation note: User key is `UserPrincipalName`. Unlike `SigninLogs`, this snapshot has no `RiskLevelAggregated`, `RiskState`, or `RiskDetail`; referencing them causes a semantic error.

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
| AADTenantId | string |
| Agent | string |
| AlternateSignInName | string |
| AppDisplayName | string |
| AppId | string |
| AppliedEventListeners | dynamic |
| AppOwnerTenantId | string |
| AuthenticationContextClassReferences | string |
| AuthenticationDetails | string |
| AuthenticationMethodsUsed | string |
| AuthenticationProcessingDetails | string |
| AuthenticationProtocol | string |
| AuthenticationRequirement | string |
| AuthenticationRequirementPolicies | string |
| AuthenticatorAppLocation | string |
| AutonomousSystemNumber | string |
| ClientAppUsed | string |
| ClientCredentialType | string |
| ClientSessionId | string |
| ConditionalAccessAudiences | string |
| ConditionalAccessPolicies | string |
| ConditionalAccessPoliciesV2 | dynamic |
| ConditionalAccessStatus | string |
| CreatedDateTime | datetime |
| CrossTenantAccessType | string |
| DeviceDetail | string |
| FederatedCredentialId | string |
| GlobalSecureAccessIpAddress | string |
| HomeTenantId | string |
| HomeTenantName | string |
| Id | string |
| IncomingTokenType | string |
| IPAddress | string |
| IsInteractive | bool |
| IsRisky | bool |
| IsTenantRestricted | bool |
| IsThroughGlobalSecureAccess | bool |
| LocationDetails | string |
| MfaDetail | string |
| NetworkLocationDetails | string |
| OriginalRequestId | string |
| OriginalTransferMethod | string |
| ProcessingTimeInMs | string |
| ResourceDisplayName | string |
| ResourceIdentity | string |
| ResourceOwnerTenantId | string |
| ResourceServicePrincipalId | string |
| ResourceTenantId | string |
| RootActorID | string |
| RiskDetail | string |
| RiskEventTypes | string |
| RiskEventTypes_V2 | string |
| RiskLevelAggregated | string |
| RiskLevelDuringSignIn | string |
| RiskState | string |
| ServicePrincipalId | string |
| SessionId | string |
| SessionLifetimePolicies | string |
| SignInEventTypes | string |
| SignInIdentifierType | string |
| TokenProtectionStatusDetails | string |
| Status | string |
| TokenIssuerName | string |
| TokenIssuerType | string |
| UniqueTokenIdentifier | string |
| UserAgent | string |
| UserDisplayName | string |
| UserId | string |
| UserPrincipalName | string |
| UserType | string |
| Type | string |
