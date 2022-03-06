import streamlit as st
import numpy as np
import pandas as pd

from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# @st.cache
def app():
    st.markdown("# Technical Metrics")
    st.write("\n")
    # Summarizes some metrics

    #1.-----Downloads data
    df = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/BTC_risk_metric/891a1032cb63160763c33f235a4714f2083c9713/BTC_price_projections.csv")


    #2.-----API token definition
    coin_name = "BTC"
    projected_days = 180

    #3.-----Plots figures

    #=================================================== BANDS CHART===========================================
    fig = go.Figure()

    #Price candlesticks plots
    fig.add_trace(go.Scatter(
        x=df['Date'],
        y=df["close"],
        mode = 'lines',
        name = '',
        line = dict(width = 0.5, color = "white")
        ))

    fig.add_trace(go.Candlestick(
        x=df['Date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close'],
        name = coin_name + ' price'
        ))

    #Defines figure properties
    fig.update_layout(
        title = coin_name + " uncertainity bands",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        legend_title="Uncertainity risk levels",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    st.plotly_chart(fig, use_container_width = True)