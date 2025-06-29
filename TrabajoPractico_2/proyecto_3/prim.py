from monticulo_binario import MonticuloBinario as ColaPrioridad
from grafo import Vertice as v
from grafo import Grafo
import sys


def prim(G, inicio):
    cp = ColaPrioridad()
    visitados = set() #conjunto para almacenar los vértices visitados sin suplicados
    
    # Inicializar distancias y predecesores de los vértices
    for v in G:
        v.asignar_distancia(sys.maxsize) # Inicializar todas las distancias a infinito
        v.asignar_predecesor(None)  #el predecesor es None al inicio
    
    # Configurar vértice inicial
    inicio.asignar_distancia(0)  
    cp.construirMonticulo([(v.obtener_distancia(), v) for v in G]) #se crea un montículo con las distancias de los vértices
    
    while not cp.estaVacio():  #minetras no este vacío el montículo
        vertice_actual = cp.eliminarMin()[1]  #se obtiene el vertice del inicio(con menor distancia)
        visitados.add(vertice_actual)  #se agrega a los visitados

        for vertice_siguiente in vertice_actual.obtener_conexiones(): #se obtienen los vertices adyac. al actual
            if vertice_siguiente not in visitados: #si el siguiente no ha sido visitado
                nuevo_costo = vertice_actual.obtener_ponderacion(vertice_siguiente) # se calcula el costo de la arista
    
                if nuevo_costo < vertice_siguiente.obtener_distancia(): #si el nuevo costo es menor a la distancia del adyacente
                    vertice_siguiente.asignar_predecesor(vertice_actual) # se asigna el predecesor al vertice siguiente
                    vertice_siguiente.asignar_distancia(nuevo_costo) #se le asigna a su vez una distanncia=nuevo costo
                    cp.decrementarClave(vertice_siguiente, nuevo_costo) #se infiltra el vértice con la nueva distancia
