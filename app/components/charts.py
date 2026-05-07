from __future__ import annotations

from typing import Iterable

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(
    style="darkgrid",
    rc={
        "axes.facecolor": "#0f172a",
        "figure.facecolor": "#0f172a",
        "grid.color": "#1f2937",
        "text.color": "#e2e8f0",
        "axes.labelcolor": "#cbd5e1",
        "xtick.color": "#94a3b8",
        "ytick.color": "#94a3b8",
        "axes.edgecolor": "#334155",
    },
)


def bar_chart(
    data,
    x: str,
    y: str,
    title: str,
    xlabel: str | None = None,
    ylabel: str | None = None,
    rotation: int = 0,
    figsize: tuple[int, int] = (8, 4),
):
    if data is None or data.empty:
        return None

    fig, ax = plt.subplots(figsize=figsize)
    sns.barplot(data=data, x=x, y=y, hue=x, ax=ax, palette="crest", legend=False)
    ax.set_title(title, color="#e2e8f0")
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    ax.tick_params(axis="x", rotation=rotation)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")
    fig.tight_layout()
    return fig


def pie_chart(
    data,
    labels: str,
    values: str,
    title: str,
    figsize: tuple[int, int] = (6, 6),
):
    if data is None or data.empty:
        return None

    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(
        data[values],
        labels=data[labels],
        autopct="%1.0f%%",
        startangle=90,
        textprops={"color": "#e2e8f0"},
    )
    ax.set_title(title, color="#e2e8f0")
    ax.axis("equal")
    fig.patch.set_facecolor("#0f172a")
    return fig


def histogram(
    data,
    column: str,
    title: str,
    bins: int = 30,
    xlabel: str | None = None,
    ylabel: str | None = None,
    figsize: tuple[int, int] = (8, 4),
):
    if data is None or data.empty:
        return None

    fig, ax = plt.subplots(figsize=figsize)
    sns.histplot(data[column], bins=bins, kde=True, ax=ax, color="#14b8a6")
    ax.set_title(title, color="#e2e8f0")
    ax.set_xlabel(xlabel or column)
    ax.set_ylabel(ylabel or "Count")
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")
    fig.tight_layout()
    return fig


def line_chart(
    data,
    x: str,
    y: str,
    title: str,
    xlabel: str | None = None,
    ylabel: str | None = None,
    figsize: tuple[int, int] = (8, 4),
):
    if data is None or data.empty:
        return None

    fig, ax = plt.subplots(figsize=figsize)
    sns.lineplot(data=data, x=x, y=y, marker="o", ax=ax, color="#22d3ee")
    ax.set_title(title, color="#e2e8f0")
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#0f172a")
    fig.tight_layout()
    return fig
