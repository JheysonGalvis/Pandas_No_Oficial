# Importamos la biblioteca pandas y la llamamos 'pd'
import pandas as pd

# Creamos una Serie de pandas usando una lista
psg_players_list = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messi'],  # Lista de jugadores
)

# Creamos un diccionario que asocia números de camiseta con nombres de jugadores
psg_dict = {1: 'Navas', 7: 'Mbappe', 10: 'Neymar', 30: 'Messi'}

# Creamos una Serie de pandas usando el diccionario
psg_players_dict = pd.Series(psg_dict)

# Imprimimos la Serie creada a partir del diccionario
print(psg_players_dict)

# Imprimimos el valor en la posición (índice) 7 de la Serie creada a partir del diccionario
print(psg_players_dict[7])
print(psg_players_dict[0:3])

# Diccionario con datos de jugadores
dict = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messi'],
        'Altura': [183.0, 170.0, 170.0, 165.0],
        'Goles': [2, 200, 150, 200]}

# Crear un DataFrame con el diccionario y índices personalizados
df = pd.DataFrame(dict, index=[1, 7, 10, 30])

# Imprimir el DataFrame
print(df)