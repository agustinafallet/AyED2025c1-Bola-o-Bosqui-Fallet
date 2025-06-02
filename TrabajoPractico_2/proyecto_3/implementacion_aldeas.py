from grafo import Grafo
from prim import prim

aldeas = []
aldeas_nombre = []
with open("aldeas.txt","r") as archie:
    a = archie.readlines()
    for linea in a:
        linea= linea.strip("\n").split(",")
        aldea_inicial = linea[0]
        aldea_final = linea[1]
        distancia=int(linea[2])
        aldeas_nombre.append([aldea_inicial])
        aldeas.append([aldea_inicial, aldea_final, distancia])
aldeas_norep=[]
for aldea in aldeas_nombre:
            if aldea not in aldeas_norep:
                aldeas_norep.append(aldea)
            else:
                  continue       

aldeas_nombre_ord= sorted(aldeas_norep, key = lambda x:x[0], reverse = False)
print(f"Las aldeas iniciales ordenadas alfabéticamente y sin repetición son:")
for aldea in aldeas_nombre_ord:
    print(f"* {aldea[0]}")
print(" ")
print("*-"*30)

print(f"\nRuta desde Peligros:")

grafo= Grafo()
# Crear el grafo y agregar los vértices
for aldea in aldeas:
    grafo.agregar_vertices(aldea[0])
    grafo.agregar_vertices(aldea[1])
    grafo.agregar_aristas(aldea[0], aldea[1], aldea[2])

# Ejecutar el algoritmo de Prim
prim(grafo, grafo.obtener_vertice('Peligros'))

# Mostrar resumen de envío y recepción de noticias
print("\nResumen de envío y recepción de noticias:")
for v in sorted(grafo, key=lambda x: x.obtener_id()):
    predecesor = v.obtener_predecesor().obtener_id() if v.obtener_predecesor() else None
    vecinas_envio = [w.obtener_id() for w in grafo if w.obtener_predecesor() == v]
    print(f"Aldea: {v.obtener_id()}")
    print(f"  Recibe noticia de: {predecesor if predecesor else 'Ninguna (origen)'}")
    if vecinas_envio:
        print(f"  Envía noticia a: {', '.join(vecinas_envio)}")
    else:
        print(f"  Envía noticia a: Ninguna")

# Suma total de distancias
suma_distancias = 0
for v in grafo:
    if v.obtener_predecesor():
        suma_distancias += v.obtener_ponderacion(v.obtener_predecesor())
print(f"\nSuma total de distancias recorridas por todas las palomas: {suma_distancias}")






