import os
import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multipage import MultiPage
from pages import home, sentiment_analysis, tech_analysis, onchain_analysis # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('Logo.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.beta_columns(2)
col1.image(display, width = 300)
col2.title("Serenity Crypto Dashboard")

# Add all your application here
app.add_page("Homepage", home.app)
app.add_page("Technical Analysis", tech_analysis.app)
app.add_page("On-chain Analsysis", onchain_analysis.app)
app.add_page("Sentiment Analysis", sentiment_analysis.app)

# The main app
app.run()
