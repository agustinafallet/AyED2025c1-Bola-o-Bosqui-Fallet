# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import random as r

def ordenamiento_burbuja (lista):
    for numero in range(len(lista)-1,0,-1):
        for i in range(numero):
            if lista[i]>lista[i+1]:
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista
    
                
if __name__ == "__main__":              
    lista_de_numeros=[r.randint(10000,50000) for i in range(500)]
    lista_original_OB=lista_de_numeros
    lista_ordenada_por_ordenamiento_burbuja=ordenamiento_burbuja(lista_de_numeros)

    print(f"la lista original:{lista_original_OB} ordenada utilizando ordenamiento burbuja:{lista_ordenada_por_ordenamiento_burbuja}")

    lista_ordenada_por_sorted=sorted(lista_original_OB, reverse=False)

    print (f"la lista ordeanada utilizando sorted: {lista_ordenada_por_sorted}")

    if lista_ordenada_por_ordenamiento_burbuja == lista_ordenada_por_sorted:
        
        print("las listas coinciden")
    else:
        print("las listas no coinciden")







