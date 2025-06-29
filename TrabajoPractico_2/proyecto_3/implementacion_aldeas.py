from grafo import Grafo
from prim import prim

# Leer archivo y crear aldeas
aldeas = []
aldeas_nombre = []
with open("aldeas.txt","r") as archivo: #lee el archivo
    for linea in archivo:
        linea = linea.strip("\n").split(",") # elimina el salto de línea y separa por comas
        aldea_inicial = linea[0].strip() # guarda el nombre de la aldea origen
        aldea_final = linea[1].strip() # guarda el nombre de la aldea destino
        distancia = int(linea[2]) # guarda la distancia entre aldeas y transforma a entero
        aldeas.append([aldea_inicial, aldea_final, distancia]) 
        aldeas_nombre.append([aldea_inicial]) 
        
aldeas_norep=[] # lista para almacenar aldeas sin repetición
# Eliminar aldeas repetidas
for aldea in aldeas_nombre:
            if aldea not in aldeas_norep: # verifica si la aldea ya está en la lista y la agrega si no está
                aldeas_norep.append(aldea)
            else:
                  continue # si ya está, continúa con la siguiente aldea

aldeas_nombre_ord= sorted(aldeas_norep, key = lambda x:x[0], reverse = False) # ordena las aldeas alfabéticamente
                                            #utiliza lambda para ordenar por el primer elemento de cada sublista


print(f"Las aldeas iniciales ordenadas alfabéticamente y sin repetición son:")

for aldea in aldeas_nombre_ord:
    print(f"* {aldea[0]}")
print(" ")
print("*-"*30)

# Crea grafo
grafo = Grafo()
vertices_unicos = set() # conjunto para almacenar los vértices sin repetición

# Agrega vértices
for aldea in aldeas: 
    vertices_unicos.add(aldea[0]) # aldea inicial
    vertices_unicos.add(aldea[1]) # aldea final

for vertice in vertices_unicos:
    grafo.agregar_vertices(vertice) # agrega cada aldea como un vértice en el grafo

# Agrega aristas
for aldea in aldeas:
    grafo.agregar_aristas(aldea[0], aldea[1], aldea[2]) # agrega una arista entre aldeas con su distancia

# Ejecuta Prim desde Peligros
vertice_inicial = grafo.obtener_vertice('Peligros') # obtiene el vértice inicial (Peligros)
prim(grafo, vertice_inicial) 

# Muestra resultados
print("\nÁrbol de expansión mínimo desde Peligros: ")
print("  ")
for v in grafo:
    predecesor = v.obtener_predecesor() # obtiene el predecesor del vértice actual
    if predecesor: # si el vértice tiene un predecesor
        print(f"Aldea: {v.obtener_id()} recibe noticia de: {predecesor.obtener_id()}") # muestra la conexión entre aldeas
    elif v.obtener_id() == 'Peligros': # si es el vértice inicial
        print(f"Aldea: Peligros es el origen")

# Calcular distancia total
suma_distancias = sum(v.obtener_distancia() for v in grafo if v.obtener_predecesor()) 
                      # suma las distancias de los vértices que tienen un predecesor
print(f"\n* Distancia total recorrida: {suma_distancias}")






