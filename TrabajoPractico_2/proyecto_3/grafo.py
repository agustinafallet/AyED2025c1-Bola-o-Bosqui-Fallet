import sys

class Vertice:
    def __init__(self, clave):
        self.id= clave
        self.conectadoA = {}
        self.distancia = sys.maxsize  # Inicializa la distancia como None
        self.predecesor = None  # Inicializa el predecesor como None

    def __eq__(self, other): # compara dos vértices por su id y predecesor
        # compara si el otro objeto es una instancia de Vertice y si sus ids y predecesores son iguales
        return isinstance(other, Vertice) and self.id == other.id and self.predecesor == other.predecesor
    
    def __hash__(self): # devuelve un hash del id del vértice para que pueda ser utilizado en diccionarios
        return hash(self.id) #generar un hash único para el vértice a partir de su id
    
    def agregar_vecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self): # devuelve una representación en cadena del vértice y sus conexiones
        return str(self.id)+"conectadoA:" + str([x.id for x in self.conectadoA])
    
    def obtener_conexiones (self):
        return self.conectadoA.keys() # obtiene los vecinos del vértice y los devuelve como una lista de claves
    
    def obtener_id(self):
        return self.id
    
    def obtener_ponderacion(self, vecino): # obtiene la ponderación de la arista hacia el vecino y la devuelve
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
        self.lista_vertices= {} # diccionario para almacenar los vértices del grafo
        self.num_vertices=0
    
    def agregar_vertices(self, clave): # agrega un nuevo vértice al grafo a partir de su clave
        if clave not in self.lista_vertices: # verifica si el vértice ya existe
            self.num_vertices += 1 # incrementa el número de vértices
            nuevo_vertice = Vertice(clave) 
            self.lista_vertices[clave] = nuevo_vertice # agrega el nuevo vértice al diccionario con su clave
            return nuevo_vertice
        return self.lista_vertices[clave] # si el vértice ya existe, lo devuelve sin crear uno nuevo
    
    def obtener_vertice(self, n): # obtiene un vértice del grafo a partir de su clave
        if n in self.lista_vertices: # verifica si el vértice existe en el grafo
            return self.lista_vertices[n] # devuelve el vértice si existe
        else: # si el vértice no existe
            return None 
        
    def __contains__(self, n): # permite verificar si un vértice está en el grafo
        return n in self.lista_vertices 
    
    def agregar_aristas(self, de, a, costo=0):
        if de not in self.lista_vertices:
            self.agregar_vertices(de)
        if a not in self.lista_vertices:
            self.agregar_vertices(a)
        self.lista_vertices[de].agregar_vecino(self.lista_vertices[a], costo)
        #self.lista_vertices[a].agregar_vecino(self.lista_vertices[de], costo) 
   
    def obtener_vertices(self):
        return self.lista_vertices.keys()
    
    def __iter__(self): #sobrecarga de metodo de iteracion 
        return iter(self.lista_vertices.values()) # devuelve un iterador sobre los valores del diccionario de vértices

if __name__ == "__main__":
    g = Grafo()
    for i in range(6):
        g.agregar_vertices(i)
        g.lista_vertices
        #print(g)
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
            print("( %s , %s )" % (v.obtener_id(), w.obtener_id())) # Imprime las conexiones de cada vértice
    g.obtener_vertice(0).asignar_distancia(10) # Asigna una distancia al vértice 0
    print(g.obtener_vertice(0).obtener_distancia())  # Debería imprimir 10
    g.obtener_vertice(0).asignar_predecesor(g.obtener_vertice(1))
    print(g.obtener_vertice(0).obtener_predecesor().obtener_id())  # Debería imprimir 1 
    print(g.obtener_vertice(0))  # Debería imprimir el objeto Vertice con id 0 y sus conexiones
    #print(g.obtener_distancia(g.obtener_vertice(1)))  # Debería imprimir la ponderación de la arista entre 0 y 1
    vertice_a = Vertice(4) # Crea un nuevo vértice con id 4
    vertice_c = Vertice(4) # Crea otro nuevo vértice con el mismo id
    vertice_a.asignar_predecesor(vertice_c) # Asigna el predecesor del vértice a otro vértice
    