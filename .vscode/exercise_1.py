import pandas as pd
import streamlit as st

stocks = pd.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
                     parse_dates=['date'], date_format="%b %d %Y")

st.write(stocks)
