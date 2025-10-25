import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Test de IQ Avanzado", page_icon="🧠", layout="centered")
st.title("🧠 Test de IQ Avanzado")

st.markdown("""
Haz el test incrustado abajo.  
Luego selecciona tu puntuación con los botones para ver tu nivel de inteligencia inmediatamente.
""")

# Mostrar el test HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()
components.html(html_code, height=700, scrolling=True)

st.markdown("---")

# Botones de puntuación rápida
st.subheader("Selecciona tu puntuación:")
cols = st.columns(11)
score = None
for i in range(11):
    if cols[i].button(str(i)):
        score = i

# Interpretación instantánea
if score is not None:
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
