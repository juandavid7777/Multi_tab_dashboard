import streamlit as st
import numpy as np
import pandas as pd

from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from pages.graphs import NUPL_graph


# @st.cache
def app():
    st.markdown("# On-Chain metrics")
    st.write("\n")
    
    NUPL_graph
    

    