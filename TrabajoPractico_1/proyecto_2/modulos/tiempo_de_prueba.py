
from random import randint
import time
from ListaDobleEnlazada import ListaDobleEnlazada #__len__, copiar, invertir 

def medir_tiempos(metodo, tamanos):
    tiempos = []
    for n in tamanos:
        lista = ListaDobleEnlazada()
        for _ in range(n):
            lista.agregar_al_final(randint(1, 10000))
        inicio = time.perf_counter()
        metodo(lista)
        fin = time.perf_counter()
        tiempos.append(fin - inicio)
    return tiempos

def graficar_resultados(tiempos, labels, tamanos):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    for tiempo, label in zip(tiempos, labels):
        plt.plot(tamanos, tiempo, marker='o', label=label)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    tamanos = [1, 10, 100, 300, 500, 700, 1000]
    tiempo_len = medir_tiempos(len, tamanos)
    tiempo_copiar = medir_tiempos(ListaDobleEnlazada.copiar, tamanos)
    tiempo_invertir = medir_tiempos(ListaDobleEnlazada.invertir, tamanos)
    
    graficar_resultados([tiempo_len, tiempo_copiar, tiempo_invertir],
                        ["len()", "copiar()", "invertir()"], tamanos)
    