# Commodity Risk Dashboard

A prototype layout for a multi-layer analytics project that surfaces commodity price
signals, forecasts, and risk insights.

## Project Structure

```
app/                         # Web Layer / UI
├── main.py                  # Streamlit entry point
├── pages/                   # Multi-page views
├── components/              # Reusable UI components
└── assets/                  # Static assets (logos, css, js)

data/                        # Data handling
├── raw/                     # Input raw data (not versioned)
├── processed/               # Cleaned datasets
└── loaders.py               # Data loading + preprocessing functions

models/                      # Modeling / Forecasting
├── train.py                 # Training scripts
├── evaluate.py              # Evaluation & metrics
└── base_model.py            # Abstract model class

utils/                       # Helper functions (logging, config, plotting)
├── logger.py
├── config.py
└── plotting.py

notebooks/                   # Exploratory analyses (Jupyter)
├── 01_data_exploration.ipynb
└── 02_model_testing.ipynb

tests/                       # Unit tests
├── test_models.py
└── test_loaders.py
```

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the Streamlit application with `streamlit run app/main.py`.

## Testing

Execute the unit tests with `pytest`.
