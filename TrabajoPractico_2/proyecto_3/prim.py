from monticulo_binario import MonticuloBinario as ColaPrioridad
from grafo import Vertice as v
#from grafo import asignar_distancia, asignar_predecesor, obtener_distancia, obtener_predecesor, obtener_conexiones, obtener_ponderacion, obtener_clave
from grafo import Grafo
import sys


def prim(G, inicio):
    cp= ColaPrioridad()
    for v in G:
        v.asignar_distancia(sys.maxsize) # inicializo distancia a infinito
        v.asignar_predecesor(None) 
    inicio.asignar_distancia(0)
    cp.construirMonticulo([(v.obtener_distancia(), v) for v in G])
    while not cp.estaVacio():
        vertice_actual = cp.eliminarMin()[1]
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_ponderacion(vertice_siguiente) # comienza función de relajación
            
            print(f"Evaluando arista {vertice_actual.obtener_id()} -> {vertice_siguiente.obtener_id()} con costo {nuevo_costo}")
            #if cp.contiene(vertice_siguiente) and
            if nuevo_costo < vertice_siguiente.obtener_distancia():
                print(f"Relajando arista {vertice_actual.obtener_id()} -> {vertice_siguiente.obtener_id()} con costo {nuevo_costo}")
                vertice_siguiente.asignar_predecesor(vertice_actual) 
                print(f"Actualizando vertice {vertice_siguiente.obtener_id()} con predecesor {vertice_actual.obtener_id()} y costo {nuevo_costo}")
                vertice_siguiente.asignar_distancia(nuevo_costo) # actualizo distancia
                cp.decrementarClave(vertice_siguiente, nuevo_costo) #actualizo cola de prioridad



if __name__ == "__main__":
    g = Grafo()
    g.agregar_aristas('A', 'B', 1)
    g.agregar_aristas('A', 'C', 3)
    g.agregar_aristas('B', 'C', 1)
    g.agregar_aristas('B', 'D', 4)
    
    prim(g, g.obtener_vertice('A'))
    for v in g:
        print(f"Vertice: {v.obtener_id()}, Predecesor: {v.obtener_predecesor().obtener_id() if v.obtener_predecesor() else None}, Distancia: {v.obtener_distancia()}")

    