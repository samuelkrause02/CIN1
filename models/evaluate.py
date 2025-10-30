"""Evaluation utilities for trained commodity risk models."""

from __future__ import annotations

from typing import Dict

import numpy as np
import pandas as pd

from models.base_model import BaseModel


def calculate_metrics(model: BaseModel, actuals: pd.Series, horizon: int) -> Dict[str, float]:
    """Return simple error metrics for the model forecast."""
    predictions = model.predict(horizon)
    predictions = predictions.reindex(actuals.index).fillna(method="ffill")

    errors = actuals - predictions
    return {
        "mae": float(np.abs(errors).mean()),
        "mse": float(np.square(errors).mean()),
    }
