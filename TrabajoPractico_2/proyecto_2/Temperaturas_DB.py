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
        return self.__izquierdo or self.__derecho
    
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
        self.raiz = None
        self.tamanio = 0

    def longitud(self):
        return self.tamanio
    
    def __len__(self):
        return self.tamanio 
    
    def __iter__(self):
        actual = self.raiz
        while actual is not None:
            yield actual
            if actual.izquierdo is not None:
                actual = actual.izquierdo
            elif actual.derecho is not None:
                actual = actual.derecho
            else:
                while actual.padre is not None and (actual.padre.derecho == actual or actual.padre.izquierdo == actual):
                        actual = actual.padre
                if actual.padre is None:
                    break
                else:
                     actual = actual.padre.derecho if actual.padre.derecho != None else None
    
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
                print("ejecuta nuevo equilibrio")
                self.nuevo_equilibrio(nodoactual.derecho)
                print("factor de equilibrio", nodoactual.factor_de_equilibrio)
    
    def nuevo_equilibrio(self,nodo):
        # if nodo.factor_de_equilibrio > 1 or nodo.factor_de_equilibrio < -1:
        #     self.reequilibrar(nodo)
        #     return
        # if nodo.padre:
        #     if nodo.hijo_izquierdo():
        #         nodo.padre.factor_de_equilibrio += 1
        #     elif nodo.hijo_derecho():
        #         nodo.padre.factor_de_equilibrio -= 1
        #     if nodo.padre.factor_de_equilibrio != 0:
        #         self.nuevo_equilibrio(nodo.padre)
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
        else:
            if rotRaiz.eshijoizquierdo():
                rotRaiz.padre.izquierdo = nuevoRaiz
            else:
                rotRaiz.padre.derecho = nuevoRaiz
        nuevoRaiz.izquierdo = rotRaiz
        rotRaiz.padre = nuevoRaiz
        print(nuevoRaiz.valor)
        #rotRaiz.factor_de_equilibrio = rotRaiz.factor_de_equilibrio + 1 - min(nuevoRaiz.factor_de_equilibrio,0)
        #nuevoRaiz.factor_de_equilibrio = nuevoRaiz.factor_de_equilibrio + 1 + max(rotRaiz.factor_de_equilibrio,0)
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
        print(nuevoRaiz.valor)
        # rotRaiz.factor_de_equilibrio = rotRaiz.factor_de_equilibrio - 1 - max(nuevoRaiz.factor_de_equilibrio,0)
        # nuevoRaiz.factor_de_equilibrio = nuevoRaiz.factor_de_equilibrio - 1 + min(rotRaiz.factor_de_equilibrio,0)
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
    arbol.agregar(10, "Diez")
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
        
        
        
        