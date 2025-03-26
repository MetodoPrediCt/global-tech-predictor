import streamlit as st
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

st.set_page_config(page_title="PrediCt - Fed 2025 Forecast", layout="centered")

st.image("https://raw.githubusercontent.com/tuusuario/predict-fed2025/main/Predict-Logo-rgb.png", width=250)  # Reemplazar por tu URL de logo
st.title("PrediCt - Forecast the Fed Rate")
st.subheader("Guide for certainty.")

st.markdown("_By Santiago Acosta · Global Predictive Analyst · metodopredict@gmail.com_")

inflation = st.slider("US Inflation Rate (%)", 2.0, 5.0, 3.2)
unemployment = st.slider("US Unemployment Rate (%)", 3.0, 6.0, 4.1)

data = yf.download("^IRX", period="1y")["Close"]
model = ARIMA(data, order=(1,1,0)).fit()
base_rate = model.forecast()[0]
rate_cut = 0.5 if inflation < 3.5 and unemployment > 4 else 0
predicted_rate = base_rate - rate_cut

sp500_base = yf.download("SPY", period="1d")["Close"][-1]
sp500_predicted = sp500_base * (1.08 if predicted_rate < 4 else 1)

st.metric("Predicted Fed Rate (April 2025)", f"{predicted_rate:.2f}%")
st.metric("Estimated S&P 500 Index", f"${sp500_predicted:.2f} USD")

st.markdown("---")
st.markdown("📩 Want a full visual report? Email **metodopredict@gmail.com**")
