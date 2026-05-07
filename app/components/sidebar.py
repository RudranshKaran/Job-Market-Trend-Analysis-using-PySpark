from __future__ import annotations

import streamlit as st


def render_sidebar(pages: list[str]) -> str:
    """Render the app sidebar and return the selected page label."""
    st.sidebar.title("Job Market Trends")
    st.sidebar.caption("PySpark Analytics Dashboard")

    st.sidebar.markdown(
        """
        **Project:** Job Market Trend Analysis  
        **Phase:** Streamlit Visualization  
        **Dataset:** Data Science Job Salaries
        """
    )

    st.sidebar.divider()
    selection = st.sidebar.radio("Navigate", pages, index=0)

    st.sidebar.divider()
    st.sidebar.markdown("Run `streamlit run app/main.py` to launch the dashboard.")

    return selection
