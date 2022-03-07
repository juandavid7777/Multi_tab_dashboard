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

    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")
    df_metrics24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/metrics24.csv")

    #Selects metrics
    df_api = df_api24[[ "Unnamed: 0",
                        "/v1/metrics/market/price_usd_ohlc-o",
                        "/v1/metrics/market/price_usd_ohlc-h",
                        "/v1/metrics/market/price_usd_ohlc-c",
                        "/v1/metrics/market/price_usd_ohlc-l",
                        ]]

    df_metrics = df_metrics24[[ "Date",
                        'price_reg',
                        'plus_3STDV',
                        'minus_3STDV',
                        'plus_2STDV',
                        'minus_2STDV',
                        'plus_1STDV',
                        'minus_1STDV',
                        ]]
    
    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "/v1/metrics/market/price_usd_ohlc-o":"open",
                        "/v1/metrics/market/price_usd_ohlc-h":"high",
                        "/v1/metrics/market/price_usd_ohlc-c":"close",
                        "/v1/metrics/market/price_usd_ohlc-l":"low",
                        })

    df_metrics = df_metrics24.rename(columns={"Date":"date"})

    #2.-----API token definition
    coin_name = "BTC"
    projected_days = 180

    #3.-----Plots figures Uncertainity bands=======================================
    #==== Basic candel stick chart =================================================
    fig = go.Figure()

    #Price candlesticks plots
    fig.add_trace(go.Scatter(
        x=df_api['date'],
        y=df_api["close"],
        mode = 'lines',
        name = '',
        line = dict(width = 0.5, color = "white")
        ))

    fig.add_trace(go.Candlestick(
        x=df_api['date'],
        open=df_api['open'],
        high=df_api['high'],
        low=df_api['low'],
        close=df_api['close'],
        name = coin_name + ' price'
        ))

    #Prices for uncertainity bands
    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["plus_3STDV"],
        mode = 'lines',
        name = '99.9%',
        line = dict(width = 0.5, dash = 'dash', color = "red"),
        ))

    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["plus_2STDV"],
        mode = 'lines',
        name = '97.8%',
        line = dict(width = 0.5, dash = 'dash', color = "yellow"),
        fill='tonexty',
        fillcolor='rgba(245, 66, 66,0.2)'  #Red
        ))

    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["plus_1STDV"],
        mode = 'lines',
        name = '84.2%',
        line = dict(width = 0.5, dash = 'dash', color = "green"),\
        fill='tonexty',
        fillcolor='rgba(245, 230, 66,0.2)'  #yellow
        ))

    #Prices regression plot
    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["price_reg"],
        mode = 'lines',
        name = '50.0%',
        line = dict(width = 1.0, dash = 'dash', color = "grey"),
        fill='tonexty',
        fillcolor='rgba(0, 199, 56,0.2)'  #green
        ))

    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["minus_1STDV"],
        mode = 'lines',
        name = '15.8%',
        line = dict(width = 0.5, dash = 'dash', color = "green"),
        fill='tonexty',
        fillcolor='rgba(0, 199, 56,0.2)'  #green
        ))

    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["minus_2STDV"],
        mode = 'lines',
        name = '2.2%',
        line = dict(width = 0.5, dash = 'dash', color = "yellow"),
        fill='tonexty',
        fillcolor='rgba(245, 230, 66,0.2)'  #Yellow
        ))

    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["minus_3STDV"],
        mode = 'lines',
        name = '0.1%',
        line = dict(width = 0.5, dash = 'dash', color = "red"),
        fill='tonexty',
        fillcolor='rgba(245, 66, 66,0.2)'  #Red
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

    # Uncertainity bands plot finished ===================================================
    #4=== Colored chart risk metric reg ==================================================

    fig = go.Figure()

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["close"],
        mode = 'markers',
        name = '',
        marker=dict(size=3,color = df_metrics["norm_dist"], colorscale='Jet',showscale=True)
        ),secondary_y=False)

    #Defines figure properties
    fig.update_layout(
        title = coin_name + " time uncertainity metric",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    st.plotly_chart(fig)

    # End of colored chart risk metric reg ==============================================
    #5=== Colored chart MA risk metric ==================================================

    fig = go.Figure()

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["close"],
        mode = 'markers',
        name = '',
        marker=dict(size=3,color = df_metrics["risk_MA_norm"], colorscale='Jet',showscale=True)
        ),secondary_y=False)

    #Defines figure properties
    fig.update_layout(
        title = coin_name + " MA uncertainity metric",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey')

    st.plotly_chart(fig)

    # End of colored chart MA risk metric ==============================================
    # Combined Basic candel stick chart =================================================
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    #Price candlesticks plots
    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["close"],
        mode = 'lines',
        name = '',
        line = dict(width = 0.5, color = "white")
        ),secondary_y=False)

    fig.add_trace(go.Candlestick(
        x=df_metrics['date'],
        open=df_metrics['open'],
        high=df_metrics['high'],
        low=df_metrics['low'],
        close=df_metrics['close'],
        name = coin_name + ' price'
        ),secondary_y=False)

    #Adds metric
    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["norm_dist"],
        mode = 'lines',
        name = "Time uncertainity downside risk",
        line = dict(width = 1.0, color = "chartreuse")
        ),secondary_y=True)

    #Adds metric
    fig.add_trace(go.Scatter(
        x=df_metrics['date'],
        y=df_metrics["risk_MA_norm"],
        mode = 'lines',
        name = "MA uncertainity downside risk",
        line = dict(width = 1.0, color = "cyan")
        ),secondary_y=True)

    #Defines figure properties
    fig.update_layout(
        title = "Combined downside risk metrics",
        xaxis_title= "Date",
        yaxis_title= coin_name + " price (USD)",
        
        plot_bgcolor = "black",
        yaxis_type="log",
        xaxis_rangeslider_visible=False)

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='grey', secondary_y = False)
    fig.update_yaxes(title = "Risk metric (0 - 1)", showgrid=True, gridwidth=1, gridcolor='silver', secondary_y = True)

    st.plotly_chart(fig)

    # # combined END ===================================================================================