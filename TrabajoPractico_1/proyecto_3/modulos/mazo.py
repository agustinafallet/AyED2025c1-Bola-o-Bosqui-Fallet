# -*- coding: utf-8 -*-

from modulos.ListaDobleEnlazada import ListaDobleEnlazada


class DequeEmptyError(Exception):
    pass

class Mazo(ListaDobleEnlazada):
    def __init__(self): 
        super().__init__()  
        
    
    def poner_carta_arriba(self, carta):
        self.agregar_al_inicio(carta)
    
    def poner_carta_abajo(self, carta):
        self.agregar_al_final(carta)
    
    
    def sacar_carta_arriba(self, mostrar=False):
        if self.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        carta = self.extraer(0)
        if mostrar:
            carta.visible = True
        return carta



     

