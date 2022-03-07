import streamlit as st
import numpy as np
import pandas as pd


# @st.cache
def app():
    st.markdown("# HOME")

    st.markdown("## BTC price latest summary")
    #Price summary
    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    #Selects metrics
    df_api = df_api24[[ "Unnamed: 0",
                        "/v1/metrics/market/price_usd_ohlc-o",
                        "/v1/metrics/market/price_usd_ohlc-h",
                        "/v1/metrics/market/price_usd_ohlc-c",
                        "/v1/metrics/market/price_usd_ohlc-l"]]

    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "/v1/metrics/market/price_usd_ohlc-o":"open",
                        "/v1/metrics/market/price_usd_ohlc-h":"high",
                        "/v1/metrics/market/price_usd_ohlc-c":"close",
                        "/v1/metrics/market/price_usd_ohlc-l":"low"})

    st.table(df_api.set_index("date").iloc[-2:-1].tail(1))


    
    # Summarizes some metrics
    st.markdown("## Metrics latest summary")
    st.write("\n")
    st.markdown("Technical summary")
    # Technical summary ====================================================================================================================================
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
                        'close',
                        'price_reg',
                        'plus_3STDV',
                        'minus_3STDV',
                        'plus_2STDV',
                        'minus_2STDV',
                        'plus_1STDV',
                        'minus_1STDV',
                        "norm_dist",
                        "risk_MA_norm"
                        ]]
    
    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "/v1/metrics/market/price_usd_ohlc-o":"open",
                        "/v1/metrics/market/price_usd_ohlc-h":"high",
                        "/v1/metrics/market/price_usd_ohlc-c":"close",
                        "/v1/metrics/market/price_usd_ohlc-l":"low",
                        })

    df_metrics = df_metrics.rename(columns={"Date":"date"})


    st.table(df_metrics.set_index("date").iloc[-2])

    # End of technical summary =============================================================================================================================
    #On chain summary ======================================================================================================================================= 
    st.markdown("Onchain summary")

    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    metric_api_name = "/v1/metrics/indicators/puell_multiple"
    metric_new_name = "Puell Multiple"
    coin_name = "BTC"

    #Selects metrics
    df_api = df_api24[[ "Unnamed: 0",
                        "/v1/metrics/market/mvrv_z_score",
                        "/v1/metrics/mining/marketcap_thermocap_ratio",
                        "/v1/metrics/indicators/net_unrealized_profit_loss",
                        "/v1/metrics/indicators/puell_multiple"]]

    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "/v1/metrics/market/mvrv_z_score":"MVRV Z Score",
                        "/v1/metrics/mining/marketcap_thermocap_ratio":"Thermocap Ratio",
                        "/v1/metrics/indicators/net_unrealized_profit_loss":"Net Unrealized Profit/Loss (NUPL)",
                        "/v1/metrics/indicators/puell_multiple":"Puell Multiple"})

    st.table(df_api.set_index("date").iloc[-2])

    #On chain summary end ======================================================================================================================================= 
    #Sentiment summary ======================================================================================================================================= 
    st.markdown("Sentiment summary")  
 
    #1.-----Downloads data and cleans it
    df_api24 = pd.read_csv("https://raw.githubusercontent.com/juandavid7777/Multi_tab_dashboard/main/data/api_24h.csv?token=GHSAT0AAAAAABSGJ422NL7BZDYFQTJXHFPCYRENPLQ")

    metric_api_name = "/v1/metrics/indicators/puell_multiple"
    metric_new_name = "Puell Multiple"
    coin_name = "BTC"

    #Selects metrics
    df_api = df_api24[[ "Unnamed: 0",
                        "fear_and_greed-value"]]

    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "fear_and_greed-value": "Fear and Greed"})

    st.table(df_api.set_index("date").iloc[-2])

    #Sentiment summary end ======================================================================================================================================= 


    
    
    
    


    