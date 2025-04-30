class Nodo: #definimos nodo doblemente enlazado
    def __init__(self,datoinicial):
        self.dato = datoinicial
        self.anterior = None
        self.siguiente = None

    def obtenerdato(self):
        return self.dato

    def obtenersiguiente(self):
        return self.siguiente

    def obteneranterior(self):
        return self.anterior

    def asignardato(self, nuevodato):
        self.dato = nuevodato

    def asignarsiguiente(self, nuevosiguiente):
        self.siguiente = nuevosiguiente

    def asignaranterior(self, nuevoanterior):
        self.anterior = nuevoanterior

class ListaDobleEnlazada:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamanio= 0
    
    @property
    def cabeza(self):
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self,nueva_cabeza):
        self._cabeza = nueva_cabeza
    
    @property
    def cola(self):
        return self._cola
    @cola.setter
    def cola(self, nueva_cola):
        self._cola = nueva_cola 
    
    @property
    def tamanio(self):
        return self._tamanio
        
    def esta_vacia(self):
        return self.tamanio == 0
    

    def __len__(self):
        return self.tamanio
    
    def agregar_al_inicio(self, dato1):
        nuevonodo= Nodo(dato1)
        if self.cabeza == None:
            self.cabeza = nuevonodo
            self.cola = nuevonodo
        
        else:
            nuevonodo.siguiente= self.cabeza
            self.cabeza.anterior = nuevonodo
            self.cabeza = nuevonodo
        self._tamanio +=1

    def agregar_al_final(self, dato):
        nuevonodo=Nodo(dato)
        if self.cola == None:
            self.cabeza = nuevonodo
            self.cola = nuevonodo
        else:
            nuevonodo.anterior = self.cola
            self.cola.siguiente = nuevonodo
            self.cola = nuevonodo
        self._tamanio+=1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception ("Posición Inválida")

        if posicion == 0:
            self.agregar_al_inicio (dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevodato= Nodo(dato)
            actual=self.cabeza
            for _ in range (posicion):
                actual= actual.siguiente
            nuevodato.anterior = actual.anterior
            nuevodato.siguiente = actual
            actual.siguiente = nuevodato
            actual.anterior = nuevodato
            self._tamanio +=1

    def extraer(self,posicion=None):
        if self.esta_vacia():
             raise Exception ("Lista Inválida")
        
        if posicion is None:
            posicion = self.tamanio -1
            
        if posicion < 0:
            posicion += self.tamanio
            
        if posicion < 0 or posicion >= self.tamanio:
            raise Exception ("Posición Inválida")
        if posicion == self.tamanio -1:
            nodo_eliminado= self.cola
            self.cola=self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self._tamanio -=1
            return nodo_eliminado.dato
        elif posicion == 0:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            if self.cabeza != None: 
                self.cabeza.anterior= None
            else:
                self.cola = None
            self._tamanio -=1
            return nodo_eliminado.dato
        else:
            nodo_eliminado = self.cabeza
            for _ in range(posicion):
                nodo_eliminado = nodo_eliminado.siguiente
            anterior = nodo_eliminado.anterior
            siguiente = nodo_eliminado.siguiente
            if anterior is not None:
                anterior.siguiente = siguiente
            if siguiente is not None:   
                siguiente.anterior = anterior
            self._tamanio -=1
            return nodo_eliminado.dato
        
    def copiar(self):
        lista_copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            lista_copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return lista_copia
    
    def invertir(self):
        actual = self.cabeza
        self.cabeza = self.cola
        self.cola = self.cabeza
        while actual is not None:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
   
    def concatenar(self, lista):
        if self.cabeza is None:
            self.cabeza = lista.cabeza
            self.cola = lista.cola
        elif lista.cabeza is not None:
            self.cola.siguiente = lista.cabeza
            lista.cabeza.anterior = self.cola
            self.cola = lista.cola
        self._tamanio += lista.tamanio 
        
    def __add__(self, otralista):
        nueva_lista =  self.copiar()
        nueva_lista.concatenar(otralista)
        return nueva_lista

    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
            





    
if __name__ == "__main__":
    lista1 = ListaDobleEnlazada()
    lista1.agregar_al_inicio(1)
    lista1.agregar_al_inicio(2)
    lista1.agregar_al_final(3)
    lista1.insertar(45,0)



    

        
        
    




        


    