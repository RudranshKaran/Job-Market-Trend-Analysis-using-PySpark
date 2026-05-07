from __future__ import annotations

import streamlit as st


def apply_theme() -> None:
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Archivo:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Archivo', sans-serif;
        color: #e2e8f0;
    }

    .stApp {
        background:
            radial-gradient(80rem 40rem at 20% -10%, rgba(13, 148, 136, 0.25) 0%, transparent 70%),
            radial-gradient(60rem 60rem at 90% 10%, rgba(234, 179, 8, 0.18) 0%, transparent 65%),
            linear-gradient(135deg, #0b1120 0%, #0f172a 55%, #0b0f1f 100%);
    }

    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc;
        letter-spacing: 0.01em;
    }

    p, li, span, label, .stMarkdown, .stText, .stCaption, .stAlert, .stSubheader {
        color: #cbd5e1;
    }

    .stMarkdown a {
        color: #5eead4;
    }

    .stDataFrame, .stTable {
        background-color: #0f172a;
        border-radius: 12px;
        border: 1px solid #1f2937;
    }

    div[data-testid="stImage"] img {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        box-shadow: 0 14px 30px rgba(2, 6, 23, 0.55);
        padding: 0.75rem;
    }

    div[data-testid="stImage"] {
        margin-top: 0.5rem;
    }

    hr {
        border-color: #1e293b;
    }

    [data-testid="stMetricValue"] {
        color: #f8fafc;
    }

    [data-testid="stMetricLabel"] {
        color: #94a3b8;
    }

    [data-testid="stSidebar"] {
        background: #0b1120;
        border-right: 1px solid #1f2937;
    }

    [data-testid="stSidebar"] a, [data-testid="stSidebar"] span {
        color: #cbd5e1;
    }

    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
        background: transparent;
        border-radius: 10px;
    }

    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
        background: rgba(148, 163, 184, 0.12);
    }

    .app-hero {
        background: linear-gradient(120deg, #0f172a 0%, #0b2f2a 60%, #122338 100%);
        color: #f8fafc;
        border-radius: 20px;
        padding: 1.6rem 1.8rem;
        box-shadow: 0 16px 40px rgba(2, 6, 23, 0.6);
        margin-bottom: 1.8rem;
        border: 1px solid rgba(148, 163, 184, 0.16);
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.1rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .hero-subtitle {
        color: #cbd5e1;
        font-size: 1rem;
        margin-bottom: 0.6rem;
    }

    .hero-pill {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        background: rgba(148, 163, 184, 0.22);
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-weight: 600;
    }

    .page-hero {
        display: grid;
        gap: 1.2rem;
        grid-template-columns: minmax(0, 1fr) auto;
        background: rgba(15, 23, 42, 0.92);
        border-radius: 20px;
        padding: 1.6rem 1.8rem;
        border: 1px solid rgba(148, 163, 184, 0.2);
        box-shadow: 0 16px 40px rgba(2, 6, 23, 0.6);
        margin-bottom: 1.6rem;
    }

    .page-hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
        color: #f8fafc;
    }

    .page-hero-subtitle {
        color: #cbd5e1;
        font-size: 1rem;
    }

    .page-meta {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
        margin-top: 0.9rem;
    }

    .page-chip {
        padding: 0.3rem 0.7rem;
        border-radius: 999px;
        background: rgba(148, 163, 184, 0.18);
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-weight: 600;
        color: #e2e8f0;
    }

    .page-kicker {
        font-size: 0.75rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #7dd3fc;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }

    .page-highlight {
        background: rgba(15, 118, 110, 0.18);
        border: 1px solid rgba(45, 212, 191, 0.4);
        color: #ccfbf1;
        padding: 0.4rem 0.8rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .section-card {
        background: #0f172a;
        border: 1px solid #1f2937;
        border-radius: 16px;
        padding: 1.2rem;
        box-shadow: 0 10px 24px rgba(2, 6, 23, 0.55);
    }

    .kpi-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 1rem 1.2rem;
        box-shadow: 0 10px 24px rgba(2, 6, 23, 0.55);
    }

    .kpi-label {
        color: #94a3b8;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }

    .kpi-value {
        color: #f8fafc;
        font-size: 1.6rem;
        font-weight: 700;
    }

    .kpi-sub {
        color: #94a3b8;
        font-size: 0.85rem;
        margin-top: 0.25rem;
    }

    .insight-list {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 16px;
        padding: 1rem 1.2rem;
        box-shadow: 0 10px 24px rgba(2, 6, 23, 0.55);
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
