class NodoArbol:
    def __init__(self, clave, valor, padre=None, izquierdo=None, derecho=None):
        self.clave=clave
        self.valor=valor
        self.padre=padre
        self.izquierdo=izquierdo
        self.derecho=derecho
        self.factor_de_equilibrio = 0
    
    def hijo_izquierdo(self):
        return self.izquierdo
    
    def hijo_derecho(self):
        return self.derecho
    
    def eshijoderecho(self):
        return self.padre and self.padre.derecho==self
    
    def eshijoizquierdo(self):
        return self.padre and self.padre.izquierdo==self
    
    def esraiz(self):
        return not self.padre
    
    def eshoja(self):
        return not self.izquierdo and not self.derecho
    
    def tiene_un_hijo(self):
        return self.izquierdo or self.derecho
    
    def tiene_ambos_hijos(self):
        return self.izquierdo and self.derecho
    
    def reemplazar_nodo(self,clave,valor,izq,der):
        self.clave = clave
        self.valor = valor
        self.izquierdo = izq
        self.derecho = der
        if self.hijoizquierdo():
            self.izquierdo.padre = self
        if self.hijoderecho():
            self.derecho.padre = self
    
            
            
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
        if nodo.factor_de_equilibrio > 1 or nodo.factor_de_equilibrio < -1:
            self.reequilibrar(nodo)
            return
        if nodo.padre:
            if nodo.hijo_izquierdo():
                nodo.padre.factor_de_equilibrio += 1
            elif nodo.hijo_derecho():
                nodo.padre.factor_de_equilibrio -= 1
            if nodo.padre.factor_de_equilibrio != 0:
                self.nuevo_equilibrio(nodo.padre)
                
    def rotacion_izquierdo(self, rotRaiz):
        nuevoRaiz  = rotRaiz.derecho
        rotRaiz.derecho = nuevoRaiz.izquierdo
        if nuevoRaiz.izquierdo != None:
            nuevoRaiz.izquierdo.padre = rotRaiz
            nuevoRaiz.padre = rotRaiz.padre
        if rotRaiz.esraiz():
            self.raiz = nuevoRaiz
        else:
            if rotRaiz.hijo_izquierdo():
                rotRaiz.padre.izquierdo = nuevoRaiz
            else:
                rotRaiz.padre.derecho = nuevoRaiz
        nuevoRaiz.izquierdo = rotRaiz
        rotRaiz.padre = nuevoRaiz
        print(nuevoRaiz.valor)
        rotRaiz.factor_de_equilibrio = rotRaiz.factor_de_equilibrio + 1 - min(nuevoRaiz.factor_de_equilibrio,0)
        nuevoRaiz.factor_de_equilibrio = nuevoRaiz.factor_de_equilibrio + 1 + max(rotRaiz.factor_de_equilibrio,0)
        
    def rotacion_derecha(self, rotRaiz):
        nuevoRaiz = rotRaiz.izquierdo
        rotRaiz.izquierdo = nuevoRaiz.derecho
        if nuevoRaiz.derecho != None:
            nuevoRaiz.derecho.padre = rotRaiz
        nuevoRaiz.padre = rotRaiz.padre
        if rotRaiz.esraiz():
            self.raiz = nuevoRaiz
        else:
            if rotRaiz.hijo_derecho():
                rotRaiz.padre.derecho = nuevoRaiz
            else:
                rotRaiz.padre.izquierdo = nuevoRaiz
        nuevoRaiz.derecho = rotRaiz
        rotRaiz.padre = nuevoRaiz
        print(nuevoRaiz.valor)
        rotRaiz.factor_de_equilibrio = rotRaiz.factor_de_equilibrio - 1 - max(nuevoRaiz.factor_de_equilibrio,0)
        nuevoRaiz.factor_de_equilibrio = nuevoRaiz.factor_de_equilibrio - 1 + min(rotRaiz.factor_de_equilibrio,0)
        
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
    # arbol.agregar(40, "Cuarenta")
    # arbol.agregar(50, "Cincuenta")
    # arbol.agregar(25, "Veinticinco")
    # for i in arbol:
    #     print(i.clave, i.valor)
    
    print("Tamaño del árbol:", arbol.longitud())
    print("Raíz del árbol:", arbol.raiz.clave)
        
        
        
        