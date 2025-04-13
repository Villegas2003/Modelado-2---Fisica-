import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Datos de entrada
st.title("Análisis de viga con tensión y reacciones")
masa = st.number_input("Masa (kg)", value=1200.0)
angulo_deg = st.number_input("Ángulo del cable (°)", value=30.0)
g = 9.81  # gravedad

# Cálculos
angulo_rad = np.radians(angulo_deg)
W = masa * g
T = (W * 2.5) / (3 * np.sin(angulo_rad))
Rx = T * np.cos(angulo_rad)
Ry = W - T * np.sin(angulo_rad)

# Resultados
st.subheader("Resultados")
st.write(f"Peso (W): {W:.2f} N")
st.write(f"Tensión (T): {T:.2f} N")
st.write(f"Reacción Rx: {Rx:.2f} N")
st.write(f"Reacción Ry: {Ry:.2f} N")

# Gráfica
fig, ax = plt.subplots(figsize=(8, 4))

# Dibujar viga
ax.plot([0, 5], [0, 0], 'saddlebrown', linewidth=6)
ax.text(0, 0.3, "Anclaje", ha='center')
ax.plot(0, 0, 'ro')  # punto de anclaje

# Peso (W)
ax.arrow(2.5, 0, 0, -1, head_width=0.1, head_length=0.2, color='red')
ax.text(2.5, -1.2, f"W = {W:.1f} N", ha='center')

# Tensión
x2 = 3 * np.cos(angulo_rad)
y2 = 3 * np.sin(angulo_rad)
ax.arrow(5, 0, -x2, y2, head_width=0.1, head_length=0.2, color='blue')
ax.text(5 - x2/2, y2/2 + 0.2, f"T = {T:.1f} N", ha='center', color='blue')

# Reacciones
ax.arrow(0, 0, Rx/1000, 0, head_width=0.1, head_length=0.2, color='green')
ax.arrow(0, 0, 0, Ry/1000, head_width=0.1, head_length=0.2, color='green')
ax.text(0.5, 0.2, f"Rx", color='green')
ax.text(-0.3, 0.5, f"Ry", color='green')

# Configurar gráfico
ax.set_xlim(-1, 6)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)
