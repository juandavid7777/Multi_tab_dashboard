import streamlit as st
import numpy as np
import pandas as pd

from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# @st.cache
def app():
    st.markdown("# On-Chain metrics")
    st.write("\n")
    
    # NUPL begining==============================================================================
    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    metric_api_name = "/v1/metrics/indicators/net_unrealized_profit_loss"
    metric_new_name = "NUPL"
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


    # NUPL chart =================================================
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    #Price candlesticks plots
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api["close"],
        mode = 'lines',
        name = '',
        line = dict(width = 0.5, color = "white")
        ),secondary_y=False)

    fig.add_trace(go.Candlestick(
        x=df_api['date'],
        open=df_api['open'],
        high=df_api['high'],
        low=df_api['low'],
        close=df_api['close'],
        name = coin_name + ' price'
        ),secondary_y=False)

    #Adds metric
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api[metric_new_name],
        mode = 'lines',
        name = metric_new_name,
        line = dict(width = 1.0, color = "cyan")
        ),secondary_y=True)

    #Defines figure properties
    fig.update_layout(
        title = metric_new_name + " metric - Sell > 0.75 : Buy < 0.25",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey', secondary_y = False)
    fig.update_yaxes(title = "NUPL value", showgrid=True, gridwidth=1, gridcolor='silver', secondary_y = True)

    st.plotly_chart(fig)

    # # NUPL END ===================================================================================
    # MVRV Z score chart =================================================
    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    metric_api_name = "/v1/metrics/market/mvrv_z_score"
    metric_new_name = "MVRV Z Score"
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


    # NUPL chart =================================================
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    #Price candlesticks plots
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api["close"],
        mode = 'lines',
        name = '',
        line = dict(width = 0.5, color = "white")
        ),secondary_y=False)

    fig.add_trace(go.Candlestick(
        x=df_api['date'],
        open=df_api['open'],
        high=df_api['high'],
        low=df_api['low'],
        close=df_api['close'],
        name = coin_name + ' price'
        ),secondary_y=False)

    #Adds metric
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api[metric_new_name],
        mode = 'lines',
        name = metric_new_name,
        line = dict(width = 1.0, color = "yellow")
        ),secondary_y=True)

    #Defines figure properties
    fig.update_layout(
        title = metric_new_name + " metric - Sell > 7: Buy < 0",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey', secondary_y = False)
    fig.update_yaxes(title = "MVRV Z score", showgrid=True, gridwidth=1, gridcolor='silver', secondary_y = True)

    st.plotly_chart(fig)

    # MVRV score end ===================================================================================
    # Thermocap Ratio =================================================
    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    metric_api_name = "/v1/metrics/mining/marketcap_thermocap_ratio"
    metric_new_name = "ThermoCap Ratio"
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


    # NUPL chart =================================================
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    #Price candlesticks plots
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api["close"],
        mode = 'lines',
        name = '',
        line = dict(width = 0.5, color = "white")
        ),secondary_y=False)

    fig.add_trace(go.Candlestick(
        x=df_api['date'],
        open=df_api['open'],
        high=df_api['high'],
        low=df_api['low'],
        close=df_api['close'],
        name = coin_name + ' price'
        ),secondary_y=False)

    #Adds metric
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api[metric_new_name],
        mode = 'lines',
        name = metric_new_name,
        line = dict(width = 1.0, color = "magenta")
        ),secondary_y=True)

    #Defines figure properties
    fig.update_layout(
        title = metric_new_name + " metric - Sell > 0.000004: Buy < 0.0000004",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey', secondary_y = False)
    fig.update_yaxes(title = "ThermoCap Ratio", showgrid=True, gridwidth=1, gridcolor='silver', secondary_y = True)

    st.plotly_chart(fig)

    # Thermocap ratio end ===================================================================================
    # Puel Multiple  ====================================================================================
    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    metric_api_name = "/v1/metrics/indicators/puell_multiple"
    metric_new_name = "Puell Multiple"
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

    # NUPL chart =================================================
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    #Price candlesticks plots
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api["close"],
        mode = 'lines',
        name = '',
        line = dict(width = 0.5, color = "white")
        ),secondary_y=False)

    fig.add_trace(go.Candlestick(
        x=df_api['date'],
        open=df_api['open'],
        high=df_api['high'],
        low=df_api['low'],
        close=df_api['close'],
        name = coin_name + ' price'
        ),secondary_y=False)

    #Adds metric
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api[metric_new_name],
        mode = 'lines',
        name = metric_new_name,
        line = dict(width = 1.0, color = "chartreuse")
        ),secondary_y=True)

    #Defines figure properties
    fig.update_layout(
        title = metric_new_name + " metric - Buy > 4: Sell < 0.5",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey', secondary_y = False)
    fig.update_yaxes(title = "Puell Multiple", showgrid=True, gridwidth=1, gridcolor='silver', secondary_y = True)

    st.plotly_chart(fig)    

        