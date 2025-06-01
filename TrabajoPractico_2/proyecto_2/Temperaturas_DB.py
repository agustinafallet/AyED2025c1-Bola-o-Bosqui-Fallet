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
    
    def max_temp_rango(self, fecha1, fecha2):
        rango =[]
        for i in self.base_de_datos:
            if isinstance(fecha1, str):
                fecha1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
            if isinstance(fecha2, str):
                fecha2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
            # Asegurarse de que las fechas están en formato date
            if i.clave>=fecha1 and i.clave<=fecha2:
                rango.append(i.valor)
        return max(rango)
           
    def min_temp_rango(self, fecha1, fecha2):
        rango =[]
        for i in self.base_de_datos:
            if isinstance(fecha1, str):
                fecha1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
            if isinstance(fecha2, str):
                fecha2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
            # Asegurarse de que las fechas están en formato date
            if i.clave>=fecha1 and i.clave<=fecha2:
                rango.append(i.valor)
        return min(rango)
    
    def temp_extremos_rango(self,fecha1,fecha2):
        return f'temperatura minima en el rango dado: {self.min_temp_rango(fecha1, fecha2)}', f"temperatura máxima en rango dado: {self.max_temp_rango(fecha1,fecha2)}"
    
    def borrar_temperatura(self, fecha):
        if isinstance(fecha, str):
            clave = datetime.strptime(fecha, "%d/%m/%Y").date()
        else:
            clave = fecha
        if self.base_de_datos.buscar(clave):
            return self.base_de_datos.eliminar(clave)
        else:
            return False

    def devolver_temperaturas(self,fecha1,fecha2):
        rango =[]
        for i in self.base_de_datos:
            if isinstance(fecha1, str):
                fecha1 = datetime.strptime(fecha1, "%d/%m/%Y").date()
            if isinstance(fecha2, str):
                fecha2 = datetime.strptime(fecha2, "%d/%m/%Y").date()
            # Asegurarse de que las fechas están en formato date
            if i.clave>=fecha1 and i.clave<=fecha2:
                rango.append(i.valor)
        return rango
    
    def cantidad_de_muestras(self):
        return self.base_de_datos.__len__()
    
        
        
            
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
    print(db.max_temp_rango("01/06/2025", "03/06/2025"))  # Output: 22.5
    print(db.min_temp_rango("01/05/2025", "04/06/2025")) #Output: 19.0
    print(db.temp_extremos_rango("01/06/2025", "03/06/2025"))  # Output: (19.0, 22.5)
    print()
    
    print(db.borrar_temperatura("02/06/2025"))  # Output: True (si se eliminó correctamente)
    print(db.devolver_temperatura("02/06/2025"))  # Output: None (si se eliminó correctamente)
    print(db.devolver_temperatura("01/06/2025"))  # Output: 20.0 (si no se eliminó)
    print(db.devolver_temperaturas("01/06/2025", "03/06/2025"))  # Output: [20.0, 19.0]
    print(db.cantidad_de_muestras())  # Output: 2 (si se eliminaron correctamente)