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
        tamanio= 0

    def esta_vacia(self):
        if tamanio == 0:
            return True

    def __len__(self):
        return tamanio
    
    def agregar_al_inicio(self, dato):
        nuevonodo= Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevonodo
            self.cola = nuevonodo
        
        else:
            nuevonodo.siguiente= self.cabeza
            self.cabeza.anterior = nuevonodo
            self.cabeza = nuevonodo
        tamanio +=1

    def agregar_al_final(self, dato):
        nuevonodo=Nodo(dato)
        if self.cola == None:
            self.cabeza = nuevonodo
            self.cola = nuevonodo
        else:
            nuevonodo.anterior = self.cola
            self.cola.siguiente = nuevonodo
            self.cola = nuevonodo
        tamanio+=1

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
            actual.anterior.siguiente = nuevodato
            actual.anterior = nuevodato
            tamanio +=1

    def extraer(self,posicion):
        if posicion < 0 or posicion > self.tamanio:
             raise Exception ("Posición Inválida")
        
        if posicion == None: #or posicion == self.tamanio
            nodo_eliminado= self.cola
            self.cola=self.cola.anterior
            return nodo_eliminado

        
        anterior.siguiente= self.siguiente
        siguiente.anterior = self.anterior
        return 


        


    