#Funciones que se usaran en la API

#Importacion de las librerias
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#################################################################################################
#carga de dataframe
df1 = pd.read_csv(r'dataframe\df1.csv')
df = pd.read_csv(r'dataframe\df.csv')

#Matriz de similaridad del los cosenos
tfidf = TfidfVectorizer (stop_words="english")
tfidf_matrix = tfidf.fit_transform(df1['genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series (df1.index, index=df1['id']).drop_duplicates()

#################################################################################################
#Funcion Presentacion
def presentacion():
    '''
    Genera una página de presentación HTML para la API Steam de consultas de videojuegos.
    
    Returns:
    str: Código HTML que muestra la página de presentación.
    '''
    return '''
    <html>
        <head>
            <title>API Steam</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: #666;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <h1>API de consultas de videojuegos de la plataforma Steam</h1>
            <p>Bienvenido a la API de Steam donde se pueden hacer diferentes consultas sobre la plataforma de videojuegos.</p>
            <p>INSTRUCCIONES:</p>
            <p>Escriba <span style="background-color: lightgray;">/docs</span> a continuación de la URL actual de esta página para interactuar con la API</p>
            <p> Visita mi perfil en <a href="https://www.linkedin.com/in/ingambcarlapezzone/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin"></a></p>
            <p> El desarrollo de este proyecto esta en <a href="https://github.com/IngCarlaPezzone/PI1_MLOps_videojuegos"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
        </body>
    </html>
    '''

###########################################################################################################
#Funcion 1

def developer( desarrollador : str ):

      #daraframe filtrando el desarrollador, agrupado por ano y contando los juegos por ano
      df_total = df1[df1['developer']==desarrollador].groupby(['Añio'])['id'].count()

      #daraframe filtrando el desarrollador y juego free,  agrupado por año y contando los juegos por año
      df_free = df1[(df1['developer']==desarrollador) & (df1['price']==0)].groupby(['Añio'])['id'].count()

      #Se crea une el dataframe total con los que salen gratis
      df_nuevo = pd.merge(df_total,df_free, on='Añio', how='left' )

      #Llena con ceros los valores NAN
      df_nuevo.fillna(0, inplace=True)

      #Crea la columna de porcentaje de contenido gratis
      df_nuevo['Contenido Free'] = round(df_nuevo['id_y']*100/df_nuevo['id_x'],0)

      #Borra la columna id_y
      df_nuevo.drop(['id_y'], axis=1, inplace=True)

      #Renombra la columna id_x
      df_nuevo.rename(columns={ 'id_x': 'Cantidad de Items'}, inplace=True)

      #Transforma lo que arroja el groupby por un dataframe "real"
      df_nuevo = df_nuevo.reset_index()

      #transforma la columna contenido Free a integer
      df_nuevo['Contenido Free'] = df_nuevo['Contenido Free'].astype('int')

      #Agrega porcentaje % a la columna contenido free
      df_nuevo['Contenido Free'] = df_nuevo['Contenido Free'].map(lambda x: f'{x}%')

      #Quita los indices naturales de los dataframe que aparecen a la izquierda
      #Pense se mostraba un datafame
      #print(df_nuevo.to_string(index=False))

      #Pregunte como se deberia mostrar la informacion y me dijeron que lo hiciera en un diccionario
      lista = []
      for i in range(0, len(df_nuevo)):
            dic={'Añio':df_nuevo.iloc[i][0] ,
                 'Cantidad de Items': df_nuevo.iloc[i][1] , 
                 'Contenido Free': df_nuevo.iloc[i][2] }
            
            lista.append(dic)

      return lista

#############################################################################################################
#Funcion 2

def userdata( User_id : str ):

    #Filtra los datos del user_id
    df_nuevo = df[df['user_id']== User_id]

    #Dinero gastado por el usuario
    Gasto = df_nuevo['price'].sum()

    #Cantidad de items comprados
    n_items = df_nuevo['item_name'].count()

    #Cantida de Juegos recomendados
    n_reco = df_nuevo['recommend'].sum()

    #Muestra los resultados en un diccionario y con el formato adecuado
    dic = {"Usuario X" : User_id, "Dinero gastado": '{:,.2f} USD'.format(Gasto), 
         "% de recomendación": '{:,.1f} %'.format(n_reco*100/n_items),
         "cantidad de items": n_items}

    return print(dic)

############################################################################################################
#Funcion 3

def UserForGenre(genero : str):
    genero = genero.lower()
    genero = genero.title()
    max_horas_ano = None
    max_horas = 0
    max_user = None  # Nuevo: mantener un registro del usuario con más horas jugadas
    horas_por_ano = {}
    
    for index, row in df.iterrows():
        if genero in row['genres']:

            # Obtener el año de la fecha de lanzamiento
            year = row['release_year']
            
            # Sumar las horas jugadas
            horas_jugadas = row['playtime_forever']
            
            if year not in horas_por_ano:
                horas_por_ano[year] = 0
                
            horas_por_ano[year] += horas_jugadas
            
            if horas_por_ano[year] > max_horas:
                max_horas = horas_por_ano[year]
                max_horas_ano = year
                max_user = row['item_id_x']
                
    #Para mostrar de manera adecuada
    lista=[]
    
    for i,k in enumerate(horas_por_ano):
        dic = {'Año':k, 'Horas':horas_por_ano[k]}
        lista.append(dic)            
    
    res = {
        
        "Usuario con más horas jugadas para Género X": max_user, 
        "Horas jugadas": lista
         
    }
            
    return res

#########################################################################################################
#Funcion 4

def best_developer_year(year: int):
    # Verificar si el año es igual a -1 y mostrar un mensaje personalizado
    if year == -1:
        return "El año ingresado es -1, lo cual no es válido."

    # Verificar que el año sea un número entero
    if not isinstance(year, int):
        return "El año debe ser un número entero."

    # Verificar que el año ingresado esté en la columna 'year_integer'
    if year not in df['posted_year'].unique():
        return "El año no se encuentra en la columna 'posted_year'."

    # Filtrar el dataset para obtener solo las filas correspondientes al año dado
    juegos_del_año = df[df['posted_year'] == year]

    # Calcular la cantidad de recomendaciones para cada juego
    recomendaciones_por_juego = juegos_del_año.groupby('developer')['recommend'].sum().reset_index()

    # Ordenar los juegos por la cantidad de recomendaciones en orden descendente
    juegos_ordenados = recomendaciones_por_juego.sort_values(by='recommend', ascending=False)

    # Tomar los tres primeros lugares
    primer_puesto = juegos_ordenados.iloc[0]['developer']
    segundo_puesto = juegos_ordenados.iloc[1]['developer']
    tercer_puesto = juegos_ordenados.iloc[2]['developer']

    # Crear el diccionario con los tres primeros lugares
    top_tres = [
        {"Puesto 1": primer_puesto},
        {"Puesto 2": segundo_puesto},
        {"Puesto 3": tercer_puesto}
    ]

    return top_tres

#############################################################################################################
#Funcion Analisis de Sentimietno

def developer_reviews_analysis(desarrollador : str):
    # Filtrar el DataFrame por el año proporcionado
    df_filtered = df[df['developer'] == desarrollador]
    
    # Contar la cantidad de registros por cada análisis de sentimiento
    resultados = df_filtered['sentiment_analysis'].value_counts()
    
    # Si algún análisis de sentimiento está ausente, añádelo con 0
    for sentimiento in ['Negative', 'Positive']:
        if sentimiento not in resultados:
            resultados[sentimiento] = 0
    
    # Almacenar los resultados en una lista de tuplas
    resultados_lista = [(sentimiento, cantidad) for sentimiento, cantidad in resultados.items()]
    lista = ['Negative = '+str(resultados.iloc[1]),  'Positive = '+str(resultados.iloc[0]) ]
    

    #print(*lista, sep=",")
    return {desarrollador : lista}

#########################################################################################################
#Funcion Sistema de Recomendacion

def developer_reviews_analysis(desarrollador : str):
    # Filtrar el DataFrame por el año proporcionado
    df_filtered = df[df['developer'] == desarrollador]
    
    # Contar la cantidad de registros por cada análisis de sentimiento
    resultados = df_filtered['sentiment_analysis'].value_counts()
    
    # Si algún análisis de sentimiento está ausente, añádelo con 0
    for sentimiento in ['Negative', 'Positive']:
        if sentimiento not in resultados:
            resultados[sentimiento] = 0
    
    # Almacenar los resultados en una lista de tuplas
    resultados_lista = [(sentimiento, cantidad) for sentimiento, cantidad in resultados.items()]
    lista = ['Negative = '+str(resultados.iloc[1]),  'Positive = '+str(resultados.iloc[0]) ]
    

    #print(*lista, sep=",")
    return {desarrollador : lista}