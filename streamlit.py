import streamlit as st
import cv2
import numpy as np
import os 

st.set_page_config(
    page_title='A COMER!',
    page_icon="🍔",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None)

with st.sidebar:
    githublink = '[GitHub Repo](https://github.com/Javingles/nADaEnLAnEvERa)'

    st.image(
        "https://www.gifsanimados.org/data/media/1481/frigorifico-y-nevera-imagen-animada-0011.gif",
        width=200)

    st.sidebar.write('Código en: ' + githublink)

    with st.expander('Sobre el proyecto'):
        st.write('La idea del proyecto etc .')
        st.write('Si quieres contribuir: ', githublink)
    #st.success("Selecciona una página.")

# Creamos una lista vacía para almacenar los alimentos faltantes
alimentos_faltantes = []

# Configuración de la página de Streamlit
st.title("¿Nada en tu nevera?")
#st.write("Carga una foto y añade los alimentos faltantes.")

# Cargar la foto
uploaded_file = st.file_uploader("Sube tu foto", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Leer la imagen con OpenCV
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), 1)
    
    # Guardar la imagen en un archivo temporal
    temp_file = "temp_image.jpg"
    cv2.imwrite(temp_file, image)
    
    # Mostrar la foto
    st.image(image, channels="BGR", use_column_width=True)

    # Preguntar si falta algún alimento
    falta_alimento = st.checkbox("¿Falta algún alimento?")
    if falta_alimento:
        alimento_faltante = st.text_input("Escribe el alimento que falta:")
        if alimento_faltante:
            alimentos_faltantes.append(alimento_faltante)
            st.success("Alimento agregado a la lista de alimentos faltantes.")

    # Aquí puedes llamar a tu modelo YOLO para el reconocimiento de objetos con la imagen en temp_file
    # y agregar la lógica para obtener los resultados del modelo
    
    # Ejemplo de resultados del modelo
    resultados_modelo = []
    
    # Agregar los resultados del modelo a la lista de alimentos faltantes
    alimentos_faltantes.extend(resultados_modelo)

    # Eliminar el archivo temporal
    if temp_file:
        os.remove(temp_file)

# Imprimir la lista de alimentos faltantes
st.subheader("Lista de alimentos faltantes:")
for alimento in alimentos_faltantes:
    st.write(alimento)

footer = """
    <style>
    footer {visibility: hidden;}
    MainMenu {visibility: hidden;}

    # footer:hover,  footer:active {
    #     color: #fa4d00;
    #     background-color: transparent;
    #     text-decoration: underline;
    #     transition: 400ms ease 0s;
    # }
    footer:after {
        content:'Created by A COMER! ©'; 
        visibility: visible;
        display: block;
        position: relative;
        padding: 5px;
        top: 2px;
    }
    </style>
    """
st.markdown(footer, unsafe_allow_html=True)