from grafo import Grafo
from prim import prim

# Leer archivo y crear aldeas
aldeas = []
aldeas_nombre = []
with open("aldeas.txt","r") as archivo:
    for linea in archivo:
        linea = linea.strip("\n").split(",")
        aldea_inicial = linea[0].strip()
        aldea_final = linea[1].strip()
        distancia = int(linea[2])
        aldeas.append([aldea_inicial, aldea_final, distancia])
        aldeas_nombre.append([aldea_inicial])
        
aldeas_norep=[]
for aldea in aldeas_nombre:
            if aldea not in aldeas_norep:
                aldeas_norep.append(aldea)
            else:
                  continue 

aldeas_nombre_ord= sorted(aldeas_norep, key = lambda x:x[0], reverse = False)

print(f"Las aldeas iniciales ordenadas alfabéticamente y sin repetición son:")

for aldea in aldeas_nombre_ord:
    print(f"* {aldea[0]}")
print(" ")
print("*-"*30)

# Crear grafo
grafo = Grafo()
vertices_unicos = set()

# Agregar vértices
for aldea in aldeas:
    vertices_unicos.add(aldea[0])
    vertices_unicos.add(aldea[1])

for vertice in vertices_unicos:
    grafo.agregar_vertices(vertice)

# Agregar aristas
for aldea in aldeas:
    grafo.agregar_aristas(aldea[0], aldea[1], aldea[2])

# Ejecutar Prim desde Peligros
vertice_inicial = grafo.obtener_vertice('Peligros')
prim(grafo, vertice_inicial)

# Mostrar resultados
print("\nÁrbol de expansión mínimo desde Peligros: ")
print("  ")
for v in grafo:
    predecesor = v.obtener_predecesor()
    if predecesor:
        print(f"Aldea: {v.obtener_id()} recibe noticia de: {predecesor.obtener_id()}")
    elif v.obtener_id() == 'Peligros':
        print(f"Aldea: Peligros es el origen")

# Calcular distancia total
suma_distancias = sum(v.obtener_distancia() for v in grafo if v.obtener_predecesor())
print(f"\n* Distancia total recorrida: {suma_distancias}")






