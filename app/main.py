"""Streamlit entry point for the Commodity Risk Dashboard."""

import streamlit as st

from data.loaders import load_default_dataset


def main() -> None:
    """Render the dashboard landing page."""
    st.set_page_config(page_title="Commodity Risk Dashboard", layout="wide")

    st.title("Commodity Risk Dashboard")
    st.write(
        """This dashboard provides insight into commodity price trends and risk metrics.
        Use the sidebar to navigate between analytics pages."""
    )

    dataset = load_default_dataset()
    st.write("Loaded dataset", dataset.head())


if __name__ == "__main__":
    main()
