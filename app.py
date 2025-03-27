import streamlit as st
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

# Configuración de página
st.set_page_config(page_title="PrediCt - Fed 2025 Forecast", layout="centered")

# Branding (opcional: logo si tenés URL pública en GitHub o CDN)
st.image("https://raw.githubusercontent.com/yourusername/predict-fed2025/main/Predict-Logo-BW.jpg", width=250)

# Títulos y autor
st.title("PrediCt - Forecast the Fed Rate")
st.subheader("Guide for certainty.")
st.markdown("_By Santiago Acosta · Global Predictive Analyst · metodopredict@gmail.com_")

# Inputs
st.markdown("### Adjust Key Economic Indicators")
inflation = st.slider("US Inflation Rate (%)", 2.0, 5.0, 3.2)
unemployment = st.slider("US Unemployment Rate (%)", 3.0, 6.0, 4.1)

# ARIMA Forecast Model with error handling
try:
    data = yf.download("^IRX", period="1y")["Close"].dropna()
    model = ARIMA(data, order=(1, 1, 0)).fit()
    forecast = model.forecast(steps=1)
    base_rate = forecast.iloc[0] if not forecast.empty else 4.25
except:
    base_rate = 4.25  # Default fallback if ARIMA fails

# Conditional rate cut logic
rate_cut = 0.5 if inflation < 3.5 and unemployment > 4 else 0
predicted_rate = base_rate - rate_cut

# S&P 500 Estimate
try:
    sp500_base = yf.download("SPY", period="1d")["Close"][-1]
    sp500_predicted = sp500_base * (1.08 if predicted_rate < 4 else 1)
except:
    sp500_predicted = 5200  # Default fallback

# Outputs
st.metric("📉 Predicted Fed Rate (April 2025)", f"{predicted_rate:.2f}%")
st.metric("📈 Estimated S&P 500 Index", f"${sp500_predicted:.2f} USD")

# Call to Action
st.markdown("---")
st.markdown("📩 Want a full PDF report with visuals? Email us at **metodopredict@gmail.com**")
