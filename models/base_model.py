"""Base classes for commodity risk forecasting models."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict

import pandas as pd


class BaseModel(ABC):
    """Minimal interface for forecasting models."""

    @abstractmethod
    def fit(self, data: pd.DataFrame) -> None:
        """Train the model on the given dataset."""

    @abstractmethod
    def predict(self, horizon: int) -> pd.Series:
        """Forecast future values for the provided horizon."""

    def serialize(self) -> Dict[str, Any]:
        """Return metadata describing the trained model."""
        return {"model": self.__class__.__name__}
