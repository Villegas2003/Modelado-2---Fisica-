import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuración inicial
st.set_page_config(page_title="Análisis de Viga", layout="centered")
st.title("📐 Análisis de viga con cable inclinado")

# Entrada de usuario
st.sidebar.header("Datos de entrada")
masa = st.sidebar.number_input("Masa (kg)", value=1200.0)
angulo_deg = st.sidebar.slider("Ángulo del cable (°)", 0.0, 90.0, 30.0)
g = 9.81  # gravedad en m/s²

# Cálculos
angulo_rad = np.radians(angulo_deg)
W = masa * g
T = (W * 2.5) / (3 * np.sin(angulo_rad))
Rx = T * np.cos(angulo_rad)
Ry = W - T * np.sin(angulo_rad)

# Resultados
st.subheader("Resultados")
st.markdown(f"**Peso (W):** {W:.2f} N")
st.markdown(f"**Tensión (T):** {T:.2f} N")
st.markdown(f"**Reacción Rx:** {Rx:.2f} N")
st.markdown(f"**Reacción Ry:** {Ry:.2f} N")

# Gráfica
fig, ax = plt.subplots(figsize=(8, 4))

# Viga horizontal
ax.plot([0, 5], [0, 0], 'saddlebrown', linewidth=6)
ax.text