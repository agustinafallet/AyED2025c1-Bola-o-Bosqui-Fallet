class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
    
    def infiltrarArriba(self, pos):
        while pos // 2 > 0:
            if self.listaMonticulo[pos][0] < self.listaMonticulo[pos//2][0]:
                temp = self.listaMonticulo[pos//2][0]
                self.listaMonticulo[pos//2][0]= self.listaMonticulo[pos][0]
                self.listaMonticulo[pos][0]=temp
            pos=pos//2

    def insertar(self, nuevo_item):
        self.listaMonticulo.append(nuevo_item)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltrarArriba(self.tamanoActual)

    def hijoMin(self,pos):
        if pos * 2 + 1 > self.tamanoActual:
            return pos * 2
        else:
            if self.listaMonticulo[pos*2][0] < self.listaMonticulo[pos*2+1][0]:
                return pos * 2
            else:
                return pos * 2 + 1

    def infiltrarAbajo(self, pos):
        """""como el monticlo es de minimo, si el padre es mayor que el hijo, hay que intercambiar. para ello
        debimos colocar [0] a la hora de comparar ya que la listaMonticulo es una lista formada por tuplas"""
        while (pos * 2) <= self.tamanoActual:
            hm = self.hijoMin(pos)
            if self.listaMonticulo[pos][0] > self.listaMonticulo[hm][0]: 
                tmp = self.listaMonticulo[pos][0]
                self.listaMonticulo[pos][0] = self.listaMonticulo[hm][0]
                self.listaMonticulo[hm][0] = tmp
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
        return self.tamanoActual == 0
    
    def contiene(self, valor):
        return valor in self.listaMonticulo
    
    def decrementarClave(self, valor, nuevaClave):
        if valor in self.listaMonticulo:
            pos = self.listaMonticulo.index(valor)
            self.listaMonticulo[pos] = nuevaClave
            self.infiltrarArriba(pos)
        else:
            raise ValueError("El valor no se encuentra en el montículo.")


# if __name__ == "__main__":
#     lista1=MonticuloBinario()
#     lista1.insertar(40)
#     lista1.insertar(30)
#     lista1.insertar(10)

    

#     print(lista1.listaMonticulo)

