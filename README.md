![Screenshot from 2023-06-16 17-13-53](https://github.com/Javingles/nADaEnLAnEvERa/assets/109460138/a9841d84-44db-424b-b16e-d73ea84ba2e9)

### :busts_in_silhouette: Componentes
<b>Víctor Comendador,</b> :arrow_right: https://github.com/victorrmtz  
<b>Ana de Córdoba,</b> :arrow_right: https://github.com/AnadeCordoba  
<b>Javier Inglés,</b> :arrow_right: https://github.com/Javingles  
<b>Efrén Marrero,</b> :arrow_right: https://github.com/EFMARR 
<b>Anghi Sánchez,</b> :arrow_right: https://github.com/AnghiSanchez   

### :notebook: Proyecto 
Creación de recetas con ChatGPT en base a productos alimenticios dados previamente detectados y clasificados con Computer Vision. Se nos ocurrieron diferentes modos de realizar el trabajo:  
<b>Imágenes captadas en el interior de la nevera:</b> Dificultad de visión si está la nevera muy llena.  
<b>Imágnes captadas fuera de la nevera:</b> No resulta práctico por el motivo mencionado en la primera opción.  
<b>Modelo OCR para los tickets de compra:</b> Diferentes tipos de tickets y posibles abreviaturas.  
<b>Realización de un Chatbot:</b> Se puede hacer directamente en ChatGPT

Finalmente optamos por la primera opción que es también la que se nos proporcionaba desde un principio.

### :factory: Funcionalidades
- <b>Funcionalidad 1:</b> Clasificación y etiquetación de alimentos en una imagen dada.
- <b>Funcionalidad 2:</b> Esos alimentos, junto con otros que añadamos si queremos a la lista, se le proporcionan a ChatGPT para que nos devuelva 3 recetas de su creación.

### :robot: Roboflow
Esta aplicación se utiliza para el etiquetado de los alimentos y entrenado posterior del modelo. Se han realizado diversos entrenamientos añadiendo o quitando opciones que nos ofrece el programa, entre ellas tenemos: 
- Características comunes: Más de 300 imágnes, algoritmo YOLO v8 y 3 outputs de salida.
- Modelo inicial: Color, Auto-orient, Resize y 90ª Rotate. Resultado: 56.8% de precisión.
- Modelo 2: Saturation y Noise. Resultado: 73.7% de precisón.
- Modelo 3: Las mismas opciones pero esta vez en Grayscale. Resultado: 60.9% de precisión.
- Modelo 4:
- Modelo 5:

### :loudspeaker: Streamlit
Esta plataforma nos permite desplegar una interfaz de usuario para que éste introduzca la imagen a etiquetar. Después de realizar todo el proceso interno, que consiste en pasarle los alimentos identificados en la imagen al ChatGPT y otros que podamos rellenar a mano, esta herramienta de IA nos proporcione 3 recetas de su creación.

### :rocket: Resultado
Esta es la solución del trabajo realizado, donde se pueden apreciar------------------------------------- 
<p align = "center">
<img src="URL URL URL URL URL URL URL URL" height=”300”       width=1000” style= "text-align: center"> 
</p>

### :open_file_folder: Estructura de este repositorio

| Carpeta | Fichero         | Descripción                                  |
|---------|-----------------|----------------------------------------------|
| `main`  | `main`          | Se pasa el proyecto definitivo únicamente    |
|         | `ReadMe`        | Documentación y Resumen del proyecto         |
| `dev`   | `xxxxxxxxx`     | Ficheros necesarios para el despliegue xxx   |
|         | `xxxxxxxx`      | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  |
|         | `xxxxxxxxxxxx`  | Distintas mágenes de prueba                  |

### :computer: Tecnologías aplicadas
- <b>Lenguajes utilizados:</b> Python, HTML5 y CSS3.
- <b>Librerías utilizadas:</b> Yolov8,
- <b>Computer Vision:</b> Roboflow
- <b>Dashboard:</b> Streamlit
- <b>Documentación:</b> MarkDown y Swagger
- <b>Presentación:</b> Canvas
- <b>Control de versiones:</b> Git/GitHub
- <b>Editores:</b> Jupyter, Visual Studio Code

### Requerimientos
Estas son las librerías utilizadas en el desarrollo del proyecto. Se encuentran en el archivo "requirements.txt" con sus respectivas versiones.
- <b>Roboflow</b>
- <b>Streamlit</b> 
- 
