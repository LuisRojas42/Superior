import archivo
import mochila
import objeto
import evolucion
import rmhc

if __name__ == '__main__':
    peso_max = 15
    max_iteration = 200
    print("peso maximo es: "+str(peso_max))
    print("limite de iteraciones de: "+str(max_iteration))
    objetos = archivo.leer("objetos.txt")
    lines = objetos.readlines()
    knapsack = rmhc.rmhc(peso_max,max_iteration)

    for i in lines:
        a = i.split(",")
        knapsack.agregar_objeto(int(a[0]), int(a[1]))

    print("Muestra de objetos de la mochila\n"+knapsack.mochila.obtener_lista_objetos())
    print(knapsack.rmhc())
"""
    objetos = archivo.leer("objetos.txt")
    lines = objetos.readlines()
    #print(lines)
    objetos.close()

    obj = objeto.objeto(1,2)
    print(obj.detalles())

    moch = mochila.mochila([],15)
    moch.agregar_elemento(3,4)
    print(moch.obtener_beneficio())
    print(moch.obtener_peso())
    print(moch.obtener_lista_objetos())
    print(moch.obtener_objetos_seleccionados())

    #print(cadena.cadena.recorrer(2))
    list = [1,2,3]
    ev = evolucion.evolucion
    print(ev.cadena_random(list))
    print(ev.obtner_b(4))
    print(ev.evolucion(1, 3))

    rm = rmhc.rmhc()
    rm.agregar_objeto(5,6)
    rm.rmhc()
"""




