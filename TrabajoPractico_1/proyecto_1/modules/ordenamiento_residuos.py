import random as r

def ordenamiento_de_residuo(lista):
    contador_sublistas = len(lista) // 2
    while contador_sublistas > 0:

        for posicion_inicio in range(contador_sublistas):
            brecha(lista, posicion_inicio, contador_sublistas)


        contador_sublistas = contador_sublistas // 2

    return lista

def brecha(lista, inicio, brecha):
    for i in range(inicio + brecha, len(lista), brecha):

        valor_actual = lista[i]
        posicion = i

        while posicion >= brecha and lista[posicion - brecha] > valor_actual:
            lista[posicion] = lista[posicion - brecha]
            posicion = posicion - brecha

        lista[posicion] = valor_actual
if __name__ == "__main__":     
    lista=[r.randint(10000,50000) for _ in range(1,500)]
    lista_basura=ordenamiento_de_residuo(lista)

    lista_sorteada=sorted(lista)

    assert lista_basura == lista_sorteada