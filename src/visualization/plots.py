from __future__ import annotations

import pandas as pd
import plotly.express as px


def feature_importance_plot(
    dataframe: pd.DataFrame,
):

    fig = px.bar(
        dataframe,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Feature Importance",
    )

    fig.update_layout(
        height=600,
        yaxis=dict(
            autorange="reversed",
        ),
    )

    return fig


def leaderboard_plot(
    dataframe: pd.DataFrame,
):

    fig = px.bar(
        dataframe,
        x="Model",
        y="R2",
        color="Model",
        title="Model Comparison (R²)",
    )

    return fig


def forecast_plot(
    dataframe: pd.DataFrame,
):

    fig = px.line(
        dataframe,
        x="ds",
        y="yhat",
        title="Weather Forecast",
    )

    return fig