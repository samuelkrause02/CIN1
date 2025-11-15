"""Utilities for loading and preprocessing commodity data."""

from __future__ import annotations

from pathlib import Path
from typing import Final

import pandas as pd

_DATA_DIR: Final[Path] = Path(__file__).resolve().parent


def load_default_dataset() -> pd.DataFrame:
    """Return a placeholder dataset for local development."""
    csv_path = _DATA_DIR / "processed" / "default_dataset.csv"
    if csv_path.exists():
        return pd.read_csv(csv_path)

    return pd.DataFrame(
        {
            "commodity": ["Crude Oil", "Natural Gas", "Gold"],
            "price_usd": [72.4, 3.1, 1930.5],
            "volatility": [0.21, 0.35, 0.12],
        }
    )
