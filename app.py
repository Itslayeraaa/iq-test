import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Test de IQ Online", page_icon="🧠", layout="centered")
st.title("🧠 Test de IQ Online")

st.markdown("""
Realiza el **Test de IQ Online Gratis** y descubre tu nivel de inteligencia.  
Puedes usar el test incrustado desde tu archivo `index.html`.
""")

# Mostrar el test HTML usando components.html
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=700, scrolling=True)

st.markdown("---")

# Captura de puntuación manual para interpretación
st.subheader("Introduce tu puntuación para ver tu nivel de inteligencia")
score = st.number_input("Tu puntuación (0-10):", min_value=0, max_value=10, step=1)

if st.button("Ver nivel de inteligencia"):
    if score <= 3:
        level = "Inteligencia baja 🧩"
    elif score <= 6:
        level = "Inteligencia promedio 🟡"
    elif score <= 8:
        level = "Inteligencia alta 🟢"
    else:
        level = "Inteligencia muy alta 🔵"

    st.success(f"Tu puntuación: {score}/10")
    st.info(f"Nivel de inteligencia: {level}")
    st.balloons()

st.markdown("---")
st.info("💡 **Nota:** Los anuncios de Google AdSense solo se mostrarán correctamente cuando subas tu `index.html` a Netlify.")
