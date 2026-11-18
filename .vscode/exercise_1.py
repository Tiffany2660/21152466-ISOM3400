import pandas as pd
import streamlit as st

stocks = pd.read_csv("https://raw.githubusercontent.com/vega/vega-datasets/main/data/stocks.csv", 
                     parse_dates=['date'], date_format="%b %d %Y")

st.markdown("###")
st.write(stocks)

"---"

year = 2005
symbols = ["AAPL", "IBM", "MSFT", "AMZN"]

prices_2005 = stocks.query(f"date < {year+1} and date >= {year} and symbol in {symbols}")

st.line_chart = (prices_2005, x="date",y="price",color="symbol")
