from arbol_avl import ArbolAVL
from datetime import datetime
from arbol_avl import NodoArbol

class Temperaturas_DB:
    def __init__(self, fecha, temperatura):    
        self.__base_de_datos = ArbolAVL()
        #NodoArbol.clave = fecha  #fecha es ahora la clave de un nodo perteneciente a la base de datos ( Que es un AAVL)
        self.__fecha = fecha     #temp es el valor de bla bla bla
        #NodoArbol.valor = temperatura
        self.__temperatura = temperatura
        
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self,nueva_temperatura):
        self.__temperatura = nueva_temperatura
        
    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha
    
    @property
    def base_de_datos(self):
        return self.__base_de_datos
    
    def guardar_temperatura(self, temperatura, fecha):
        # Si la fecha es datetime, conviértela a date para usar como clave
        if isinstance(fecha, str):  # normaliza la fecha en caso de que tenga formato fecha!!
            clave = datetime.strptime(fecha,"%d/%m/%Y").date()
        else:
            clave = fecha
        self.base_de_datos.agregar(clave, temperatura)
    
    def devolver_temperatura(self,fecha):
        if isinstance (fecha, str): #normaliza la fecha en caso de que tenga formato fecha!!
            clave = datetime.strptime(fecha,"%d/%m/%Y").date()
        else:
            clave = fecha
        for i in self.base_de_datos:
            if i.clave == clave:
                return i.valor
        return None
    
    
            
if __name__ == "__main__":
    # Ejemplo de uso
    db = Temperaturas_DB("01/06/2025", 18.5)

    # Guardar temperaturas con fechas en formato string
    db.guardar_temperatura(20.0, "01/06/2025")
    db.guardar_temperatura(22.5, "02/06/2025")
    db.guardar_temperatura(19.0, "03/06/2025")

    # Consultar temperaturas usando fechas en formato string
    print(db.devolver_temperatura("01/06/2025"))  # Output: 20.0
    print(db.devolver_temperatura("02/06/2025"))  # Output: 22.5
    print(db.devolver_temperatura("03/06/2025"))  # Output: 19.0

    # Consultar una fecha que no existe
    print(db.devolver_temperatura("04/06/2025"))  # Output: None