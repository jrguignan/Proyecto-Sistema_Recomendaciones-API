# Importaciones
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
import funciones_api as fa

import importlib
importlib.reload(fa)

# Se instancia la aplicación
app = FastAPI()

# Funciones
@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Presentación"])
def Presentacion():
    '''
    Página de inicio -  Muestra una presentación.

    Returns:
    HTMLResponse: Respuesta HTML que muestra la presentación.

    Haga clik en "Try it out" y luego en "Execute" y scrollear hasta "Responses" -> "Response body"
    
    '''
    return fa.presentacion()

#######################
#Funcion 1

@app.get(path = '/developer',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del genero en el box abajo y de click en "Execute".<br>
                        3. Scrollear hasta "Responses" -> "Response body" <br>
                        4. Muestra: Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.
                        </font>
                        """,
         tags=["Funciones"])
def developer(desarrollador : str = Query(..., 
                            description="Desarollador de videojuego", 
                            example='Valve')):
    return fa.developer(desarrollador)

############################
#Funcion 2

@app.get(path = '/userdata',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del genero en el box abajo y de click en "Execute".<br>
                        3. Scrollear hasta "Responses" -> "Response body" <br>
                        4. Muestra: Cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
                        </font>
                        """,
         tags=["Funciones"])
def userdata(User_id : str = Query(..., 
                            description="User_id", 
                            example='76561197970982479')):
    return fa.userdata(User_id)

###########################
#Funcion 3
@app.get(path = '/UserForGenre',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del genero en el box abajo y de click en "Execute".<br>
                        3. Scrollear hasta "Responses" -> "Response body" <br>
                        4. Muestra: El usuario que acumula más horas jugadas para el género dado y la suma de horas jugadas por año de lanzamiento.
                        </font>
                        """,
         tags=["Funciones"])
def UserForGenre(genero : str = Query(..., 
                            description="Genero de videojuego", 
                            example='Action')):
    return fa.UserForGenre(genero)

############################
#Funcion 4
@app.get(path = '/best_developer_year',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del genero en el box abajo y de click en "Execute".<br>
                        3. Scrollear hasta "Responses" -> "Response body" <br>
                        4. Muestra: El  top 3 de desarrolladores con juegos más recomendados por usuarios para el año dado.
                        </font>
                        """,
         tags=["Funciones"])
def best_developer_year(year : int = Query(..., 
                            description="Año", 
                            example='2011')):
    return fa.best_developer_year(year)

#############################
#Funcion 5
@app.get(path = '/developer_reviews_analysis',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del genero en el box abajo y de click en "Execute".<br>
                        3. Scrollear hasta "Responses" -> "Response body" <br>
                        4. Muestra: El analisis de sentimiento categorizado de la desarrolladora de videojuegos dada.
                        </font>
                        """,
         tags=["Analisis de Sentimiento"])
def developer_reviews_analysis(desarrollador : str = Query(..., 
                            description="Desarrollador de videojuego", 
                            example='Valve')):
    return fa.developer_reviews_analysis(desarrollador)

######################################
#Recomendaciones
#Funcion 1
@app.get(path = '/recomendacion_juego',
          description = """ <font color="blue">
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el nombre del genero en el box abajo y de click en "Execute".<br>
                        3. Scrollear hasta "Responses" -> "Response body" <br>
                        4. Muestra: Recomienda 5 juegos a partir del id de un juego dado.
                        </font>
                        """,
         tags=["Sistema Recomendación Item-Item"])
def recomendacion_juego(juego_id : int = Query(..., 
                            description="ID del Videojuego", 
                            example='670290')):
    return fa.recomendacion_juego(juego_id)

