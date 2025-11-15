"""Training script stubs for commodity risk models."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from data.loaders import load_default_dataset
from models.base_model import BaseModel


def train_model(model: BaseModel, output_dir: Path) -> Path:
    """Train the provided model and save artifacts to disk."""
    dataset = load_default_dataset()
    model.fit(dataset)

    output_dir.mkdir(parents=True, exist_ok=True)
    artifact_path = output_dir / "model_metadata.json"
    pd.Series(model.serialize()).to_json(artifact_path)
    return artifact_path
