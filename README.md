![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)


![henry](https://camo.githubusercontent.com/3cb94d41ac073b2d10b8c7423e5a54e2928610821a2837883e4a9a56052f37ab/68747470733a2f2f643331757a386c77666d796e38672e636c6f756466726f6e742e6e65742f4173736574732f6c6f676f2d68656e72792d77686974652d6c672e706e67)
# Proyecto Individual  1 
## Data Science & Machine Learning Operations (MLOps) 


<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

## Introducción

Este proyecto simula el rol de un MLOps Engineer, es decir, la combinación de un Data Engineer y Data Scientist, para la plataforma de videojuegos Steam. Para su desarrollo, se entregan unos datos y se solicita un Producto Mínimo Viable que muestre una API deployada en un servicio en la nube y la aplicación de dos modelos de Machine Learning, por una lado, un análisis de sentimientos sobre los comentarios de los usuarios de los juegos y, por otro lado, la recomendación de juegos a partir de dar el nombre de un juego o a partir de los gustos de un usuario en particular.

##Contexto
Se plantea desde los propietarios de la plataforma Steam la necesidad de contar con los datos en una API para poder ser consumidos. Por otro lado existe la necesidad de poder realizar las consultas al modelo de recomendación para lo cual resulta necesario hacer un deploy de la API.

## Datos

Para este proyecto se proporcionaron tres archivos JSON:

* **australian_user_reviews.json** es un dataset que contiene los comentarios que los usuarios realizaron sobre los juegos que consumen, además de datos adicionales como si recomiendan o no ese juego, emoticones de gracioso y estadísticas de si el comentario fue útil o no para otros usuarios. También presenta el id del usuario que comenta con su url del perfil y el id del juego que comenta.

* **australian_users_items.json** es un dataset que contiene información sobre los juegos que juegan todos los usuarios, así como el tiempo acumulado que cada usuario jugó a un determinado juego.

* **output_steam_games.json** es un dataset que contiene datos relacionados con los juegos en sí, como los título, el desarrollador, los precios, características técnicas, etiquetas, entre otros datos.

## Descripcion del dataset
Para descargar el dataset original, se puede descargar del siguiente link. [Datasets](https://drive.google.com/drive/folders/1XrgahQxKIrEwvViS9NzGbTVBnPkQ-2EW?usp=sharing)


| **Column**         | **Description**                                                   | **Example**                                                                                                                                                                           |
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


## Tareas desarrolladas

### ETL

* Se abrieron y leyeron los archivos de formato JSON en líneas separadas.
* Se analizaron y almacenaron en una lista.
* Se tomó la lista de objetos JSON, se concatenaron en un único DataFrame.
* Se desanidaron columnas anidadas.
* Se eliminaron nulos y columnas innecesarias para el análisis.
* Se corrigió formato de fechas.
* Se corrigió formato Mayúsculas y Minúsculas
* En el archivo Reviews.json, se utilizó la biblioteca NLTK (***Natural Language Toolkit***) y la función **SentimentIntensityAnalyzer** para aplicar análisis de sentimiento y clasificar la columna 'Reviews', que contiene reseñas realizadas por los usuarios de los juegos, en positivas, neutrales y negativas.

### EDA

Los conjuntos de datos tenían algunos aspectos que corregir relacionados con variables numéricas.La columna playtime_forever tuvo algunos valores atípicos con cantidades irreales de horas jugadas para algunos usuarios, las cantidades fueron corregidas

### API
Para el desarrolo de la API se decidió utilizar el framework FastAPI, creando las siguientes funciones:

+ def **PlayTimeGenre( *`genero` : str* )**:
    Debe devolver `año` con mas horas jugadas para dicho género.
  
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
			     "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

+ def **UsersRecommend( *`año` : int* )**:
   Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **UsersWorstDeveloper( *`año` : int* )**:
   Devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **sentiment_analysis( *`empresa desarrolladora` : str* )**:
    Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total 
    de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 

Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}

<br/>

### Machine Learning

El modelo establece una relación item-item. Esto significa que dado un item_id, en función de qué tan similar sea al resto, se recomendarán artículos similares. Aquí, la entrada es un juego y la salida es una lista de juegos recomendados.

 El método de aprendizaje automático utilizado es K-Neighbours. No es el mejor método para abordar los conjuntos de datos y parte de este proyecto se centra en eso. Debido a que el proyecto debe implementarse en Render, la memoria RAM disponible es limitada y lo importante aquí era comprender la diferencia entre los diferentes modelos de Machine Learning. Anteriormente, probé árboles de decisión y procesamiento de lenguaje natural usando similitud de coseno.



### Deploy

Para el deploy de la API se seleccionó la plataforma Render que es una nube unificada para crear y ejecutar aplicaciones y sitios web, permitiendo el despliegue automático desde GitHub. Para esto se siguieron estos pasos:

- Se generó un API de manera local con FastAPI.
- Se generó un servicio nuevo  en `render.com`, conectado al presente repositorio.
- Finalmente, el servicio queda corriendo en [proyecto-api_steam](https://proyecto-api-steam.onrender.com/)


#### Requerimientos
- [Python](https://docs.python.org/es/3/library/index.html)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Render](https://render.com/)

#### Autor
- José R. Guignan
- Mail: joserguignan@gmail.com
- Linkedin:[linkedin](www.linkedin.com/in/jrguignan)

