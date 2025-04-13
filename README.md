# Modelado 2

Este proyecto permite simular el análisis de una viga con cable inclinado utilizando fórmulas físicas para calcular la tensión, las reacciones en la viga y mostrar una representación gráfica.

## Requisitos

- *Python 3.x* (se recomienda la versión 3.9 o superior).
- *Streamlit*: Framework para construir la interfaz web.
- *Matplotlib*: Biblioteca para gráficos.
- *NumPy*: Biblioteca para cálculos numéricos.

## Descarga de Python 3.9.0
- *Windows*: Python 3.9.0 para Windows​
- *macOS*: Python 3.9.0 para macOS​
- *Linux*: La mayoría de distribuciones de Linux incluyen Python en sus repositorios. Puedes instalar Python 3.9 utilizando el gestor de paquetes de tu distribución.

## Instalación

1. Clona o descarga este repositorio en tu máquina local.


2.	Instala las dependencias necesarias desde requirements.txt:

```bash
pip install -r requirements.txt
```

3.	Instala Streamlit
   
```bash
pip install streamlit  
```

Uso
	1.	Una vez que hayas instalado las dependencias, ejecuta la aplicación:
 
```bash
streamlit run app.py
```


	1.	La aplicación se abrirá automáticamente en tu navegador predeterminado.
	2.	Introduce los valores de entrada:
	•	Masa (kg): La masa del objeto que cuelga de la viga.
	•	Ángulo del cable (°): El ángulo que forma el cable con la horizontal.
	3.	La aplicación calculará automáticamente la tensión en el cable, las reacciones en la viga, y mostrará una gráfica de la viga con las fuerzas representadas.

