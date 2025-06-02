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
        return self.tamanoActual ==None or self.tamanoActual == 0
    
    def contiene(self, vertice):
        return any(item[1] == vertice for item in self.listaMonticulo[1:])

    def decrementarClave(self, vertice, nuevaClave):   #el formato en el que se recibe es (clave, vertice)
        # Busca la posición de la tupla que contiene el vértice
        for i in range(1, len(self.listaMonticulo)):
            if self.listaMonticulo[i][1] == vertice:
                self.listaMonticulo[i] = (nuevaClave, vertice)
                self.infiltrarArriba(i)
                return

if __name__ == "__main__":
    b = MonticuloBinario()
    b.insertar((5, 'A'))
    b.insertar((3, 'B'))
    b.insertar((8, 'C'))
    b.insertar((1, 'D'))
    b.insertar((4, 'E'))
    print("Montículo después de inserciones:", b.listaMonticulo)
    print("Elemento mínimo eliminado:", b.eliminarMin())
    print("Montículo después de eliminar el mínimo:", b.listaMonticulo)
    b.construirMonticulo([(2, 'F'), (6, 'G'), (0, 'H')])
    print("Montículo después de construir desde una lista:", b.listaMonticulo)
    print("¿Está vacío el montículo?", b.estaVacio())
    print("¿Contiene el valor (3, 'B')?", b.contiene((3, 'B')))
    b.decrementarClave ('G', 1)  
    print("Montículo después de decrementar clave:", b.listaMonticulo)

