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
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")
    df_api = df_api24[[df_api[[/v1/metrics/market/price_usd_ohlc-o,
                    /v1/metrics/market/price_usd_ohlc-h,
                    /v1/metrics/market/price_usd_ohlc-c,
                    /v1/metrics/market/price_usd_ohlc-l,
                    fear_and_greed-value]]]]

    #2.-----API token definition
    coin_name = "BTC"
    projected_days = 180

    st.table(df_api)

    #3.-----Plots figures

    # ==== Basic candel stick chart =================================================
    # fig = go.Figure()

    # #Price candlesticks plots
    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["close"],
    #     mode = 'lines',
    #     name = '',
    #     line = dict(width = 0.5, color = "white")
    #     ))

    # fig.add_trace(go.Candlestick(
    #     x=df['Date'],
    #     open=df['open'],
    #     high=df['high'],
    #     low=df['low'],
    #     close=df['close'],
    #     name = coin_name + ' price'
    #     ))

    # #Prices for uncertainity bands
    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["plus_3STDV"],
    #     mode = 'lines',
    #     name = '99.9%',
    #     line = dict(width = 0.5, dash = 'dash', color = "red"),
    #     ))

    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["plus_2STDV"],
    #     mode = 'lines',
    #     name = '97.8%',
    #     line = dict(width = 0.5, dash = 'dash', color = "yellow"),
    #     fill='tonexty',
    #     fillcolor='rgba(245, 66, 66,0.2)'  #Red
    #     ))

    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["plus_1STDV"],
    #     mode = 'lines',
    #     name = '84.2%',
    #     line = dict(width = 0.5, dash = 'dash', color = "green"),\
    #     fill='tonexty',
    #     fillcolor='rgba(245, 230, 66,0.2)'  #yellow
    #     ))

    # #Prices regression plot
    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["price_reg"],
    #     mode = 'lines',
    #     name = '50.0%',
    #     line = dict(width = 1.0, dash = 'dash', color = "grey"),
    #     fill='tonexty',
    #     fillcolor='rgba(0, 199, 56,0.2)'  #green
    #     ))

    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["minus_1STDV"],
    #     mode = 'lines',
    #     name = '15.8%',
    #     line = dict(width = 0.5, dash = 'dash', color = "green"),
    #     fill='tonexty',
    #     fillcolor='rgba(0, 199, 56,0.2)'  #green
    #     ))

    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["minus_2STDV"],
    #     mode = 'lines',
    #     name = '2.2%',
    #     line = dict(width = 0.5, dash = 'dash', color = "yellow"),
    #     fill='tonexty',
    #     fillcolor='rgba(245, 230, 66,0.2)'  #Yellow
    #     ))

    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["minus_3STDV"],
    #     mode = 'lines',
    #     name = '0.1%',
    #     line = dict(width = 0.5, dash = 'dash', color = "red"),
    #     fill='tonexty',
    #     fillcolor='rgba(245, 66, 66,0.2)'  #Red
    #     ))

    # #Defines figure properties
    # fig.update_layout(
    #     title = coin_name + " uncertainity bands",
    #     xaxis_title= "Date",
    #     yaxis_title= coin_name + " price (USD)",
    #     legend_title="Uncertainity risk levels",
        
    #     plot_bgcolor = "black",
    #     yaxis_type="log",
    #     xaxis_rangeslider_visible=False)

    # fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    # fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    # st.plotly_chart(fig, use_container_width = True)

    # #=== Colored chart ========================================

    # fig = go.Figure()

    # # Create figure with secondary y-axis
    # fig = make_subplots(specs=[[{"secondary_y": True}]])

    # fig.add_trace(go.Scatter(
    #     x=df['Date'],
    #     y=df["close"],
    #     mode = 'markers',
    #     name = '',
    #     marker=dict(size=3,color = df["norm_dist"], colorscale='Jet',showscale=True)
    #     ),secondary_y=False)

    # #Defines figure properties
    # fig.update_layout(
    #     title = coin_name + " uncertainity colored metric",
    #     xaxis_title= "Date",
    #     yaxis_title= coin_name + " price (USD)",
        
    #     plot_bgcolor = "black",
    #     yaxis_type="log",
    #     xaxis_rangeslider_visible=False)

    # fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    # fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    # st.plotly_chart(fig)