class MonticuloBinario: #utilizamos el concepto de MB para la construccion de una cola de prioridad
    def __init__(self):
        self.listaMonticulo = [0]  #inicializamos la lista en 0 para que el primer elemento sea el 1
        self.tamanoActual = 0 #inicializamos el tamaño actual del monticulo en 0


#funcion para mantener la condicion del monticulo.
    def infiltrarArriba(self, pos):  
        while pos // 2 > 0: #comprueba que no sea la raíz
            if self.listaMonticulo[pos] < self.listaMonticulo[pos//2]:   #comprueba si el elemento es menor que su padre
                temp = self.listaMonticulo[pos//2]    #intercambia el elemento con su padre
                self.listaMonticulo[pos//2]= self.listaMonticulo[pos]  
                self.listaMonticulo[pos]=temp
            pos=pos//2  #actualiza la posicion del elemento a su padre

    def insertar(self, nuevo_item):     
        self.listaMonticulo.append(nuevo_item)   #añade el nuevo elemento al final de la lista
        self.tamanoActual = self.tamanoActual + 1  #incrementa el tamaño del monticulo
        self.infiltrarArriba(self.tamanoActual) #llama a la fucion para mantener la condicion del monticulo

    def hijoMin(self,pos): 
        if pos * 2 + 1 > self.tamanoActual:  #comprueba si el hijo derecho existe
            return pos * 2 #devuelve el hijo izquierdo si el derecho no existe
        else: 
            if self.listaMonticulo[pos*2] < self.listaMonticulo[pos*2+1]:  #compara los hijos izquierdo y derecho
                return pos * 2  #retorna el hijo izquierdo si es menor que el derecho
            else:
                return pos * 2 + 1 #retorna el hijo derecho si es menor o igual que el izquierdo

#funcion para mantener la condicion del monticulo.
    def infiltrarAbajo(self, pos):
        while (pos * 2) <= self.tamanoActual:  #comprueba que el nodo tenga al menos un hijo
            hm = self.hijoMin(pos)          #obtiene el hijo menor
            if self.listaMonticulo[pos] > self.listaMonticulo[hm]:     #compara el nodo con su hijo menor
                tmp = self.listaMonticulo[pos]               #intercambia el nodo con su hijo menor
                self.listaMonticulo[pos] = self.listaMonticulo[hm]        
                self.listaMonticulo[hm] = tmp           
            pos = hm         #actualiza la posicion del nodo al hijo menor
    
    def eliminarMin(self):       
        valorSacado = self.listaMonticulo[1]        #guarda el valor del nodo raiz
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]          #reemplaza la raiz con el ultimo elemento del monticulo
        self.tamanoActual = self.tamanoActual - 1          #decrementa el tamaño del monticulo
        self.listaMonticulo.pop()       #elimina el ultimo elemento del monticulo
        self.infiltrarAbajo(1)       #llama a la funcion para mantener la condicion del monticulo
        return valorSacado
  
    def construirMonticulo(self,unaLista):  #construye un monticulo a partir de una lista 
        pos = len(unaLista) // 2         #inicia desde el ultimo nodo que tiene hijos
        self.tamanoActual = len(unaLista)     #actualiza el tamaño del monticulo
        self.listaMonticulo = [0] + unaLista[:]    #inicializa la lista del monticulo con un 0 y copia los elementos de la lista dada
        while (pos > 0):           #recorre la lista desde el ultimo nodo con hijos hasta la raiz
            self.infiltrarAbajo(pos)      #llama a la funcion para mantener la condicion del monticulo
            pos = pos - 1          #decrementa la posicion del nodo

    def __len__ (self):
        return self.tamanoActual  

    def __iter__(self):
        return iter(self.listaMonticulo)     #permite iterar sobre los elementos del monticulo, omitiendo el primer elemento (0)

    
if __name__ == "__main__":

    lista1=MonticuloBinario()
    lista1.insertar(40)
    lista1.insertar(30)
    lista1.insertar(2)
    lista1.insertar(10)
    print(lista1.listaMonticulo)
    for i in lista1:
        print(i)
    print(f"tamaño:{lista1.__len__()}")
    print(lista1.eliminarMin())
    print(lista1.listaMonticulo)
    print(f"tamaño:{lista1.__len__()}")
    lista1.construirMonticulo([40, 30, 2, 10])
    print(lista1.listaMonticulo)
    lista1.insertar(5)
    print(lista1.listaMonticulo)
