"""Credential helper shared by all clients."""
from __future__ import annotations

from functools import lru_cache

from azure.identity import DefaultAzureCredential


@lru_cache(maxsize=1)
def get_credential() -> DefaultAzureCredential:
    """Return a cached DefaultAzureCredential bound to the signed-in `az login` session.

    If you need a different tenant or account, run `az login --tenant <tenant-id>`
    before using this tool; DefaultAzureCredential picks up the active `az` context.
    This tool never stores or requests secrets of its own.
    """
    return DefaultAzureCredential()
