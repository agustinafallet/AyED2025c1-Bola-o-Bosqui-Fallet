class NodoArbol:
    def __init__(self, clave, valor, padre=None, izquierdo=None, derecho=None): # Nodo de un árbol AVL
        self.__clave=clave  
        self.__valor=valor
        self.__padre=padre
        self.__izquierdo=izquierdo
        self.__derecho=derecho
        self.__factor_de_equilibrio = 0 
    
    @property  
    def clave(self):
        return self.__clave
    
    @clave.setter
    def clave(self, valor):
        self.__clave = valor
    
    @property 
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    @property
    def padre(self):
        return self.__padre
    
    @padre.setter
    def padre(self, valor):
        self.__padre = valor
    
    @property
    def izquierdo(self):
        return self.__izquierdo
    
    @izquierdo.setter
    def izquierdo(self, valor):
        self.__izquierdo = valor
        
    @property
    def derecho(self):
        return self.__derecho
    
    @derecho.setter
    def derecho(self, valor):
        self.__derecho = valor
        
    @property
    def factor_de_equilibrio(self):
        return self.__factor_de_equilibrio
    
    @factor_de_equilibrio.setter
    def factor_de_equilibrio(self, valor):
        self.__factor_de_equilibrio = valor
        
    def hijo_izquierdo(self):  # Verifica si el nodo tiene hijo izquierdo
        return self.__izquierdo
    
    def hijo_derecho(self):   # Verifica si el nodo tiene hijo derecho
        return self.__derecho
    
    def eshijoderecho(self):  # Verifica si el nodo es hijo derecho de su padre
        return self.__padre and self.__padre.derecho==self
    
    def eshijoizquierdo(self):  #Lo contrario de lo anterior
        return self.__padre and self.__padre.izquierdo==self
    
    def esraiz(self):   # Verifica si el nodo es la raíz del árbol
        return not self.__padre
    
    def eshoja(self):  # Verifica si el nodo es una hoja (sin hijos)
        return not self.__izquierdo and not self.__derecho
    
    def tiene_un_hijo(self):  # Verifica si el nodo tiene solo un hijo
        return (self.__izquierdo is not None) != (self.__derecho is not None)  # Solo uno de los dos

    def tiene_ambos_hijos(self):  # Verifica si el nodo tiene ambos hijos
        return self.__izquierdo and self.__derecho
    
    def reemplazar_nodo(self,clave,valor,izq,der): # Reemplaza los valores del nodo actual
        self.__clave =  clave
        self.__valor = valor
        self.__izquierdo = izq   # Nuevo hijo izquierdo
        self.__derecho = der     # Nuevo hijo derecho
        if self.hijoizquierdo():  # Si tiene hijo izquierdo, lo asigna al padre
            self.__izquierdo.padre = self  
        if self.hijoderecho():   # Si tiene hijo derecho, lo asigna al padre
            self.__derecho.padre = self
    
            
            
class ArbolAVL:
    def __init__(self):
        self.__raiz = None  # Raíz del árbol
        self.__tamanio = 0  # Tamaño del árbol (número de nodos), se incializa en 0

    @property
    def raiz(self):
        return self.__raiz
    
    @raiz.setter
    def raiz(self, valor):
        self.__raiz = valor
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter 
    def tamanio(self, valor):
        self.__tamanio = valor
        
    def longitud(self):  # Retorna el tamaño del árbol
        return self.tamanio
    
    def __len__(self):  # Permite usar len(arbol) para obtener el tamaño del árbol
        return self.tamanio 
    
    def __iter__(self):  # Permite iterar sobre los nodos del árbol en orden
        def recorrido_in_order(nodo):  # Recorrido in-order del árbol
            if nodo is not None:
                yield from recorrido_in_order(nodo.izquierdo) #recorrido sub arbol izquierdo
                yield nodo
                yield from recorrido_in_order(nodo.derecho) #recorrido sub arbol derecho
        yield from recorrido_in_order(self.raiz) #recorrido desde la raíz del árbol
            
    def actualizar_factor(self, nodo): # Actualiza el factor de equilibrio del nodo
        nodo.factor_de_equilibrio = self.altura(nodo.izquierdo) - self.altura(nodo.derecho)        
    
    def altura(self, nodo): # Calcula la altura del árbol a partir de un nodo
        if nodo is None:
            return -1
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho)) # Devuelve la altura del nodo, considerando que una hoja tiene altura 0 y comparando los hijos izquierdo y derecho para obtener la mayor altura.
    
    def agregar ( self, clave, valor):  # Agrega un nuevo nodo al árbol
        if self.raiz:  # Si el árbol no está vacío, se agrega el nodo en la posición correspondiente
            self._agregar(clave,valor,self.raiz) 
        else:
            self.raiz = NodoArbol(clave,valor) # Si el árbol está vacío, se crea un nuevo nodo como raíz
        self.tamanio += 1 # Incrementa el tamaño del árbol
        return True  
    
    def _agregar(self,clave,valor,nodoactual):  # Método recursivo para agregar un nodo al árbol
        if clave < nodoactual.clave:            # Si la clave es menor, se va al subárbol izquierdo
            if nodoactual.hijo_izquierdo():     # Si ya hay un hijo izquierdo, se llama recursivamente
                self._agregar(clave,valor,nodoactual.izquierdo) 
            else:
                nodoactual.izquierdo = NodoArbol(clave,valor,padre=nodoactual) # Si no hay hijo izquierdo, se crea un nuevo nodo
                self.nuevo_equilibrio(nodoactual.izquierdo)  #se llama a nuevo_equilibrio para verificar si el árbol necesita ser reequilibrado
        else:
            if nodoactual.hijo_derecho():       # Si la clave es mayor o igual, se va al subárbol derecho
                self._agregar(clave,valor,nodoactual.derecho)  # Si ya hay un hijo derecho, se llama recursivamente 
            else:
                nodoactual.derecho = NodoArbol(clave,valor,padre=nodoactual)  # Si no hay hijo derecho, se crea un nuevo nodo
                self.nuevo_equilibrio(nodoactual.derecho)  #se llama a nuevo_equilibrio para verificar si el árbol necesita ser reequilibrado
    
    def buscar(self, clave):  # Busca un nodo por su clave
        def _buscar(nodo, clave):    # Método recursivo para buscar un nodo por su clave
            if nodo is None or nodo.clave == clave:  # Si el nodo es None o la clave coincide, se retorna el nodo
                return nodo
            elif clave < nodo.clave:  # Si la clave es menor, se busca en el subárbol izquierdo
                return _buscar(nodo.izquierdo, clave)  
            else:    # Si la clave es mayor, se busca en el subárbol derecho
                return _buscar(nodo.derecho, clave)
        
        return _buscar(self.raiz, clave) # Retorna el nodo encontrado o None si no se encuentra
    
    def _buscar_sucesor(self, nodo):  # Busca el sucesor (el menor del subárbol derecho)
        nodo = nodo.derecho           # Comienza en el subárbol derecho del nodo a eliminar
        while nodo.izquierdo:         # Mientras haya un hijo izquierdo, se sigue buscando
            nodo = nodo.izquierdo     # Se mueve al hijo izquierdo 
        return nodo                   # Retorna el nodo más a la izquierda del subárbol derecho, que es el sucesor
    
    def _eliminar(self, nodo):
        padre = nodo.padre    # Guarda el padre del nodo a eliminar para rebalancear después
        if nodo.eshoja(): # caso 1, se elimina directamente el nodo 
            if nodo.esraiz():  # Si el nodo es la raíz, se establece la raíz como None
                self.raiz = None
            else:
                if nodo.eshijoizquierdo(): # Si es hijo izquierdo, se elimina de su padre
                    nodo.padre.izquierdo = None    
                else:
                    nodo.padre.derecho = None   # Si es hijo derecho, se elimina de su padre
        elif nodo.tiene_un_hijo(): # caso 2, si tiene un hijo, se busca el hijo y se vuelve el padre
            hijo = nodo.hijo_izquierdo() or nodo.hijo_derecho() # Se obtiene el hijo (izquierdo o derecho)
            if nodo.esraiz():    # Si el nodo es la raíz, se establece el hijo como nueva raíz
                self.raiz = hijo  
                if self.raiz:     # Si el hijo no es None, se establece su padre como None
                    self.raiz.padre = None 
            else:
                if nodo.eshijoizquierdo(): # Si es hijo izquierdo, se establece el hijo como hijo izquierdo del padre
                    nodo.padre.izquierdo = hijo   
                else:
                    nodo.padre.derecho = hijo   # Si es hijo derecho, se establece el hijo como hijo derecho del padre
                hijo.padre = nodo.padre
        else: # caso 3, si tiene ambos hijos, se busca el menor del subarbol derecho, y ese pasa a ser el padre
            sucesor = self._buscar_sucesor(nodo)  # Se busca el sucesor del nodo a eliminar
            nodo.clave, nodo.valor = sucesor.clave, sucesor.valor   # Se reemplaza el nodo a eliminar con el sucesor
            self._eliminar(sucesor)  # Elimina el sucesor, que tendrá a lo sumo un hijo derecho

        # Rebalancear desde el padre del nodo eliminado
        actual = padre
        while actual:   # Se recorre hacia arriba desde el padre del nodo eliminado
            self.actualizar_factor(actual)  # Actualiza el factor de equilibrio del nodo actual
            if actual.factor_de_equilibrio < -1:  # Si el factor de equilibrio es menor que -1, se rebalancea
                if self.altura(actual.derecho.derecho) >= self.altura(actual.derecho.izquierdo):  # Si el subárbol derecho es más alto o igual al izquierdo
                    self.rotacion_izquierdo(actual)  # Rotación izquierda
                else:      
                    self.rotacion_derecha(actual.derecho) # Rotación derecha en el subárbol derecho
                    self.rotacion_izquierdo(actual)   # Rotación izquierda en el nodo actual
            elif actual.factor_de_equilibrio > 1:  # Si el factor de equilibrio es mayor que 1, se rebalancea
                if self.altura(actual.izquierdo.izquierdo) >= self.altura(actual.izquierdo.derecho): # Si el subárbol izquierdo es más alto o igual al derecho
                    self.rotacion_derecha(actual)  # Rotación derecha
                else:
                    self.rotacion_izquierdo(actual.izquierdo) # Rotación izquierda en el subárbol izquierdo
                    self.rotacion_derecha(actual)  # Rotación derecha en el nodo actual
            actual = actual.padre # Se mueve al padre del nodo actual para seguir rebalanceando hacia arriba
    
    def eliminar(self, clave):  # Elimina un nodo por su clave
        nodo = self.buscar(clave)  # Busca el nodo a eliminar
        if nodo:  # Si el nodo existe, se procede a eliminarlo
            self._eliminar(nodo)  # Elimina el nodo encontrado
            self.tamanio -= 1  # Decrementa el tamaño del árbol
            return True # Retorna True si se eliminó el nodo correctamente
        return False # Si el nodo no existe, no se hace nada y se retorna False
    
    def nuevo_equilibrio(self,nodo): # Rebalancea el árbol a partir del nodo recién agregado
        while nodo: # Recorre hacia arriba desde el nodo recién agregado
            self.actualizar_factor(nodo)  # Actualiza el factor de equilibrio del nodo
            if nodo.factor_de_equilibrio < -1: # Si el factor de equilibrio es menor que -1, se rebalancea  
                if self.altura(nodo.derecho.derecho) >= self.altura(nodo.derecho.izquierdo): # Si el subárbol derecho es más alto o igual al izquierdo:
                    self.rotacion_izquierdo(nodo)  # Rotación izquierda
                else:  # Si el subárbol izquierdo es más alto, se hace una rotación derecha en el subárbol derecho y luego una rotación izquierda en el nodo actual
                    self.rotacion_derecha(nodo.derecho)
                    self.rotacion_izquierdo(nodo)
            elif nodo.factor_de_equilibrio > 1: # Si el factor de equilibrio es mayor que 1, se rebalancea
                if self.altura(nodo.izquierdo.izquierdo) >= self.altura(nodo.izquierdo.derecho): # Si el subárbol izquierdo es más alto o igual al derecho:
                    self.rotacion_derecha(nodo) # Rotación derecha
                else:
                    self.rotacion_izquierdo(nodo.izquierdo) # Rotación izquierda en el subárbol izquierdo
                    self.rotacion_derecha(nodo) # Rotación derecha en el nodo actual
            nodo = nodo.padre # Se mueve al padre del nodo actual para seguir rebalanceando hacia arriba
    
    def rotacion_izquierdo(self, rotRaiz): # Realiza una rotación izquierda en el nodo dado
        nuevoRaiz  = rotRaiz.derecho      # El nuevo nodo raíz será el hijo derecho del nodo actual
        rotRaiz.derecho = nuevoRaiz.izquierdo  # El hijo derecho del nodo actual se convierte en el hijo izquierdo del nuevo nodo raíz
        if nuevoRaiz.izquierdo: # Si el nuevo nodo raíz tiene un hijo izquierdo, se actualiza su padre
            nuevoRaiz.izquierdo.padre = rotRaiz  
        nuevoRaiz.padre = rotRaiz.padre  # El padre del nuevo nodo raíz será el padre del nodo actual
        if rotRaiz.esraiz():  # Si el nodo actual es la raíz, se actualiza la raíz del árbol
            self.raiz = nuevoRaiz 
            self.raiz.padre = None 
        else: # Si no es la raíz, se actualiza el padre del nodo actual
            if rotRaiz.eshijoizquierdo(): 
                rotRaiz.padre.izquierdo = nuevoRaiz 
            else:  # Si es hijo derecho, se actualiza el padre del nodo actual
                rotRaiz.padre.derecho = nuevoRaiz  # El padre del nuevo nodo raíz será el padre del nodo actual
        nuevoRaiz.izquierdo = rotRaiz # El nodo actual se convierte en el hijo izquierdo del nuevo nodo raíz
        rotRaiz.padre = nuevoRaiz # El padre del nodo actual se actualiza al nuevo nodo raíz
        self.actualizar_factor(rotRaiz) # Actualiza el factor de equilibrio del nodo actual
        self.actualizar_factor(nuevoRaiz) # Actualiza el factor de equilibrio del nuevo nodo raíz
        
    def rotacion_derecha(self, rotRaiz): 
        nuevoRaiz = rotRaiz.izquierdo
        rotRaiz.izquierdo = nuevoRaiz.derecho
        if nuevoRaiz.derecho:
            nuevoRaiz.derecho.padre = rotRaiz
        nuevoRaiz.padre = rotRaiz.padre
        if rotRaiz.esraiz():
            self.raiz = nuevoRaiz
        else:
            if rotRaiz.eshijoderecho():
                rotRaiz.padre.derecho = nuevoRaiz
            else:
                rotRaiz.padre.izquierdo = nuevoRaiz
        nuevoRaiz.derecho = rotRaiz
        rotRaiz.padre = nuevoRaiz
        self.actualizar_factor(rotRaiz)
        self.actualizar_factor(nuevoRaiz)
        
    def reequilibrar(self, nodo):
        if nodo.factor_de_equilibrio < -1:
            if nodo.derecho.factor_de_equilibrio > 0:
                self.rotacion_derecha(nodo.derecho)
                self.rotacion_izquierdo(nodo)
            else:
                self.rotacion_izquierdo(nodo)
        elif nodo.factor_de_equilibrio > 1:
            if nodo.izquierdo.factor_de_equilibrio < 0:
                self.rotacion_izquierdo(nodo.izquierdo)
                self.rotacion_derecha(nodo)
            else:
                self.rotacion_derecha(nodo)
                
if __name__ == "__main__":
    arbol = ArbolAVL()
    arbol.agregar(20, "Veinte")
    arbol.agregar(30, "Treinta")
    arbol.agregar(5, "Cinco")
    arbol.agregar(40, "Cuarenta")
    arbol.agregar(50, "Cincuenta")
    arbol.agregar(25, "Veinticinco")
    for i in arbol:
        print(i.clave, i.valor)
        
    print("Tamaño del árbol:", arbol.longitud())
    print("Raíz del árbol:", arbol.raiz.clave)
    print("Buscar clave 30:", arbol.buscar(30).valor)
    print("Buscar clave 100:", arbol.buscar(100))  # No debería encontrar nada
    arbol.eliminar(30)
    print("Después de eliminar clave 30:")
    for i in arbol:
        print(i.clave, i.valor)
    print("Tamaño del árbol después de eliminar:", arbol.longitud())
    print("Raíz del árbol después de eliminar:", arbol.raiz.clave)



