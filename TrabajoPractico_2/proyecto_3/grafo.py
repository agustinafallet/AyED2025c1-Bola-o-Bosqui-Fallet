import sys

class Vertice:
    def __init__(self, clave):
        self.id= clave
        self.conectadoA = {}
        self.distancia = None  # Inicializa la distancia como infinito
        self.predecesor = None  # Inicializa el predecesor como None

    
    def agregar_vecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id)+"conectadoA:" + str([x.id for x in self.conectadoA])
    
    def obtener_conexiones (self):
        return self.conectadoA.keys()
    
    def obtener_id(self):
        return self.id
    
    def obtener_ponderacion(self, vecino):
        return self.conectadoA[vecino]
    
    def asignar_distancia(self, distancia):
        self.distancia = distancia

    def obtener_distancia(self):
        return self.distancia  
    
    def asignar_predecesor(self, predecesor):
        self.predecesor = predecesor

    def obtener_predecesor(self):
        return self.predecesor
    
 
class Grafo:
    def __init__(self):
        self.lista_vertices= {}
        self.num_vertices=0
    
    def agregar_vertices(self, clave):
        self.num_vertices=self.num_vertices + 1
        nuevo_vertice= Vertice(clave)
        self.lista_vertices[clave]= nuevo_vertice
        return nuevo_vertice
    
    def obtener_vertice(self, n):
        if n in self.lista_vertices:
            return self.lista_vertices[n]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.lista_vertices
    
    def agregar_aristas(self, de, a, costo=0):
        if de not in self.lista_vertices:
            nv=self.agregar_vertices(de)
        if a not in self.lista_vertices:
            nv=self.agregar_vertices(a)
        self.lista_vertices[de].agregar_vecino(self.lista_vertices[a], costo)
    
    def obtener_vertices(self):
        return self.lista_vertices.keys()
    
    def __iter__(self):
        """
        sobrecarga de metodo de iteracion 
        """
        return iter(self.lista_vertices.values())

if __name__ == "__main__":
    g = Grafo()
    for i in range(6):
        g.agregar_vertices(i)
        g.lista_vertices
        print(g)
    g.agregar_aristas(0,1,5)
    g.agregar_aristas(0,5,2)
    g.agregar_aristas(1,2,4)
    g.agregar_aristas(2,3,9)
    g.agregar_aristas(3,4,7)
    g.agregar_aristas(3,5,3)
    g.agregar_aristas(4,0,1)
    g.agregar_aristas(5,4,8)
    g.agregar_aristas(5,2,1)
    for v in g:
        for w in v.obtener_conexiones():
            print("( %s , %s )" % (v.obtener_id(), w.obtener_id()))
    g.obtener_vertice(0).asignar_distancia(10)
    print(g.obtener_vertice(0).obtener_distancia())  # Debería imprimir 10
    g.obtener_vertice(0).asignar_predecesor(g.obtener_vertice(1))
    print(g.obtener_vertice(0).obtener_predecesor().obtener_id())  # Debería imprimir 1 
    print(g.obtener_vertice(0))  # Debería imprimir el objeto Vertice con id 0 y sus conexiones
    #print(g.obtener_distancia(g.obtener_vertice(1)))  # Debería imprimir la ponderación de la arista entre 0 y 1
