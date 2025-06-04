from monticulo_binario import MonticuloBinario as ColaPrioridad
from grafo import Vertice as v
from grafo import Grafo
import sys


def prim(G, inicio):
    cp = ColaPrioridad()
    visitados = set()
    
    # Inicializar todas las distancias a infinito
    for v in G:
        v.asignar_distancia(sys.maxsize)
        v.asignar_predecesor(None)
    
    # Configurar vértice inicial
    inicio.asignar_distancia(0)
    cp.construirMonticulo([(v.obtener_distancia(), v) for v in G])
    
    while not cp.estaVacio():
        vertice_actual = cp.eliminarMin()[1]
        visitados.add(vertice_actual)
        
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            if vertice_siguiente not in visitados:
                nuevo_costo = vertice_actual.obtener_ponderacion(vertice_siguiente)
    
                if nuevo_costo < vertice_siguiente.obtener_distancia():
                    vertice_siguiente.asignar_predecesor(vertice_actual)
                    vertice_siguiente.asignar_distancia(nuevo_costo)
                    cp.decrementarClave(vertice_siguiente, nuevo_costo)
