import streamlit as st
import numpy as np
import pandas as pd

from pages.graphs import NUPL_graph


# @st.cache
def app():
    st.markdown("# On-Chain metrics")
    st.write("\n")
    # Summarizes some metrics
    st.markdown("Technical summary") 
    st.markdown("Onchain summary") 
    st.markdown("Sentiment summary")

    NUPL_graph  