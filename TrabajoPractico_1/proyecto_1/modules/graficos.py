from matplotlib import pyplot as plt
from tiempos import medir_tiempos
from ordenamiento_burbuja import ordenamiento_burbuja
from ordenamiento_quicksort import ordenamiento_quicksort
from ordenamiento_residuos import ordenamiento_de_residuo

def graficar_tiempos(lista_metodos_ord):
    tamanos = [1, 10, 100, 300, 500, 700, 1000]
    
    # figsize es el tamaño de la figura en pulgadas (width, height)
    plt.figure(figsize=(10, 6))

    for metodo_ord in lista_metodos_ord:
        
        tiempos = medir_tiempos(metodo_ord, tamanos)

        # plot es para graficar los tiempos de ordenamiento
        # plot es el método de matplotlib para graficar
        # marker='o' es para poner un punto en cada coordenada
        plt.plot(tamanos, tiempos, marker='o', label=metodo_ord.__name__)

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de tiempos de ordenamiento')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()
    
graficar_tiempos([ordenamiento_burbuja, ordenamiento_de_residuo, ordenamiento_quicksort])
