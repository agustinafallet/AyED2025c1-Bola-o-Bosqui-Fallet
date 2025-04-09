def ordenamiento_quicksort(lista):
    for llenarRanura in range(len(lista)-1,0,-1):
       posicionDelMayor=0
       for ubicacion in range(1,llenarRanura+1):
           if lista[ubicacion]>lista[posicionDelMayor]:
               posicionDelMayor = ubicacion

       temp = lista[llenarRanura]
       lista[llenarRanura] = lista[posicionDelMayor]
       lista[posicionDelMayor] = temp
    return lista

if __name__ == "__main__": 
    import random as r
    lista=[r.randint(10000,50000) for _ in range(1,500)]

    lista_quicksort=ordenamiento_quicksort(lista)

    lista_sorteada=sorted(lista)
    assert lista_quicksort == lista_sorteada
