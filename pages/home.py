import streamlit as st
import numpy as np
import pandas as pd


# @st.cache
def app():
    st.markdown("## HOME")
    st.write("\n")
    # Summarizes some metrics
    st.markdown("# Metrics latest summary")
    st.write("\n")
    st.markdown("Technical summary")

    #On chain summary ======================================================================================================================================= 
    st.markdown("Onchain summary")

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
                        "/v1/metrics/market/mvrv_z_score",
                        "/v1/metrics/mining/marketcap_thermocap_ratio",
                        "/v1/metrics/indicators/net_unrealized_profit_loss",
                        "fear_and_greed-value"]]

    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "/v1/metrics/market/price_usd_ohlc-o":"open",
                        "/v1/metrics/market/price_usd_ohlc-h":"high",
                        "/v1/metrics/market/price_usd_ohlc-c":"close",
                        "/v1/metrics/market/price_usd_ohlc-l":"low",
                        "/v1/metrics/market/mvrv_z_score":"MVRVZ",
                        "/v1/metrics/mining/marketcap_thermocap_ratio":"thermocap_rat",
                        "/v1/metrics/indicators/net_unrealized_profit_loss":"NUPL",
                        "fear_and_greed-value": "fg_val"})

    st.table(df_api.iloc[-1])

    #On chain summary end ======================================================================================================================================= 



    st.markdown("Sentiment summary")  
 


    
    
    
    


    