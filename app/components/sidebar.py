from __future__ import annotations

import streamlit as st


def render_sidebar(pages: list[str]) -> str:
    """Render the app sidebar and return the selected page label."""
    st.sidebar.markdown("## Job Market Trends")
    st.sidebar.caption("PySpark Analytics")

    st.sidebar.divider()
    selection = st.sidebar.radio("Navigate", pages, index=0)

    return selection
