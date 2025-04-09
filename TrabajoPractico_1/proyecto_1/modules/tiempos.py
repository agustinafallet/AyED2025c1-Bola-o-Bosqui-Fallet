import random as r
import time 

from ordenamiento_burbuja import ordenamiento_burbuja
from ordenamiento_quicksort import ordenamiento_quicksort
from ordenamiento_residuos import ordenamiento_de_residuo

def medir_tiempos(metodo_ord,tamaños):
    tiempos_ord=[]
    for n in tamaños:
        datos = []
        for _ in range(n):
            datos.append(r.randint(1,10000))
    
        inicio = time.perf_counter()
        metodo_ord(datos)
        fin = time.perf_counter()
        tiempos_ord.append(fin - inicio)
        
        print(f"tiempo de ordenamiento por seleccion para n={n}: {fin - inicio:.4f} segundos")
    return tiempos_ord


if __name__ == "__main__":
    lista=[1,2,3,4]
#metodo_bubble=medir_tiempos(ordenamiento_burbuja,lista_de_numeros)
#metodo_residuo=medir_tiempos(ordenamiento_de_residuo,lista_de_numeros)
#metodo_quicksort=medir_tiempos(ordenamiento_quicksort,lista_de_numeros)
medir_tiempos(ordenamiento_burbuja,lista)

       
       
    
        