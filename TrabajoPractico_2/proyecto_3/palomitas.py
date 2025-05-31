from prim import prim 
from listaaldeas import aldeas
from grafo import Grafo
from grafo import Vertice


   
grafo= Grafo()
for i in range(len(aldeas)):
    grafo.agregar_vertices(i)
    grafo.lista_vertices    
    #print(grafo.obtener_vertice(i))

for aldea in aldeas:
    grafo.agregar_aristas(aldea[0],aldea[1],aldea[2])
    #print(grafo.obtener_vertice(aldea))


for i in range(len(aldeas)):
    print(grafo.obtener_vertice(i))

print(" ")
print(" ")
print(" ")
print(" ")
