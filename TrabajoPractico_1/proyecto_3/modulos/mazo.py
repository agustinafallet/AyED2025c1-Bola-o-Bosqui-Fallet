# mazo.py

from proyecto_2.modules.LDE import ListaDobleEnlazada
from 
# class DequeEmptyError(Exception)
#     if Exception = True 
#         raise Exception ()

class Mazo(ListaDobleEnlazada):
    def __init__(self, agregar_al_final, agregar_al_inicio, extraer, esta_vacia):
        super().__init__(agregar_al_final, agregar_al_inicio, extraer, esta_vacia) 
        self.mazo = ListaDobleEnlazada()
    
    @property
    def mazo(self):
        return self.mazo

    @mazo.setter
    def DequeEmpyError(self, mazo):
        if ListaDobleEnlazada.esta_vacia(mazo) == True:
           raise Exception ("Esta vacia")

    def poner_carta_arriba(self, carta):
        return ListaDobleEnlazada.agregar_al_final(carta)
    
    def poner_carta_abajo(self, carta):
        return ListaDobleEnlazada.agregar_al_inicio(carta)
        



     

