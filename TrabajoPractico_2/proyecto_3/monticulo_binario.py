class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
    
    def infiltrarArriba(self, pos):
        while pos // 2 > 0:
            if self.listaMonticulo[pos] < self.listaMonticulo[pos//2]:
                temp = self.listaMonticulo[pos//2]
                self.listaMonticulo[pos//2]= self.listaMonticulo[pos]
                self.listaMonticulo[pos]=temp
            pos=pos//2

    def insertar(self, nuevo_item):
        self.listaMonticulo.append(nuevo_item)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltrarArriba(self.tamanoActual)

    def hijoMin(self,pos):
        if pos * 2 + 1 > self.tamanoActual:
            return pos * 2
        else:
            if self.listaMonticulo[pos*2] < self.listaMonticulo[pos*2+1]:
                return pos * 2
            else:
                return pos * 2 + 1

    def infiltrarAbajo(self, pos):
        while (pos * 2) <= self.tamanoActual:
            hm = self.hijoMin(pos)
            if self.listaMonticulo[pos] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[pos]
                self.listaMonticulo[pos] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            pos = hm
    
    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltrarAbajo(1)
        return valorSacado
  
    def construirMonticulo(self,unaLista):
        pos = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (pos > 0):
            self.infiltrarAbajo(pos)
            pos = pos - 1


if __name__ == "__main__":
    lista1=MonticuloBinario()
    lista1.insertar(40)
    lista1.insertar(30)
    lista1.insertar(10)

    

    print(lista1.listaMonticulo)

