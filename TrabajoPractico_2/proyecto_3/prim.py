from monticulo_binario import MonticuloBinario as ColaPrioridad
from grafo import Vertice as v
from grafo import Grafo
import sys


def prim(G, inicio):
    cp= ColaPrioridad()
    for v in G:
        v.asignar_distancia(sys.maxsize) # inicializo distancia a infinito
        v.asignar_predecesor(None) 
    inicio.asignar_distancia(0)
    cp.construirMonticulo((v.obtener_distancia(), v) for v in G)
    
    while not cp.estaVacio():
        vertice_actual = cp.eliminarMin()[1]
        for vertice_siguiente in vertice_actual.obtener_conexiones():
            nuevo_costo = vertice_actual.obtener_distancia() + vertice_actual.obtener_ponderacion(vertice_siguiente)
            # comienza función de relajación
            
            ####prueba de funcionamiento
            # print(f"Evaluando arista {vertice_actual.obtener_id()} -> {vertice_siguiente.obtener_id()} con costo {nuevo_costo}")
            # print(f"Vertice: {v.obtener_id()}, Predecesor: {v.obtener_predecesor().obtener_id() if v.obtener_predecesor() else None}, Distancia: {v.obtener_distancia()}")
            
            if cp.contiene(vertice_siguiente) and nuevo_costo < vertice_siguiente.obtener_distancia():
                ####
                # print(f"Relajando arista {vertice_actual.obtener_id()} -> {vertice_siguiente.obtener_id()} con costo {nuevo_costo}")
                vertice_siguiente.asignar_predecesor(vertice_actual) 
                ####
                #print(f"Actualizando vertice {vertice_siguiente.obtener_id()} con predecesor {vertice_actual.obtener_id()} y costo {nuevo_costo}")
                vertice_siguiente.asignar_distancia(nuevo_costo) # actualizo distancia
                cp.decrementarClave(vertice_siguiente, nuevo_costo) #actualizo cola de prioridad



if __name__ == "__main__":
    grafo = Grafo()
    # Crear el grafo y agregar los vértices
    aldeas = [['Aldea1', 'Aldea2', 5], ['Aldea1', 'Aldea3', 10], ['Aldea2', 'Aldea3', 2], ['Aldea2', 'Aldea4', 3], ['Aldea3', 'Aldea4', 1]]
    for aldea in aldeas:
        grafo.agregar_vertices(aldea[0])
        grafo.agregar_vertices(aldea[1])
        grafo.agregar_aristas(aldea[0], aldea[1], aldea[2])
    # Ejecutar el algoritmo de Prim
    prim(grafo, grafo.obtener_vertice('Aldea1'))
    # Imprimir los resultados
    for v in grafo:
        predecesor = v.obtener_predecesor().obtener_id() if v.obtener_predecesor() else None
        print(f"Vértice: {v.obtener_id()}, Predecesor: {predecesor}, Distancia: {v.obtener_distancia()}")
