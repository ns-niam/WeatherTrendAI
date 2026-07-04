import streamlit as st

from components.header import show_header
from components.metrics import show_metrics
from components.tables import show_leaderboard
from components.charts import show_model_chart
from components.footer import show_footer


st.set_page_config(
    page_title="WeatherTrendAI",
    page_icon="🌦",
    layout="wide",
)

st.markdown("""
<style>

.built-card{
position:fixed;
top:15px;
right:20px;
z-index:999;

background:#111827;

padding:15px 22px;

border-radius:14px;

border:1px solid rgba(255,255,255,.08);

box-shadow:0 8px 30px rgba(0,0,0,.35);

backdrop-filter:blur(10px);
}

.built-title{
font-size:15px;
color:#9CA3AF;
}

.built-name{
font-size:22px;
font-weight:700;
color:white;
margin-top:4px;
}

.built-role{
font-size:13px;
color:#60A5FA;
margin-top:2px;
}

</style>

<div class="built-card">

<div class="built-title">
✨ Built with
</div>

<div class="built-name">
Niam
</div>

<div class="built-role">
AI Engineer
</div>

</div>

""", unsafe_allow_html=True)

show_header()

show_metrics()

st.markdown(
"""
### About

WeatherTrendAI is an end-to-end machine learning platform for
weather prediction, model comparison, forecasting, and analytics.
"""
)

show_leaderboard()

show_model_chart()

show_footer()