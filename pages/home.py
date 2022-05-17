import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from functions import add_metricBar

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
                        "close",
                        "norm_dist",
                        "risk_MA_norm",
                        'plus_3STDV',
                        'plus_2STDV',
                        'plus_1STDV',
                        'price_reg',
                        'minus_1STDV',
                        'minus_2STDV',
                        'minus_3STDV'                        
                        ]]
    
    #Renames the metrics
    df_api = df_api.rename(columns={"Unnamed: 0":"date",
                        "/v1/metrics/market/price_usd_ohlc-o":"open",
                        "/v1/metrics/market/price_usd_ohlc-h":"high",
                        "/v1/metrics/market/price_usd_ohlc-c":"close",
                        "/v1/metrics/market/price_usd_ohlc-l":"low",
                        })

    df_metrics = df_metrics.rename(columns={"Date":"date",
                                            "norm_dist":"Time uncertainity risk",
                                            "risk_MA_norm":"MA uncertainity risk",
                                            'plus_3STDV':"99.9% risk price",
                                            'plus_2STDV':"97.8% risk price",
                                            'plus_1STDV':"84.2% risk price",
                                            'price_reg': "50.0% risk price",
                                            'minus_1STDV': "15.8% risk price",
                                            'minus_2STDV': "2.2% risk price",
                                            'minus_3STDV': "0.1% risk price"
                                            })


    st.table(df_metrics.set_index("date").iloc[df_metrics["close"].index.get_loc(df_metrics["close"].last_valid_index())])

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


    #test!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Dataframe cosntructed externally (APIS or metrics)

    #Collected data API/metrics
    values = [1.1429,0.000005,0.3936,0.8243,0.55,0.0015,0.13,0.35]
    titles = ["MVRV Z Score","Thermocap Ratio","NUPL","Puell Multiple", "Percent supply profit", "Reserve risk", "MA log relation", "Time channel"]
    df_IDs = ["name1","name2","name3","name4", "name5", "name6", "name7", "name8"]
    values_prev = [1.14,0.000004,0.32,0.8245,0.52,0.0016, 0.13, 0.36]

    #Researched data
    min_vals = [-1,0,-1.5,0.2,0,0.0005,0,0]
    max_vals = [12,0.000007,1,10,1,0.06,1,1]
    buy_bnds = [0,0.00000033,0,0.5,0.5,0.003,0.2,0.2]
    mid_bnds = [3.5,0.000002165,0.375,2.25,0.75,0.01,0.5,0.5]
    sell_bnds = [7,0.000004,0.75,4,0.95,0.02,0.8,0.8]

    df = pd.DataFrame(data = {"value":values,
                            "title":titles,
                            "df_ID":df_IDs,
                            "value_prev":values_prev,
                            "min_val":min_vals,
                            "max_val":max_vals,
                            "buy_bnd":buy_bnds,
                            "mid_bnd":mid_bnds,
                            "sell_bnd":sell_bnds})

    #Plotting range            
    fig = go.Figure()

    #Plotting-----------------------------------------

    nos_metrics = len(df)
    msp = 0.06
    sp = (1-(msp*nos_metrics))/nos_metrics

    for i, row in df.iterrows():
        add_metricBar(value = row["value"], title = row["title"], value_prev = row["value_prev"], min_val = row["min_val"], max_val = row["max_val"], buy_bnd = row["buy_bnd"], mid_bnd =row["mid_bnd"], sell_bnd = row["sell_bnd"], x = [0,1], y = [i*(msp+sp),i*(msp+sp)+sp])

    fig.update_layout(height = nos_metrics*60 , margin = {'t':0, 'b':50, 'l':300})

    fig.show()


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


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


    
    
    
    


    