from __future__ import annotations

import streamlit as st


def render_metric_cards(metrics: list[dict]) -> None:
    """Render KPI metric cards in a single row."""
    if not metrics:
        st.info("No metrics available to display.")
        return

    cols = st.columns(len(metrics))
    for col, item in zip(cols, metrics, strict=False):
        label = item.get("label", "Metric")
        value = item.get("value", "-")
        subtitle = item.get("subtitle", "")
        with col:
            st.markdown(
                f"""
                <div class="kpi-card">
                    <div class="kpi-label">{label}</div>
                    <div class="kpi-value">{value}</div>
                    <div class="kpi-sub">{subtitle}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
