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

class ListaDoblementeEnlazada:
    def __init__(self, dato):
        self.cabeza = None
        self.cola = None
        self.tamanio= 0

    def esta_vacia(self):
        if self.tamanio == 0:
            return True

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
        self.tamanio +=1

    def agregar_al_final(self, dato):
        nuevonodo=Nodo(dato)
        if self.cola == None:
            self.cabeza = nuevonodo
            self.cola = nuevonodo
        else:
            nuevonodo.anterior = self.cola
            self.cola.siguiente = nuevonodo
            self.cola = nuevonodo
        self.tamanio+=1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion >= self.tamanio:
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
            self.tamanio +=1

    def extraer(self,posicion):
        if posicion < 0 or posicion > self.tamanio:
             raise Exception ("Posición Inválida")
        
        if posicion == None or posicion == self.tamanio:
            nodo_eliminado= self.cola
            self.cola=self.cola.anterior
            self.tamanio -=1
            return nodo_eliminado
        elif posicion == 0:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
            self.tamanio -=1
            return nodo_eliminado
        else:
            nodo_eliminado = self.cabeza
            for _ in range(posicion):
                nodo_eliminado = nodo_eliminado.siguiente
            anterior = nodo_eliminado.anterior
            siguiente = nodo_eliminado.siguiente
            anterior = siguiente
            siguiente = anterior
            self.tamanio -=1
            return nodo_eliminado
    #copiar(): Realiza una copia de la lista elemento a elemento y devuelve la copia.
    # Verificar que el orden de complejidad de este método sea O(n) y no O(n2).
    def copiar(self):
        lista_copia = ListaDoblementeEnlazada(None)
        actual = self.cabeza
        while actual is not None:
            lista_copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return lista_copia
    def invertir(self):
        lista_invertida = ListaDoblementeEnlazada(None)
        actual = self.cabeza
        while actual is not None:
            lista_invertida.agregar_al_inicio(actual.dato)
            actual = actual.siguiente
        return lista_invertida
    #concatenar(Lista): Recibe una lista como argumento y retorna la lista actual con la lista pasada como parámetro concatenada al 
    # final de la primera.
    def concatenar(self, lista):
        if self.cabeza is None:
            self.cabeza = lista.cabeza
            self.cola = lista.cola
        elif lista.cabeza is not None:
            self.cola.siguiente = lista.cabeza
            lista.cabeza.anterior = self.cola
            self.cola = lista.cola
        self.tamanio += lista.tamanio
    #__add__(Lista): El resultado de “sumar” dos listas debería ser una nueva lista con los elementos de la primera lista y 
    # los de la segunda. Aprovechar el método concatenar para evitar repetir código.
    def __add__(self, otralista):
        nueva_lista =  ListaDoblementeEnlazada(None)
        nueva_lista.cabeza = self.cabeza
        nueva_lista.cola = self.cola
        nueva_lista.tamanio = self.tamanio
        nueva_lista.concatenar(otralista)
        return nueva_lista
#iterar sobre la lista
    def __iter__(self):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
            
lista1 = ListaDoblementeEnlazada(None)
lista1.agregar_al_inicio(1)
lista1.agregar_al_inicio(2)
lista1.agregar_al_final(3)
lista1.insertar(45,1)
print(lista1.extraer(1).dato)
print(lista1.extraer(0).dato)
print(lista1.__iter__())
    
    



    

        
        
    




        


    