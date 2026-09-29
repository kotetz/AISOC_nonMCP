# DeviceFileCertificateInfo

- Snapshot: 2026-09-29
- Last observed in Usage (30d): 2026-09-29T10:00:00Z
- Observed by search (365d): True
- Source: DeviceFileCertificateInfo | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| CertificateSerialNumber | string |
| CrlDistributionPointUrls | string |
| DeviceId | string |
| DeviceName | string |
| IsRootSignerMicrosoft | bool |
| IsSigned | bool |
| IsTrusted | bool |
| Issuer | string |
| IssuerHash | string |
| MachineGroup | string |
| ReportId | long |
| SHA1 | string |
| SignatureType | string |
| Signer | string |
| SignerHash | string |
| Timestamp | datetime |
| TimeGenerated | datetime |
| CertificateCountersignatureTime | datetime |
| CertificateCreationTime | datetime |
| CertificateExpirationTime | datetime |
| SourceSystem | string |
| Type | string |
