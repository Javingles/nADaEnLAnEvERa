import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from roboflow import Roboflow
from tempfile import NamedTemporaryFile
import os
from dotenv import load_dotenv
import json
import openai


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave de la API desde las variables de entorno
api_key = os.getenv('api_key')

# Inicializar Roboflow
rf = Roboflow(api_key)
project = rf.workspace().project("nevera_javi")
model = project.version(4).model

# Configurar tu clave de API de OpenAI
gpt_key = os.getenv('gpt_key')
openai.api_key = gpt_key

@st.cache(allow_output_mutation=True)
def load_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def predict(image_path):
    prediction = model.predict(image_path).json()

    # Verificar si la respuesta es una cadena de texto
    if isinstance(prediction, str):
        prediction = json.loads(prediction)

    return prediction

def obtener_sugerencias_recetas(etiquetas):
    etiquetas_str = ",".join(etiquetas)
    solicitud_completado = f"Quiero recetas con los siguientes ingredientes: {etiquetas_str}."
    respuesta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=solicitud_completado,
        max_tokens=90,
        temperature=0.7,
        n=3,  # Obtener 3 sugerencias de recetas
        stop=None,
        timeout=15,
    )

    # print("respuesta: ", respuesta)
    sugerencias_recetas = [opcion['text'].strip() for opcion in respuesta['choices']]
    return sugerencias_recetas

st.set_page_config(
    page_title='¡A COMER!',
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
        st.subheader('Idea del Proyecto')
        st.write('¿No tienes idea de qué hacer de cena? ¿Te apetece cocinar con inteligencia artificial y redes neuronales? ¿Quieres ahorrar?')
        st.write('Para evitar que el mundo siga desperdiciando gran parte de la producción alimentaria, mejorar el medio ambiente, la producción de gases, luchar contra el hambre y poder ahorrar. Carga una foto de tu nevera (con la puera abierta) y te convertiremos en el mejor chef.')


food_classes = []

st.title("¿Nada en tu neverAI?")

uploaded_file = st.file_uploader("Sube tu foto", type=["jpg", "jpeg", "png"]) # Subir la foto

if uploaded_file is not None:
    with NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_image_path = temp_file.name

    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen cargada', use_column_width=True)

    prediction = predict(temp_image_path)
    labels = prediction['predictions']

    label_dict = {}
    image_classes = []
    for label in labels:
        class_name = label['class']
        image_classes.append(class_name)
        confidence = label['confidence']
        if class_name in label_dict:
            label_dict[class_name].append(confidence)
        else:
            label_dict[class_name] = [confidence]

    st.subheader("Etiquetas encontradas:")
    for class_name, confidences in label_dict.items():
        avg_confidence = round(sum(confidences) / len(confidences) * 100)
        st.write(f"- {class_name}: {avg_confidence}% de acierto")

    img = load_image(temp_image_path)
    fig, ax = plt.subplots()
    ax.imshow(img)

    colors = ['r', 'g', 'b', 'y', 'm', 'c']
    for i, label in enumerate(labels):
        x = int(label['x'])
        y = int(label['y'])
        width = int(label['width'])
        height = int(label['height'])
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor=colors[i % len(colors)], facecolor='none')
        ax.add_patch(rect)
        text_y = y - 10 if y > 20 else y + height + 10
        ax.text(x, text_y, f"{label['class']} {avg_confidence}%", color=colors[i % len(colors)], fontsize=7, va='center')

    plt.axis('off')
    st.pyplot(fig)

    os.remove(temp_image_path)

    temp_file = "temp_image.jpg"
    image_np = np.array(image)  # Convertir la imagen a una matriz NumPy
    cv2.imwrite(temp_file, cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))  # Guardar la imagen convertida

    falta_alimento = st.checkbox("¿Falta algún alimento?")
    if falta_alimento:
        alimento_faltante = st.text_input("Escribe el alimento que falta:")
        if alimento_faltante:
            food_classes.append(alimento_faltante)
            st.success("Alimento agregado a la lista de alimentos faltantes.")

    food_classes.extend(image_classes)

    if temp_file:
        os.remove(temp_file)

    sugerencias = obtener_sugerencias_recetas(food_classes)

    st.subheader("Sugerencias de recetas:")
    for i, sugerencia in enumerate(sugerencias):
        st.write(f"Receta {i+1}: {sugerencia}")

footer = """
    <style>
    footer {visibility: hidden;}
    MainMenu {visibility: hidden;}

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
