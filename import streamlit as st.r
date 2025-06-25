import streamlit as st

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Portafolio de Samira Ortiz", layout="centered")

# CABECERA
st.title("Samira Ortiz")
st.subheader("Estudiante Universitaria - Facultad de Ciencias y Artes de la Comunicación - PUCP")
st.markdown("**Carrera:** Comunicación Audiovisual")
st.markdown("**Correo:** betsabethortiz4@gmail.com")

# SECCIÓN: PRESENTACIÓN
st.markdown("---")
st.header("Sobre mí")
st.markdown("""
Soy estudiante de Comunicación Audiovisual en la Pontificia Universidad Católica del Perú (PUCP). 
Me interesa explorar el mundo del cine, la fotografía, el periodismo digital y la producción audiovisual.

Soy una persona comprometida con mi desarrollo artístico y profesional, con experiencia en actividades creativas, académicas y laborales.
""")

# EDUCACIÓN
st.markdown("---")
st.header("Formación académica")
st.markdown("""
- **Educación Inicial:** Estudios básicos en una institución educativa con formación integral.
- **Primaria:** Desarrollo de habilidades comunicativas, participación escolar y actividades artísticas.
- **Secundaria:** Fortalecimiento académico y participación en talleres culturales.
- **Preparación preuniversitaria:** Enfocada en el ingreso a la PUCP, desarrollando habilidades en comunicación y humanidades.
""")

# EXPERIENCIA
st.markdown("---")
st.header("Experiencia")
st.markdown("""
- **Secretaria en academia preuniversitaria**  
  Organización de horarios, atención al público y apoyo en gestión educativa.

- **Danzante en la agrupación Dinastía Wanka**  
  Participación en concursos folclóricos en Huancayo y otras regiones.

- **Fotógrafa temporal en la agrupación de huaylas Juventud Incontrastable**  
  Registro visual de presentaciones, ensayos y eventos culturales.
""")

# GALERÍA (puedes cambiar por URLs o eliminar si aún no tienes imágenes)
st.markdown("---")
st.header("Galería de trabajos")
st.image("https://via.placeholder.com/600x400.png?text=Trabajo+1", caption="Captura de proyecto audiovisual", use_column_width=True)
st.image("https://via.placeholder.com/600x400.png?text=Trabajo+2", caption="Registro fotográfico de evento", use_column_width=True)

# PIE DE PÁGINA
st.markdown("---")
st.markdown("Portafolio creado con ❤️ usando Streamlit")