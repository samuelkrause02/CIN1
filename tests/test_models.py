"""Unit tests for model utilities."""

from __future__ import annotations

import pandas as pd

from models.base_model import BaseModel


class DummyModel(BaseModel):
    """Minimal model for tests."""

    def __init__(self) -> None:
        self._fitted = False

    def fit(self, data: pd.DataFrame) -> None:  # type: ignore[override]
        self._fitted = not data.empty

    def predict(self, horizon: int) -> pd.Series:  # type: ignore[override]
        if not self._fitted:
            raise RuntimeError("Model must be fitted before calling predict().")
        return pd.Series([1.0] * horizon)


def test_model_serialization() -> None:
    model = DummyModel()
    model.fit(pd.DataFrame({"value": [1, 2, 3]}))
    assert model.serialize()["model"] == "DummyModel"
