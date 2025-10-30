"""Tests for data loading helpers."""

from __future__ import annotations

import pandas as pd

from data.loaders import load_default_dataset


def test_load_default_dataset_returns_dataframe() -> None:
    dataset = load_default_dataset()
    assert isinstance(dataset, pd.DataFrame)
    assert {"commodity", "price_usd", "volatility"}.issubset(dataset.columns)
