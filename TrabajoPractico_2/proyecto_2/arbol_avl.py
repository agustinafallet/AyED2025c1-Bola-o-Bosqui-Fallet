class NodoArbol:
    def __init__(self, clave, valor, padre=None, izquierdo=None, derecho=None):
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
        
    def hijo_izquierdo(self):
        return self.__izquierdo
    
    def hijo_derecho(self):
        return self.__derecho
    
    def eshijoderecho(self):
        return self.__padre and self.__padre.derecho==self
    
    def eshijoizquierdo(self):
        return self.__padre and self.__padre.izquierdo==self
    
    def esraiz(self):
        return not self.__padre
    
    def eshoja(self):
        return not self.__izquierdo and not self.__derecho
    
    def tiene_un_hijo(self):
        return (self.__izquierdo is not None) != (self.__derecho is not None)  # Solo uno de los dos

    def tiene_ambos_hijos(self):
        return self.__izquierdo and self.__derecho
    
    def reemplazar_nodo(self,clave,valor,izq,der):
        self.__clave = clave
        self.__valor = valor
        self.__izquierdo = izq
        self.__derecho = der
        if self.hijoizquierdo():
            self.__izquierdo.padre = self
        if self.hijoderecho():
            self.__derecho.padre = self
    
            
            
class ArbolAVL:
    def __init__(self):
        self.__raiz = None
        self.__tamanio = 0

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
        
    def longitud(self):
        return self.tamanio
    
    def __len__(self):
        return self.tamanio 
    
    def __iter__(self):
        def recorrido_in_order(nodo):
            if nodo is not None:
                yield from recorrido_in_order(nodo.izquierdo)
                yield nodo
                yield from recorrido_in_order(nodo.derecho)
        yield from recorrido_in_order(self.raiz)
            
    def actualizar_factor(self, nodo):
        nodo.factor_de_equilibrio = self.altura(nodo.izquierdo) - self.altura(nodo.derecho)         
    
    def altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))
    
    def agregar ( self, clave, valor):
        if self.raiz:
            self._agregar(clave,valor,self.raiz)
        else:
            self.raiz = NodoArbol(clave,valor)
        self.tamanio += 1
        return True
    
    def _agregar(self,clave,valor,nodoactual): 
        if clave < nodoactual.clave:
            if nodoactual.hijo_izquierdo():
                self._agregar(clave,valor,nodoactual.izquierdo)
            else:
                nodoactual.izquierdo = NodoArbol(clave,valor,padre=nodoactual)
                self.nuevo_equilibrio(nodoactual.izquierdo)
        else:
            if nodoactual.hijo_derecho():
                self._agregar(clave,valor,nodoactual.derecho)
            else:
                nodoactual.derecho = NodoArbol(clave,valor,padre=nodoactual)
                self.nuevo_equilibrio(nodoactual.derecho)
    
    def buscar(self, clave):
        def _buscar(nodo, clave):
            if nodo is None or nodo.clave == clave:
                return nodo
            elif clave < nodo.clave:
                return _buscar(nodo.izquierdo, clave)
            else:
                return _buscar(nodo.derecho, clave)
        
        return _buscar(self.raiz, clave)
    
    def _buscar_sucesor(self, nodo):
        nodo = nodo.derecho
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo
    
    def _eliminar(self, nodo):
        padre = nodo.padre
        if nodo.eshoja():
            if nodo.esraiz():
                self.raiz = None
            else:
                if nodo.eshijoizquierdo():
                    nodo.padre.izquierdo = None
                else:
                    nodo.padre.derecho = None
        elif nodo.tiene_un_hijo():
            hijo = nodo.hijo_izquierdo() or nodo.hijo_derecho()
            if nodo.esraiz():
                self.raiz = hijo
                if self.raiz:
                    self.raiz.padre = None
            else:
                if nodo.eshijoizquierdo():
                    nodo.padre.izquierdo = hijo
                else:
                    nodo.padre.derecho = hijo
                hijo.padre = nodo.padre
        else:
            sucesor = self._buscar_sucesor(nodo)
            nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
            self._eliminar(sucesor)  # Elimina el sucesor, que tendrá a lo sumo un hijo derecho

        # Rebalancear desde el padre del nodo eliminado
        actual = padre
        while actual:
            self.actualizar_factor(actual)
            if actual.factor_de_equilibrio < -1:
                if self.altura(actual.derecho.derecho) >= self.altura(actual.derecho.izquierdo):
                    self.rotacion_izquierdo(actual)
                else:
                    self.rotacion_derecha(actual.derecho)
                    self.rotacion_izquierdo(actual)
            elif actual.factor_de_equilibrio > 1:
                if self.altura(actual.izquierdo.izquierdo) >= self.altura(actual.izquierdo.derecho):
                    self.rotacion_derecha(actual)
                else:
                    self.rotacion_izquierdo(actual.izquierdo)
                    self.rotacion_derecha(actual)
            actual = actual.padre
    
    def eliminar(self, clave):
        nodo = self.buscar(clave)
        if nodo:
            self._eliminar(nodo)
            self.tamanio -= 1
            return True
        return False
    
    def nuevo_equilibrio(self,nodo):
        while nodo:
            self.actualizar_factor(nodo)
            if nodo.factor_de_equilibrio < -1:
                if self.altura(nodo.derecho.derecho) >= self.altura(nodo.derecho.izquierdo):
                    self.rotacion_izquierdo(nodo)
                else:
                    self.rotacion_derecha(nodo.derecho)
                    self.rotacion_izquierdo(nodo)
            elif nodo.factor_de_equilibrio > 1:
                if self.altura(nodo.izquierdo.izquierdo) >= self.altura(nodo.izquierdo.derecho):
                    self.rotacion_derecha(nodo)
                else:
                    self.rotacion_izquierdo(nodo.izquierdo)
                    self.rotacion_derecha(nodo)
            nodo = nodo.padre
    
    def rotacion_izquierdo(self, rotRaiz):
        nuevoRaiz  = rotRaiz.derecho
        rotRaiz.derecho = nuevoRaiz.izquierdo
        if nuevoRaiz.izquierdo:
            nuevoRaiz.izquierdo.padre = rotRaiz
        nuevoRaiz.padre = rotRaiz.padre
        if rotRaiz.esraiz():
            self.raiz = nuevoRaiz
            self.raiz.padre = None
        else:
            if rotRaiz.eshijoizquierdo():
                rotRaiz.padre.izquierdo = nuevoRaiz
            else:
                rotRaiz.padre.derecho = nuevoRaiz
        nuevoRaiz.izquierdo = rotRaiz
        rotRaiz.padre = nuevoRaiz
        self.actualizar_factor(rotRaiz)
        self.actualizar_factor(nuevoRaiz)
        
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



