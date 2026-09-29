"""Thin, read-only API client for Microsoft Sentinel / Log Analytics investigations.

Everything in this package goes through the Azure Monitor Log Analytics Query
API (see clients.logs.run_kql). There is no write path: this tool is for
investigation only.
"""

__version__ = "0.1.0"
