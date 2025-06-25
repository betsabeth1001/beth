import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portafolio de Samira Ortiz", layout="wide")

# ======== INICIO ========
st.markdown("<h1 style='text-align: center;'>Samira Ortiz</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Estudiante Universitaria - Facultad de Ciencias y Artes de la Comunicación - PUCP</h4>", unsafe_allow_html=True)
st.image("img/hero.png", width=200)

# ======== SOBRE MÍ ========
st.header("Sobre mí")
st.write("""
Hola, soy **Samira Ortiz**. Soy estudiante de Comunicación Audiovisual en la Pontificia Universidad Católica del Perú, apasionada por contar historias a través de la imagen y el sonido. Me interesa el cine, la dirección, la edición y la creación de contenido visual con enfoque social y creativo. Busco explorar nuevas narrativas que conecten con las personas y generen reflexión.
""")

# Datos personales
with st.expander("📌 Datos Personales"):
    st.markdown("""
    - **Cumpleaños:** 10-01-2004  
    - **Teléfono:** 966 956 976  
    - **Email:** betsabethortiz4@gmail.com  
    - **Instagram:** @ortizbetsabeth  
    - **Dirección:** Urb. Los Jardines de Shangrila Mz. F1 Lt.16  
    - **Ciclo:** Quinto ciclo
    """)

# Intereses
with st.expander("💡 Intereses"):
    intereses = ["🎮 Juegos", "🎧 Danza", "✈️ Viajar", "🥾 Deporte", "📚 Libros", "📷 Fotos", "🎬 Películas", "🏔️ Cultura"]
    st.write(", ".join(intereses))

# ======== SKILLS ========
st.header("Skills")
col1, col2 = st.columns(2)

with col1:
    st.subheader("📷 Technical Skills")
    st.progress(75, "Manejo de cámaras y equipos de grabación")
    st.progress(89, "Edición de video y postproducción")
    st.progress(95, "Diseño sonoro y edición de audio")
    st.progress(81, "Guion y estructura narrativa")
    st.progress(55, "Motion graphics y efectos visuales")

with col2:
    st.subheader("👩‍💼 Professional Skills")
    st.progress(80, "Comunicación")
    st.progress(70, "Trabajo en equipo")
    st.progress(99, "Creatividad")
    st.progress(65, "Dedicación")
    st.progress(94, "Gestión de proyectos")

# ======== CURRICULUM ========
st.header("Curriculum")

with st.expander("🎓 Educación"):
    st.markdown("""
    - **Inicial - I.E.P. Jesús Obrero (2007 - 2009)**  
      Desarrollo emocional, cognitivo y social en entornos creativos.
      
    - **Primaria - I.E.P. Divino Maestro de Pro (2010 - 2015)**  
      Estrategias didácticas para pensamiento crítico y creatividad.

    - **Secundaria - I.E.P. Divino Maestro de Pro (2005 - 2008)**  
      Formación integral con preparación para ingreso universitario.
    """)

with st.expander("💼 Experiencia de Trabajo"):
    st.markdown("""
    - **Secretaria - Academia San Marci (2016 - 2018)**  
      Atención al público, gestión de matrículas y organización documental.

    - **Danzante - Dinastía Wanka (2024 - 2025)**  
      Concursos y presentaciones culturales en Huancayo.

    - **Fotógrafa - Juventud Incontrastable (2025)**  
      Captura visual de presentaciones y eventos de Huaylas.
    """)

# ======== PORTFOLIO ========
st.header("🎞️ Portafolio")

portfolio = [
    ("img/p1.jpg", "Agrupación Folclórica", "Juventud Incontrastable"),
    ("img/p2.png", "Agrupación Folclórica", "Calentamiento"),
    ("img/p9 (1).png", "Huaridanza", "Cajero"),
    ("img/p4.png", "Dinastía Wanka", "Pareja Wanka"),
    ("img/p7.jpg.JPG", "Huaridanza", "Herencia 1"),
    ("img/p8. jpg.JPG", "Huaridanza", "Herencia 2"),
]

for i in range(0, len(portfolio), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(portfolio):
            img_path, title, desc = portfolio[i + j]
            with cols[j]:
                st.image(img_path, caption=f"**{title}** - {desc}", use_column_width=True)