from random import randint
import time
from ordenamiento_burbuja import ordenamiento_burbuja
from ordenamiento_quicksort import ordenamiento_quicksort
from ordenamiento_residuos import ordenamiento_de_residuo
def medir_tiempos(metodo_ord, tamanos):
    tiempos_ord_selecc = []

    for n in tamanos:
        datos = [randint(1, 10000) for _ in range(n)]

        inicio = time.perf_counter()
        metodo_ord(datos)
        fin = time.perf_counter()
        tiempos_ord_selecc.append(fin - inicio)
        
        print(f"Tiempo de ordenamiento por seleccion para n={n}: {fin - inicio:.6f} segundos")
    
    return tiempos_ord_selecc

if __name__ == '__main__':
    tamanos = [1, 10, 100, 300, 500, 700, 1000]
    tiempos_ord_burbuja=medir_tiempos(ordenamiento_burbuja,tamanos)
    tiempos_ord_quicksort=medir_tiempos(ordenamiento_quicksort,tamanos)
    tiempos_ord_residuos=medir_tiempos(ordenamiento_de_residuo,tamanos)
    