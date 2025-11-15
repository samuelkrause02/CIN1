"""Plotting utilities for the dashboard."""

from __future__ import annotations

from typing import Iterable

import plotly.express as px
import pandas as pd


def line_chart(data: pd.DataFrame, x: str, y: Iterable[str]) -> px.line:
    """Return a simple Plotly line chart."""
    return px.line(data, x=x, y=list(y), title="Commodity Price Trends")
