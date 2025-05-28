class Vertice:
    def __init__(self, clave):
        self.id= clave
        self.conectadoA = {}

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

        
        

