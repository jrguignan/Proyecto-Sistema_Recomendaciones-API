#Funciones que se usaran en la API

#Importacion de las librerias
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#################################################################################################
#carga de dataframe
df1 = pd.read_csv(r"dataframe/df1.csv")
df1_redu = pd.read_csv(r"dataframe/df1_redu.csv")
df = pd.read_csv(r"dataframe/df.csv")


#Matriz de similaridad del los cosenos
tfidf = TfidfVectorizer (stop_words="english")
tfidf_matrix = tfidf.fit_transform(df1_redu['genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

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
            <p>Instrucciones:</p>
            <p>Escriba <span style="background-color: lightgray;">/docs</span> a continuación de la URL actual de esta página para interactuar con la API</p>
            <p> El siguiente repositorio contiene el código del proyecto <a href="https://github.com/jrguignan/Proyecto-Sistema_Recomendaciones-API"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
        </body>
    </html>
    '''

###########################################################################################################
#Funcion 1

def developer(desarrollador : str):
      df_total = df1[df1['developer']==desarrollador].groupby(['Añio'])['id'].count()
      df_free = df1[(df1['developer']==desarrollador) & (df1['price']==0)].groupby(['Añio'])['id'].count()
      df_nuevo = pd.merge(df_total,df_free, on='Añio', how='left' )
      df_nuevo.fillna(0, inplace=True)
      df_nuevo['Contenido Free'] = round(df_nuevo['id_y']*100/df_nuevo['id_x'],0)
      df_nuevo.drop(['id_y'], axis=1, inplace=True)
      df_nuevo.rename(columns={ 'id_x': 'Cantidad de Items'}, inplace=True)
      df_nuevo = df_nuevo.reset_index()
      df_nuevo['Contenido Free'] = df_nuevo['Contenido Free'].astype('int')
      df_nuevo['Contenido Free'] = df_nuevo['Contenido Free'].map(lambda x: f'{x}%')
      dic = df_nuevo.to_dict('list')
      dic_return = {} 

      for i in range(0, len(df_nuevo)):
          dic1 = {'Año': dic['Añio'][i], 
                  'Cantidad de Items': dic['Cantidad de Items'][i], 
                  'Contenido Free': dic['Contenido Free'][i]}
          dic_return[i] = dic1

      return dic_return


#############################################################################################################
#Funcion 2

def userdata(User_id : str):
    df_nuevo = df[df['user_id']== User_id]
    gasto = str(round(df_nuevo['price'].sum(),2))+' USD'
    n_items = df_nuevo['item_name'].count()
    n_reco = df_nuevo['recommend'].sum()
    por_reco = str(n_reco*100/n_items) + '%'

    return {"Usuario X" : str(User_id), 
           "Dinero gastado": str(gasto), 
           "% de recomendación": str(por_reco),
           "cantidad de items": int(n_items)  
           }

############################################################################################################
#Funcion 3

def UserForGenre(genero : str):
    genero = genero.lower()
    genero = genero.title()
    max_horas_ano = None
    max_horas = 0
    max_user = None  
    horas_por_ano = {}
    
    for index, row in df.iterrows():
        if genero in row['genres']:

            year = row['release_year']
            horas_jugadas = row['playtime_forever']
            
            if year not in horas_por_ano:
                horas_por_ano[year] = 0
                
            horas_por_ano[year] += horas_jugadas
            
            if horas_por_ano[year] > max_horas:
                max_horas = horas_por_ano[year]
                max_horas_ano = year
                max_user = row['item_id_x']        
    
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
    if year == -1:
        return "El año ingresado es -1, lo cual no es válido."

    if not isinstance(year, int):
        return "El año debe ser un número entero."

    if year not in df['posted_year'].unique():
        return "El año no se encuentra en la columna 'posted_year'."

    juegos_del_año = df[df['posted_year'] == year]
    recomendaciones_por_juego = juegos_del_año.groupby('developer')['recommend'].sum().reset_index()
    juegos_ordenados = recomendaciones_por_juego.sort_values(by='recommend', ascending=False)

    primer_puesto = juegos_ordenados.iloc[0]['developer']
    segundo_puesto = juegos_ordenados.iloc[1]['developer']
    tercer_puesto = juegos_ordenados.iloc[2]['developer']

    top_tres = [
        {"Puesto 1": primer_puesto},
        {"Puesto 2": segundo_puesto},
        {"Puesto 3": tercer_puesto}
    ]

    return top_tres

#############################################################################################################
#Funcion Analisis de Sentimiento

def developer_reviews_analysis(desarrollador : str):
    df_filtered = df[df['developer'] == desarrollador]
    resultados = df_filtered['sentiment_analysis'].value_counts()
    
    for sentimiento in ['Negative', 'Positive']:
        if sentimiento not in resultados:
            resultados[sentimiento] = 0
    
    resultados_lista = [(sentimiento, cantidad) for sentimiento, cantidad in resultados.items()]
    lista = ['Negative = '+str(resultados.iloc[1]),  'Positive = '+str(resultados.iloc[0]) ]
    
    return {desarrollador : lista}

#########################################################################################################
#Funcion Sistema de Recomendacion

def recomendacion_juego (juego_id : int):

    indices = pd.Series (df1_redu.index, index=df1_redu['id']).drop_duplicates()
    idx = indices[juego_id]

    sim_scores = list(enumerate (cosine_sim[idx]))
    sim_scores = sorted (sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores [1:11]
    game_indices = [i[0] for i in sim_scores]

    lista = list(df1_redu['id'].iloc[game_indices])
    lista = lista[0:10]
    
    a=None
    lista_juegos=[]
    for i,l in enumerate(lista):
        if not(l in lista_juegos) and (l != juego_id):
           lista_juegos.append(lista[i])
    
    return {
          'Juegos recomendados a partir del juego' : str(juego_id), 
          'No 1': str(df1_redu[df1_redu['id']==lista_juegos[0]].iloc[0][1]),
          'No 2': str(df1_redu[df1_redu['id']==lista_juegos[1]].iloc[0][1]),
          'No 3': str(df1_redu[df1_redu['id']==lista_juegos[2]].iloc[0][1]),
          'No 4': str(df1_redu[df1_redu['id']==lista_juegos[3]].iloc[0][1]),
          'No 5': str(df1_redu[df1_redu['id']==lista_juegos[4]].iloc[0][1])
          }
