"""Environment-driven configuration for the aisoc CLI."""
from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    workspace_id: str


def get_settings() -> Settings:
    """Read required settings from the environment (populated via .env)."""
    workspace_id = os.environ.get("AISOC_WORKSPACE_ID")
    if not workspace_id:
        raise RuntimeError(
            "AISOC_WORKSPACE_ID is not set. Copy .env.example to .env and fill in "
            "your Log Analytics workspace ID (see `az monitor log-analytics "
            "workspace list -o table`)."
        )
    return Settings(workspace_id=workspace_id)
