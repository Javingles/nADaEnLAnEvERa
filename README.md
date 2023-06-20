![Screenshot from 2023-06-20 09-38-12](https://github.com/Javingles/nADaEnLAnEvERa/assets/109460138/dabb54bd-4d76-477e-b2f0-a8d992cc34be)


### :busts_in_silhouette: Componentes
<b>Víctor Comendador,</b> :arrow_right: https://github.com/victorrmtz  
<b>Ana de Córdoba,</b> :arrow_right: https://github.com/AnadeCordoba  
<b>Javier Inglés,</b> :arrow_right: https://github.com/Javingles  
<b>Efrén Marrero,</b> :arrow_right: https://github.com/EFMARR  
<b>Anghi Sánchez,</b> :arrow_right: https://github.com/AnghiSanchez   

### :notebook: Proyecto 
Creación de recetas con ChatGPT en base a productos alimenticios previamente detectados y clasificados con Computer Vision.  
Teníamos varias opciones para realizar el proyecto, aquí las citamos:  
<b>Imágenes captadas en el interior de la nevera:</b> Dificultad de visión si la nevera está muy llena.  
<b>Imágnes captadas fuera de la nevera:</b> No resulta práctico por el motivo mencionado en la primera opción.  
<b>Modelo OCR para los tickets de compra:</b> Diferentes tipos de tickets y posibles abreviaturas.  
<b>Realización de un Chatbot:</b> Se puede hacer directamente en ChatGPT.  
Finalmente optamos por la primera opción que es también la que se nos proporcionaba desde un principio.

### :factory: Funcionalidades
- <b>Funcionalidad 1:</b> Clasificación y etiquetación de alimentos en una imagen dada.
- <b>Funcionalidad 2:</b> Esos alimentos, junto con otros añadidos a la lista, se le proporcionan a ChatGPT para que nos devuelva 3 recetas de su creación.

### :floppy_disk: Dataset
Los imágenes utilizadas han sido proporcionadas por cada uno de los integrantes del proyecto realizando los siguientes pasos:
- Fotografiado del interior de la nevera teniendo en consideración distintos ángulos, distinta iluminación y la aproximación o no de los alimentos por baldas.
- Creación de las etiquetas con Roboflow de cada tipo de alimento. Se empezó etiquetando cada alimento y se crearon 78 etiquetas, para mejorar el modelo y la
precisión de este, se consideró oportuno reducir estas etiquetas a de 34.
- Etiquetado de cada imagen por separado utilizando bounding boxes, al trabajar con redes neuronales convolucionales, estas se encargan de identificar los márgenes de
cada alimento.
- El dataset se divide en Training(70%), Validation(17%) y Testing(13%).

![Screenshot from 2023-06-20 16-15-27](https://github.com/Javingles/nADaEnLAnEvERa/assets/109460138/3dfbf895-b2d5-44f4-ac45-c6bd1bb5d549)



### :robot: Roboflow
Se ha trabajado en Roboflow, que es una plataforma de inteligencia artificial diseñada para facilitar la construcción y despliegue de modelos de visión por ordenador, donde se puede crear y etiquetar datasets. Ésta proporciona una API Key del proyecto en el que se trabaje la cual se llama en el código para la conexión. Se han realizado diversos entrenamientos añadiendo o quitando opciones de Preprocessing y Data Augmentation que nos ofrece el programa, entre ellas aplicamos: 
- Características comunes: Más de 300 imágenes, algoritmo YOLO v8 y 3 outputs de salida.
- Modelo inicial: Color, Auto-orient, Resize y 90ª Rotate. Resultado: 56.8% de precisión.
- Modelo 2: Se añaden Saturation y Noise. Resultado: 73.7% de precisón.
- Modelo 3: Las mismas opciones pero esta vez en Grayscale. Resultado: 60.9% de precisión.  
Se elige etiquetar los alimentos con bounding boxes ya que la herramienta “polygon tool” se emplea para la segmentación de objetos y no para la detección, como es este caso. Los beneficios de la detección con bounding boxes se prefiere sobre la segmentación por varias razones. Es más eficiente computacionalmente y menos compleja, ya que solo requiere definir una caja alrededor del objeto. La anotación de datos es más sencilla, lo que reduce costos y tiempo de etiquetado. Es adecuada para muchas aplicaciones prácticas donde no se necesita una forma precisa del objeto. Sin embargo, la segmentación se utiliza cuando se requiere mayor precisión y comprensión detallada de la forma y estructura del objeto en la imagen.
Se ha hecho público y se puede consultar en este enlace:
https://universe.roboflow.com/neveraflow/nadaenlanevera

![Screenshot from 2023-06-20 16-47-00](https://github.com/Javingles/nADaEnLAnEvERa/assets/109460138/a8d42025-281e-4604-bbe8-3894dabca7f4)


### :loudspeaker: Streamlit
Esta plataforma nos permite desplegar una interfaz de usuario para que éste introduzca la imagen a etiquetar. Después de realizar todo el proceso interno, que consiste en pasarle los alimentos identificados en la imagen al ChatGPT y otros que podamos rellenar a mano, esta herramienta de IA nos proporcione 3 recetas de su creación.
Para la conexión con ChatGPT es necesaria una API key proporcionada por OpenAI al registrar una cuenta, esta se llama en el código y conecta con el modelo ‘text-davinci-003’, ajustando una creatividad de 0,7, el límite de tokens entre otros. 

![Screenshot from 2023-06-20 16-39-29](https://github.com/Javingles/nADaEnLAnEvERa/assets/109460138/3aaee5fb-ba50-4326-898e-298ac4b9b49b)


### :rocket: ChatGPT
Y esta es la solución del trabajo realizado, hay facetas que mejorar como la preparación y las recetas en si, pero el objetivo del proyecto se ha realizado con éxito. En futuras implementaciones se podrán incluir temas nutricionales, dietéticos, mejorar la estética de la interfaz y por supuesto afinar más el modelo predictivo.

![Screenshot from 2023-06-20 16-42-41](https://github.com/Javingles/nADaEnLAnEvERa/assets/109460138/aa7edf8f-ee40-428b-aee9-a021705627d6)


### :open_file_folder: Estructura de este repositorio

| Carpeta | Fichero             | Descripción                                |
|---------|---------------------|--------------------------------------------|
| `main`  | `main`              | Se pasa el proyecto definitivo únicamente  |
|         | `ReadMe`            | Documentación y Resumen del proyecto       |
| `dev`   | `web.py`            | Interfaz Web creada con Streamlit          |
|         | `Readme`            | Documentación y Resumen del proyecto       |
|         | `requirements.txt`  | Requirimientos para el despliegue          |
|         | `.gitignore`        | Ocultación de información sensible         |

### :computer: Tecnologías aplicadas
- <b>Lenguajes utilizados:</b> Python, HTML5 y CSS3.
- <b>Librerías utilizadas:</b> Yolov8, Roboflow, Streamlit, OpenAI
- <b>Computer Vision:</b> Roboflow
- <b>Dashboard:</b> Streamlit
- <b>Documentación:</b> MarkDown y Swagger
- <b>Presentación:</b> Canvas
- <b>Control de versiones:</b> Git/GitHub
- <b>Editores:</b> Jupyter, Visual Studio Code
