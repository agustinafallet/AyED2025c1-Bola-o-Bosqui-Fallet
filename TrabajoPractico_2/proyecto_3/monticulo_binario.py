class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
    
    def infiltrarArriba(self, pos):
        while pos // 2 > 0:
            hijo = list(self.listaMonticulo[pos])
            padre = list(self.listaMonticulo[pos//2])
            if hijo[0] < padre[0]:
                # Intercambio de posiciones
                temp = padre[0]
                #print(f"Intercambiando {padre} con {hijo} en posiciones {pos//2} y {pos}") 
                #list(self.listaMonticulo[pos//2]), list(self.listaMonticulo[pos]) == list(self.listaMonticulo[pos]), list(temp)
                padre[0] = hijo[0]
                hijo[0] = temp
                
            pos=pos//2

    def insertar(self, nuevo_item):
        self.listaMonticulo.append(nuevo_item)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltrarArriba(self.tamanoActual)

    # def hijoMin(self,pos):
    #     compara1= list(self.listaMonticulo[pos*2])
    #     compara2= list(self.listaMonticulo[pos*2+1])

    #     if compara2[0] > self.tamanoActual:
    #         return pos * 2
    #     else:
    #         if compara1[0] < compara2[0]:
    #             return pos * 2
    #         else:
    #             return pos * 2 + 1

    def hijoMin(self, pos):
    # Si no hay hijo derecho, devolvemos el hijo izquierdo directamente
        if pos * 2 + 1 > self.tamanoActual:
            return pos * 2
        else:
            if self.listaMonticulo[pos * 2][0] < self.listaMonticulo[pos * 2 + 1][0]:
                return pos * 2
            else:
                return pos * 2 + 1


    # def infiltrarAbajo(self, pos):
    #     """""como el monticulo es de minimo, si el padre es mayor que el hijo, hay que intercambiar. para ello
    #     debimos colocar [0] a la hora de comparar ya que la listaMonticulo es una lista formada por tuplas"""
    #     while (pos * 2) <= self.tamanoActual:
    #         hm = self.hijoMin(pos)
    #         hijo= list(self.listaMonticulo[hm])
    #         padre = list(self.listaMonticulo[pos])
    #         if hijo[0] < padre[0]: 
    #             tmp = padre[0]
    #             padre[0] = hijo[0]
    #             hijo[0] = tmp
    #         pos = hm

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
        # pos = len(unaLista) // 2
        # self.tamanoActual = len(unaLista)
        # self.listaMonticulo = [0] + unaLista[:]
        # while (pos > 0):
        #     self.infiltrarAbajo(pos)
        #     pos = pos - 1

    def estaVacio(self):
        return self.tamanoActual ==None or self.tamanoActual == 0
    
    def contiene(self, valor):
        return valor in self.listaMonticulo
    
    def decrementarClave(self, valor, nuevaClave):
        if valor in self.listaMonticulo:
            pos = self.listaMonticulo.index(valor)
            self.listaMonticulo[pos] = nuevaClave
            self.infiltrarArriba(pos)
        else:
            raise ValueError("El valor no se encuentra en el montículo.")


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
    b.decrementarClave((6, 'G'), (1, 'G'))
    print("Montículo después de decrementar clave:", b.listaMonticulo)

