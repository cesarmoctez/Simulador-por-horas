import streamlit as st
import streamlit.components.v1 as components

# Configurar la página de Streamlit para que use todo el ancho de la pantalla
st.set_page_config(layout="wide", page_title="Simulador de Costos Logísticos")

# Leer el código de tu archivo HTML
with open("simulador.html", "r", encoding="utf-8") as f:
    codigo_html = f.read()

# Renderizar el HTML dentro de Streamlit
# Ajustamos el height a 1200 o más para que no aparezcan barras de desplazamiento dobles
components.html(codigo_html, height=1200, scrolling=True)