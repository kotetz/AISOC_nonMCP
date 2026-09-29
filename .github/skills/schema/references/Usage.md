# Usage

- Snapshot: 2026-09-29
- Observed by search (365d): True
- Source: Usage | getschema
- Authority: workspace snapshot; refresh on schema errors or connector changes

| Column | Kusto type |
|---|---|
| TenantId | string |
| Computer | string |
| TimeGenerated | datetime |
| Plan | string |
| SourceSystem | string |
| StartTime | datetime |
| EndTime | datetime |
| ResourceUri | string |
| LinkedResourceUri | string |
| DataType | string |
| Solution | string |
| BatchesWithinSla | long |
| BatchesOutsideSla | long |
| BatchesCapped | long |
| TotalBatches | long |
| AvgLatencyInSeconds | real |
| Quantity | real |
| QuantityUnit | string |
| IsBillable | bool |
| MeterId | string |
| LinkedMeterId | string |
| Type | string |
