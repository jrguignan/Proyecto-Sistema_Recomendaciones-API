![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)


![henry](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/images/Logo%20HENRY.png)

# Proyecto Sistema de Recomendación Steam - API
## Data Science & Machine Learning Operations (MLOps) 

<p align="center">
<img src="https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/images/MILOPS.png"  height=300>
</p>

## Introducción

Este proyecto simula el rol de un MLOps Engineer, es decir, la combinación de un Data Engineer y Data Scientist, para la plataforma de videojuegos Steam. Para su desarrollo, se entregan unos datos y se solicita un Producto Mínimo Viable que muestre una API deployada en un servicio en la nube y la aplicación de un modelo de Machine Learning, por una lado, un análisis de sentimientos sobre los comentarios de los usuarios de los juegos y, por otro lado, la recomendación de juegos a partir de dar el id de un juego en particular.

## Contexto
Se plantea desde los propietarios de la plataforma Steam la necesidad de contar con los datos en una API para poder ser consumidos. Por otro lado existe la necesidad de poder realizar las consultas al modelo de recomendación para lo cual resulta necesario hacer un deploy de la API.

## Datos

Para este proyecto se proporcionaron tres archivos JSON:

* **australian_user_reviews.json** es un dataset que contiene los comentarios que los usuarios realizaron sobre los juegos que consumen, además de datos adicionales como si recomiendan o no ese juego, emoticones de gracioso y estadísticas de si el comentario fue útil o no para otros usuarios. También presenta el id del usuario que comenta con su url del perfil y el id del juego que comenta.

* **australian_users_items.json** es un dataset que contiene información sobre los juegos que juegan todos los usuarios, así como el tiempo acumulado que cada usuario jugó a un determinado juego.

* **output_steam_games.json** es un dataset que contiene datos relacionados con los juegos en sí, como los título, el desarrollador, los precios, características técnicas, etiquetas, entre otros datos.

## Descripcion del dataset
Para descargar el dataset original, se puede descargar del siguiente link. [Datasets](https://drive.google.com/drive/folders/1XrgahQxKIrEwvViS9NzGbTVBnPkQ-2EW?usp=sharing)


| **Columnas**         | **Descripcion**                                                   | **Ejemplo**                                                                                                                                                                           |
|------------------- |------------------------------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| publisher          | Content publisher                                                  | [Ubisoft, Dovetail Games - Trains, Degica]                                                                                                                                           |
| genres             | Content genre                                                      | [Action, Adventure, Racing, Simulation, Strategy]                                                                                                                                    |
| app_name           | Content name                                                       | [Warzone, Soundtrack, Puzzle Blocks]                                                                                                                                                 |
| title              | Content title                                                      | [The Dream Machine: Chapter 4 , Fate/EXTELLA - Sweet Room Dream, Fate/EXTELLA - Charming Bunny]                                                                                       |
| url                | Content publication URL                                            | [http://store.steampowered.com/app/761140/Lost_Summoner_Kitty/]                                                                                                                      |
| release_date       | Release date                                                       | [2018-01-04]                                                                                                                                                                         |
| tags               | Content tags                                                       | [Simulation, Indie, Action, Adventure, Funny, Open World, First-Person, Sandbox, Free to Play]                                                                                       |
| discount_price     | Discount price                                                     | [22.66, 0.49, 0.69]                                                                                                                                                                  |
| reviews_url        | Content reviews URL                                                | [http://steamcommunity.com/app/681550/reviews/?browsefilter=mostrecent&p=1]                                                                                                           |
| specs              | Specifications                                                     | [Multi-player, Co-op, Cross-Platform Multiplayer, Downloadable Content]                                                                                                              |
| price              | Content price                                                      | [4.99, 9.99, Free to Use, Free to Play]                                                                                                                                              |
| early_access       | Early access                                                       | [False, True]                                                                                                                                                                        |
| id                 | Unique content identifier                                          | [761140, 643980, 670290]                                                                                                                                                            |
| developer          | Developer                                                          | [Kotoshiro, Secret Level SRL, Poolians.com]                                                                                                                                         |
| metascore          | Metacritic score                                                   | [80, 74, 77, 75]                                                                                                                                                                    |
| user_id            | Unique user identifier                                             | [76561197970982479, evcentric, maplemage]                                                                                                                                            |
| user_url           | User profile URL                                                   | [http://steamcommunity.com/id/evcentric]                                                                                                                                             |
| reviews            | User review in Json format                                         | {'funny': '', 'posted': 'Posted September 8, 2013.','last_edited': '','item_id': '227300','helpful': '0 of 1 people (0%) found this review helpful','recommend': True,'review': "For a simple..."}                                       |                                                                                                                                                                                   |
| user_id            | Unique user identifier                                             | [76561197970982479, evcentric, maplemage]                                                                                                                                            |
| user_url           | User profile URL                                                   | [http://steamcommunity.com/id/evcentric]                                                                                                                                             |
| items              | User items in Json format                                          | {'item_id': '273350', 'item_name': 'Evolve Stage 2', 'playtime_forever': 58, 'playtime_2weeks': 0}                                                                                |


## Tareas Desarrolladas

### [ETL](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/ETL.ipynb)


* Se abrieron y leyeron los archivos de formato JSON **anidados**.
* Se guardaron en dataframes, **df_games**, **df_items** y **df_reviews**.
* Se hizo una limpieza general de los datos.
* Se creó un datafreme con todos las columnas a utilizar **df**.
* Se transformó la columna **price** a float y los valores de juegos gratis, pasaron a ser 0
* Se creó la columna **release_year** y **posted_year** a partir de **release_date** y **posted_year**.
* Se creó un segundo datadrame **df1**, para facilitar el código de las funciones.
* Se eliminaron nulos y columnas innecesarias para el análisis.
* Se guardó **df** y **df1** dentro de la carpeta [dataframe.](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/tree/main/dataframe)


### [EDA](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/EDA.ipynb)

Se aplicó la regla de los **3 sigmas** sobre las columna **Playtime_forever** y **price**. Tambien se revisaron las distintas columnas que se utilizaron en las funciones. No se realizó mayor cambio sobre los dataframes, ya que no se consideró necesario. Los análisis se realizaron en algunos casos sobre el dataframe **df** y otros sobre el **df1**, para mayor comodidad.

### [Funciones](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/funciones.ipynb)
Para el desarrollo de la API se decidió utilizar el framework FastAPI, creando las siguientes funciones:

+ def **developer( *desarrollador : str* )**:
    Debe devolver la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.
  
Ejemplo de retorno: {"Año: 2023 ,Cantidad de Items: 50 , Contenido Free: 27%}<br>
                    {"Año: 2022 ,Cantidad de Items: 45 , Contenido Free: 25%}
<br/>

+ def **userdata( *User_id : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, <br>
"Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
<br/>

+ def **UserForGenre( *genero : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
  
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,<br>
"Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
<br/>

+ def **best_developer_year( *año : int* )**:
   Debe devolver el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]
<br/>

+ def **developer_reviews_analysis( *desarrolladora : str* )**:
    Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

Ejemplo de retorno: {'Valve' : [Negative = 182, Positive = 278]}
<br/>

+ def **recomendacion_juego( *id de producto* )**: 
    Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

Ejemplo de retorno: {'Juegos recomendados a partir del juego juego_id': '6787990',<br>
                     'No 1': 'Snooker-online multiplayer snooker game!',<br>
                     'No 2': "Malzbie's Pinball Collection",<br>
                     'No 3': 'Zaccaria Pinball - Blackbelt Table',<br>
                     'No 4': 'Zaccaria Pinball - Bronze Membership',<br>
                     'No 5': 'Zaccaria Pinball - Cine Star Table'}<br>

<br/>

### [Sistema de Recomendación](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/Sistema_Recomendacion-ML.ipynb)

El modelo establece una relación item-item. Esto significa que dado un item_id, en función de qué tan similar sea al resto, se recomendarán artículos similares. La entrada es un juego y la salida es una lista de juegos recomendados.

Se utilizó una técnica de procesamiento de lenguaje natural (NLP) llamada TF-IDF (Term Frequency-Inverse Document Frequency) y el cálculo de similitud del coseno para analizar la similitud entre textos, en este caso, para analizar la similitud entre los géneros de los juegos del datafame df1_redu. Se tuvo que reducir la cantidad de filas del dataframe original df1, ya que en **render** ofrece poca capacidad de cómputo de manera gratuita.

Del siguiente link se puede descargar la matriz [cosine_sim](https://drive.google.com/file/d/18UzYTkwHRVFnN0S3mYILUKBE-BTQmS2j/view?usp=sharing) (cosine similarity) en formato parquet, la matriz esta entrenada con todos los datos.


### Deploy de la API

#### FastAPI

Para el deploy de la API de manera local, se seleccionó la plataforma Render. Para esto se siguieron estos pasos:

- Se creó el entorno virtual, dentro de la carpeta del proyecto **python -m venv fastapi-env**
- Se activó el entorno virtual **fastapi-env\Scripts\activate.bat**
- Se instaló los paquetes a utilizar **pip install fastapi**,**pip install uvicorn**, ETC
- Se creó el archivo **main.py**
- Se levantó el servidor **uvicorn main:app --reload**

![Fastapi](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/images/fastapi.png)

_Recomendaciones_: Si la salida produce un **null** o no se muestra parte del contenido, posiblemente sea la manera de mostrar el return de la función. Si la salida dice **Internal Error** probablemente la función no este corriendo, por falta de una librería o fallo en la misma.

_Nota_: Se omitió copiar la carpeta [Lib](https://drive.google.com/file/d/12WO9M0hQy5EvTKQTntB_Gi7SKPzzqu3Z/view?usp=sharing) detro del directorio [/fastapi-env](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/tree/main/fastapi-env), que contiene las librerías descargadas para el entorno virtual. Esto se hizo para ahorrar espacio en el Github. 

#### Render

Para el deploy de la API se seleccionó la plataforma Render que es una nube unificada para ejecutar aplicaciones y sitios web, permitiendo el despliegue automático desde GitHub. Para esto se siguieron estos pasos:

- Se debe crear una cuenta en la página [render.com](https://render.com/)
- Crear el archivo requirements.txt con las librerias a utilizar, se puede usar **python -m pip freeze**
- Ir a la página, y crear un web service
- Escoger en donde están los archivos del deploy, nuestro caso GitHub
- Pasar el link del reposiorio público con los archivos del deploy
- Dar nombre al deploy, llenar Runtime:**python3**, Start Command:**uvicorn main:app --host 0.0.0.0 --port 10000**
- Se escogió la versión gratis en nuestro caso.
- Se generó un servicio nuevo  en [render.com](https://render.com/), conectado al presente repositorio.
- Finalmente, el servicio queda corriendo en [Sistema de Recomendación Steam - API](https://proyecto-api-steam.onrender.com/)

![Render](https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API/blob/main/images/render1.png)

_Recomendaciones_: Se debe estar pendiente de la primera vez que se corre un repositorio en render, porque si da un error casi siempre sólo se muesta en la primera corrida, las siguientes veces no nuestra el error. Se debe tener en cuenta que la capacidad gratis es bastante limitada.

## Video

En este [video](https://drive.google.com/drive/folders/1IJHL48pwmgE-M0aLox7iKMWzsn3_whpG?usp=sharing) se explica brevemente este proyecto mostrando el funcionamiento de la API. <br>


## Requerimientos
- [Python](https://docs.python.org/es/3/library/index.html)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Render](https://render.com/)

## Autor
- José R. Guignan
- Mail: joserguignan@gmail.com
- Linkedin: [https://www.linkedin.com/in/jrguignan](https://www.linkedin.com/in/jrguignan)

