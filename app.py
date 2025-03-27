import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr"],
    "Inflación": [3.2, 3.4, 3.1, 2.9]
})

fig = px.line(df, x="Mes", y="Inflación", title="Inflación mensual 2025")
fig.show()
import plotly.express as px

# Configuración profesional de la página
st.set_page_config(
    page_title="Global Tech Predictor",
    page_icon="🌐",
    layout="wide"
)

# Título y descripción
st.title("🌍 Global Tech Predictor")
st.markdown("""
    *Real-time market predictions for tech startups worldwide.  
    Data sources: Crunchbase, World Bank, and proprietary AI models.*
""")

# Carga de datos con caché (¡más rápido!)
@st.cache_data
def load_data():
    # Ejemplo: Datos públicos de acciones tech (reemplaza con tus datos)
    data = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=12, freq="M"),
        "Revenue": [100, 120, 150, 180, 200, 240, 300, 350, 400, 450, 500, 600]
    })
    return data

df = load_data()

# Gráfico interactivo con Plotly
fig = px.line(df, x="Date", y="Revenue", 
              title="Tech Startup Revenue Growth (2023)",
              labels={"Revenue": "Revenue (USD thousands)"})
st.plotly_chart(fig, use_container_width=True)

# Botón de acción (ejemplo: descarga de reporte)
if st.button("📊 Download Full Report (PDF)"):
    st.success("Report generated! Check your downloads.")
