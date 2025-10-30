"""Configuration helpers for the dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    """Application level configuration."""

    data_dir: Path
    model_dir: Path


def load_config(base_path: Path | None = None) -> AppConfig:
    """Construct an :class:`AppConfig` with sensible defaults."""
    base = base_path or Path.cwd()
    return AppConfig(data_dir=base / "data", model_dir=base / "artifacts")
