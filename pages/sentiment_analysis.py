import streamlit as st
import numpy as np
import pandas as pd

from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# @st.cache
def app():
    st.markdown("# Sentiment Metrics")
    st.write("\n")
    
    #=== Fear and Greed ========================================
    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    metric_api_name = "fear_and_greed-value"
    metric_new_name = "Fear and Greed Index"
    coin_name = "BTC"

    #Selects metrics
    df_api = df_api24[[ "Unnamed: 0",
                        "/v1/metrics/market/price_usd_ohlc-o",
                        "/v1/metrics/market/price_usd_ohlc-h",
                        "/v1/metrics/market/price_usd_ohlc-c",
                        "/v1/metrics/market/price_usd_ohlc-l",
                        metric_api_name]]

    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "/v1/metrics/market/price_usd_ohlc-o":"open",
                        "/v1/metrics/market/price_usd_ohlc-h":"high",
                        "/v1/metrics/market/price_usd_ohlc-c":"close",
                        "/v1/metrics/market/price_usd_ohlc-l":"low",
                        metric_api_name:metric_new_name})
    
    
    fig = go.Figure()

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=df_api['Date'],
        y=df_api["close"],
        mode = 'markers',
        name = '',
        marker=dict(size=3,color = df_api[metric_new_name], colorscale='Jet',showscale=True)
        ),secondary_y=False)

    #Defines figure properties
    fig.update_layout(
        title = coin_name + " Fear and Greed Index",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    st.plotly_chart(fig)