# Workspace schema references

This directory is the shared, workspace-specific schema source for all investigation skills.

- Validate `snapshot.json` against the SHA-256 of the current normalized `AISOC_WORKSPACE_ID` before using these files in a new environment.
- If the fingerprint differs, regenerate the catalog and table files for the current workspace before investigating.
- Start with `catalog.md` to locate a table.
- A table named `<TableName>` always maps to `<TableName>.md` in this directory; do not infer a domain subdirectory.
- Load only the table files required for the current investigation.
- Treat each file as a dated snapshot, not a permanent product contract.
- Do not run `getschema` during normal investigations when a current reference exists.
- Run live `getschema` only when a reference is missing, a query reports an unknown column, or a connector/schema change is known.
- After a live schema check, update the corresponding reference so the same discovery cost is not paid again.
- For `dynamic` columns, use a narrowly projected sample only when the internal JSON shape is required; `getschema` cannot describe that shape.