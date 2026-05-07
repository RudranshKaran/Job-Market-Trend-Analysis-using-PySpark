from __future__ import annotations

import streamlit as st


def render_page_header(
    title: str,
    subtitle: str,
    tag: str | None = None,
    meta: list[str] | None = None,
) -> None:
    """Render a consistent hero header across pages."""
    meta = meta or []
    meta_html = "".join([f"<span class=\"page-chip\">{item}</span>" for item in meta])
    tag_html = f"<span class=\"page-highlight\">{tag}</span>" if tag else ""
    st.markdown(
        f"""
        <div class="page-hero">
            <div>
                <div class="page-kicker">Job Market Trends</div>
                <div class="page-hero-title">{title}</div>
                <div class="page-hero-subtitle">{subtitle}</div>
                <div class="page-meta">{meta_html}</div>
            </div>
            <div>{tag_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
