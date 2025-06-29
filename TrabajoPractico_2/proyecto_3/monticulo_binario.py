class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0] 
        self.tamanoActual = 0 
    
    
    def infiltrarArriba(self, pos): 
        while pos // 2 > 0:
            if self.listaMonticulo[pos][0] < self.listaMonticulo[pos // 2][0]:
                self.listaMonticulo[pos], self.listaMonticulo[pos // 2] = self.listaMonticulo[pos // 2], self.listaMonticulo[pos]
            pos = pos // 2

    def insertar(self, nuevo_item):
        self.listaMonticulo.append(nuevo_item)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltrarArriba(self.tamanoActual)

    def hijoMin(self, pos):
    # Si no hay hijo derecho, devolvemos el hijo izquierdo directamente
        if pos * 2 + 1 > self.tamanoActual:
            return pos * 2
        else:
            if self.listaMonticulo[pos * 2][0] < self.listaMonticulo[pos * 2 + 1][0]:
                return pos * 2
            else:
                return pos * 2 + 1

    def infiltrarAbajo(self, pos):
        while (pos * 2) <= self.tamanoActual:
            hm = self.hijoMin(pos)
            if self.listaMonticulo[hm][0] < self.listaMonticulo[pos][0]:
                self.listaMonticulo[pos], self.listaMonticulo[hm] = self.listaMonticulo[hm], self.listaMonticulo[pos]
            pos = hm
    
    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltrarAbajo(1)
        return valorSacado
  
    def construirMonticulo(self,unaLista):
        for i in unaLista:
            self.insertar(i)
        

    def estaVacio(self):
        return self.tamanoActual == None or self.tamanoActual == 0 
    
    def contiene(self, vertice): # verifica si el montículo contiene un vértice específico
        for i in self.listaMonticulo[1:][1]:
            if i == vertice: #compara el vértice con el segundo elemento de la tupla
                a= True # devuelve True si el vértice está presente
            else:
                a= False # devuelve False si el vértice no está presente
        return a # devuelve el resultado de la verificación
        
    def __iter__(self): # permite iterar sobre los elementos del montículo
        for i in range (1, len(self.listaMonticulo)): # comienza desde 1 para omitir el primer elemento (0)
            yield self.listaMonticulo[i] # yield devuelve el elemento actual de la lista del montículo

    def __str__(self): # devuelve una representación en cadena del montículo
        for i in self.listaMonticulo:
            print(i)

                        #el formato en el que se recibe es (clave, vertice)
    def decrementarClave(self, vertice, nuevaClave):    # busca el vértice en el montículo y actualiza su clave
        for i in range(1, len(self.listaMonticulo)): # busca la posición de la tupla que contiene el vértice
            if self.listaMonticulo[i][1] == vertice: # compara el vértice con el segundo elemento de la tupla
                self.listaMonticulo[i] = (nuevaClave, vertice) # Actualiza la clave del vértice
                self.infiltrarArriba(i) # reordena el montículo
                return

if __name__ == "__main__":
    b = MonticuloBinario()
    b.insertar((5, 'A'))
    b.insertar((3, 'B'))
    b.insertar((8, 'C'))
    b.insertar((1, 'D'))
    b.insertar((4, 'E'))
    print("Montículo después de inserciones:", b.listaMonticulo) # muestra el montículo después de insertar elementos
    print("Elemento mínimo eliminado:", b.eliminarMin()) 
    print("Montículo después de eliminar el mínimo:", b.listaMonticulo)
    b.construirMonticulo([(2, 'F'), (6, 'G'), (0, 'H')]) # construye el montículo a partir de una lista
    print("Montículo después de construir desde una lista:", b.listaMonticulo)
    print("¿Está vacío el montículo?", b.estaVacio())
    print("¿Contiene el valor (3, 'B')?", b.contiene(('B'))) # devuelve True si el montículo contiene el vértice 'B'
    b.decrementarClave ('G', 1)  # decrementar la clave del vértice 'G' a 1
    print("Montículo después de decrementar clave:", b.listaMonticulo)
    