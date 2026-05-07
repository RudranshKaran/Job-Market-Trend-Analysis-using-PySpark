from __future__ import annotations

from typing import Iterable

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


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
    sns.barplot(data=data, x=x, y=y, ax=ax, palette="crest")
    ax.set_title(title)
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    ax.tick_params(axis="x", rotation=rotation)
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
    ax.pie(data[values], labels=data[labels], autopct="%1.0f%%", startangle=90)
    ax.set_title(title)
    ax.axis("equal")
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
    sns.histplot(data[column], bins=bins, kde=True, ax=ax, color="#0ea5a4")
    ax.set_title(title)
    ax.set_xlabel(xlabel or column)
    ax.set_ylabel(ylabel or "Count")
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
    sns.lineplot(data=data, x=x, y=y, marker="o", ax=ax, color="#0f766e")
    ax.set_title(title)
    ax.set_xlabel(xlabel or x)
    ax.set_ylabel(ylabel or y)
    fig.tight_layout()
    return fig
