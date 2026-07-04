import streamlit as st


def show_metrics():

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "Accuracy",
        "95.83%",
        "Best Performance"
    )

    c2.metric(
        "Best Model",
        "Random Forest"
    )

    c3.metric(
        "Dataset",
        "151,047"
    )

    c4.metric(
        "API",
        "Healthy",
        "Running"
    )