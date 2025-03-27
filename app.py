import streamlit as st
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import plotly.express as px

st.image("logo_predict.png")
st.title("Metodo PrediCt - Fed 2025 Prediction")
st.write("Santiago Acosta - International Trade Advisor | metodopredict@gmail.com | +54 351 688-3177 | Javier Lopez 2656, 5009 Córdoba, Argentina")

inflacion = st.slider("US Inflation (%)", 2.0, 5.0, 3.2)
desempleo = st.slider("US Unemployment (%)", 3.0, 6.0, 4.1)

data = yf.download("^IRX", period="1y")["Close"]
model = ARIMA(data, order=(1,1,0)).fit()
tasa_fed = model.forecast()[0] - (0.5 if inflacion < 3.5 and desempleo > 4 else 0)
sp500_base = yf.download("SPY", period="1d")["Close"][-1]
sp500_pred = sp500_base * (1.08 if tasa_fed < 4 else 1)

st.metric("Predicted Fed Rate (April 2025)", f"{tasa_fed:.2f}%")
st.metric("Estimated S&P 500", f"${sp500_pred:.2f} (+8%)")
fig = px.line(data, title="1-Year Treasury Yield Trend", labels={"value": "Yield (%)"})
st.plotly_chart(fig)
st.image("banner_predict.png")

if st.button("Request Custom Report ($50)"):
    st.success("Email your request to metodopredict@gmail.com")
