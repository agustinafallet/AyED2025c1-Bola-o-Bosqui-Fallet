from grafo import Grafo
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
print(f"Las aldeas iniciales ordenadas alfabéticamente y sin repetición:{aldeas_nombre_ord}")

if __name__ == "__main__":
      g= Grafo()
      g.agregar_vertices("Aldea")
      for aldea in aldeas:
            g.agregar_vertices(aldea[0])

