# Análisis de Viga con Cable Inclinado

Este proyecto permite simular el análisis de una viga con cable inclinado utilizando fórmulas físicas para calcular la tensión, las reacciones en la viga y mostrar una representación gráfica.

## Requisitos

- *Python 3.x* (se recomienda la versión 3.7 o superior).
- *Streamlit*: Framework para construir la interfaz web.
- *Matplotlib*: Biblioteca para gráficos.
- *NumPy*: Biblioteca para cálculos numéricos.

## Instalación

1. Clona o descarga este repositorio en tu máquina local.


2.	Instala las dependencias necesarias desde requirements.txt:

pip install -r requirements.txt


Uso
	1.	Una vez que hayas instalado las dependencias, ejecuta la aplicación:

streamlit run app.py


	1.	La aplicación se abrirá automáticamente en tu navegador predeterminado.
	2.	Introduce los valores de entrada:
	•	Masa (kg): La masa del objeto que cuelga de la viga.
	•	Ángulo del cable (°): El ángulo que forma el cable con la horizontal.
	3.	La aplicación calculará automáticamente la tensión en el cable, las reacciones en la viga, y mostrará una gráfica de la viga con las fuerzas representadas.

