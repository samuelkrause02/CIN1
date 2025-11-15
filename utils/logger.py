"""Simple logging utility for the dashboard."""

import logging
from typing import Optional

_LOGGER: Optional[logging.Logger] = None


def get_logger(name: str = "commodity-risk-dashboard") -> logging.Logger:
    """Return a module-level logger with a default configuration."""
    global _LOGGER
    if _LOGGER is None:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
        _LOGGER = logging.getLogger(name)
    return _LOGGER
