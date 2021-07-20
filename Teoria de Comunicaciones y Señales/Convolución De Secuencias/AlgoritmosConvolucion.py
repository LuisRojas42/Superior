
def convolucionFinita(Xn, xn0, Hn, hn0):

    filas = []
    convolucion = []

    #Multiplicación término a término
    #Se almacena en filas para despues sumar cada columna
    for i in range(len(Hn)):
        #Se agrega una nueva fila
        filas.insert(i, [])

        #Se agregan 0s al inicio en caso de ser necesario
        for j in range(i):
            filas[i].insert(j, 0)

        #Se hace la multiplicación término a término
        for k in range(len(Xn)):
            mult = Hn[i] * Xn[k]
            filas[i].insert(k + i, mult)

        #Se agregan 0s al final en caso de ser necesario
        #Para terminar con una matriz cuadrada
        for l in range(len(Hn) - i - 1):
            filas[i].append(0)

    #Se suman las columnas
    for i in range(len(filas[0])):
        suma = 0
        for j in range(len(filas)):
            suma = suma + filas[j][i]

        convolucion.insert(i, suma)

    #Se calcula el elemento en n=0
    origen = xn0 + hn0

    return convolucion, origen



def convolucionPeriodica(Xn, xn0, Hn, hn0):
    #X(n) es la secuencia periódica

    filas = []
    result = []
    nuevasfilas = []
    convolucion = []

    # Multiplicación término a término
    # Se almacena en filas para despues sumar cada columna
    for i in range(len(Xn)):
        # Se agrega una nueva fila
        filas.insert(i, [])

        # Se agregan 0s al inicio en caso de ser necesario
        for j in range(i):
            filas[i].insert(j, 0)

        # Se hace la multiplicación término a término
        for k in range(len(Hn)):
            mult = Hn[k] * Xn[i]
            filas[i].insert(k + i, mult)

        # Se agregan 0s al final en caso de ser necesario
        # Para terminar con una matriz cuadrada
        for l in range(len(Xn) - i - 1):
            filas[i].append(0)

    # Se suman las columnas
    for i in range(len(filas[0])):
        suma = 0
        for j in range(len(filas)):
            suma = suma + filas[j][i]

        result.insert(i, suma)

    # En caso de que el vector resultado no sea exactamente divisible
    # entre el periodo de X(n), se agregan 0s al final
    # para que se pueda dividir en bloques de N
    if len(result) % len(Xn) != 0:
        ceros = len(Xn) - len(result) % len(Xn)
        for i in range(ceros):
            result.append(0)

    #Se separa la secuencia resultando en bloques de N
    #Siendo N el periodo de la secuencia periódica X(n)
    #Y apilando los bloques uno debajo del otro
    for i in range(int (len(result) / len(Xn))):
        nuevasfilas.insert(i, [])
        for j in range (len(Xn)):
            index = (i * len(Xn)) + j
            nuevasfilas[i].insert(j, result[index])

    #Se suman las nuevas filas
    for i in range(len(nuevasfilas[0])):
        suma = 0
        for j in range(len(nuevasfilas)):
            suma = suma + nuevasfilas[j][i]

        convolucion.insert(i, suma)


    #Se calcula el elemento en n=0
    origen = xn0 + hn0
    origen = origen % len(Xn)

    return convolucion, origen



def convolucionCircular(Xn, xn0, Hn, hn0):
    #Ambas secuencias son periódicas

    filas = []
    result = []
    nuevasfilas = []
    convolucion = []

    # Multiplicación término a término
    # Se almacena en filas para despues sumar cada columna
    for i in range(len(Xn)):
        # Se agrega una nueva fila
        filas.insert(i, [])

        # Se agregan 0s al inicio en caso de ser necesario
        for j in range(i):
            filas[i].insert(j, 0)

        # Se hace la multiplicación término a término
        for k in range(len(Hn)):
            mult = Hn[k] * Xn[i]
            filas[i].insert(k + i, mult)

        # Se agregan 0s al final en caso de ser necesario
        # Para terminar con una matriz cuadrada
        for l in range(len(Xn) - i - 1):
            filas[i].append(0)

    # Se suman las columnas
    for i in range(len(filas[0])):
        suma = 0
        for j in range(len(filas)):
            suma = suma + filas[j][i]

        result.insert(i, suma)

    #Se utiliza el periodo mayor (N)
    if len(Xn) >= len(Hn):
        periodo = len(Xn)
    else:
        periodo = len(Hn)

    #En caso de que el vector resultado no sea exactamente divisible
    # entre el periodo, se agregan 0s al final
    # para que se pueda dividir en bloques de N
    if len(result) % periodo != 0:
        ceros = periodo - len(result) % periodo
        for i in range(ceros):
            result.append(0)

    #Se separa la secuencia resultando en bloques de N
    #Siendo N el periodo mayor de las secuencias
    #Y apilando los bloques uno debajo del otro
    for i in range(int (len(result) / periodo)):
        nuevasfilas.insert(i, [])
        for j in range(periodo):
            index = (i * periodo) + j
            nuevasfilas[i].insert(j, result[index])

    #Se suman las nuevas filas
    for i in range(len(nuevasfilas[0])):
        suma = 0
        for j in range(len(nuevasfilas)):
            suma = suma + nuevasfilas[j][i]

        convolucion.insert(i, suma)


    #Se calcula el elemento en n=0
    origen = xn0 + hn0
    origen = origen % periodo

    return convolucion, origen


if __name__ == '__main__':
    #EJEMPLOS

    #CONVOLUCION FINITA

    x = [1, 0, -4, 3]
    xn0 = 2             #El valor -4
    h = [1, 2, 3]
    hn0 = 0             #El valor 1

    Conv, origen = convolucionFinita(x, xn0, h, hn0)

    print("CONVOLUCIÓN FINITA")
    print("Vector Resultado:", end=' ')
    for x in Conv:
        print(x, end=' ')
    print("")
    print("Origen: {}, valor -> {}".format(origen, Conv[origen]))
    print("")


    x = [-10, 4, 0.25, -1, 0, 2]
    xn0 = 2
    h = [3, -7, 11, 9, -5]
    hn0 = 3

    Conv, origen = convolucionFinita(x, xn0, h, hn0)

    print("CONVOLUCIÓN FINITA")
    print("Vector Resultado:", end=' ')
    for x in Conv:
        print(x, end=' ')
    print("")
    print("Origen: {}, valor -> {}".format(origen, Conv[origen]))
    print("")

    #CONVOLUCION PERIÓDICA

    x = [2, 3]
    xn0 = 1
    h = [-5, 7, 4, 0, 1]
    hn0 = 3

    Conv, origen = convolucionPeriodica(x, xn0, h, hn0)

    print("CONVOLUCIÓN PERIÓDICA")
    print("Vector Resultado:", end=' ')
    for x in Conv:
        print(x, end=' ')
    print("")
    print("Origen: {}, valor -> {}".format(origen, Conv[origen]))
    print("")


    x = [2, 3, 1]
    xn0 = 2
    h = [4, 1, 2, -2]
    hn0 = 1

    Conv, origen = convolucionPeriodica(x, xn0, h, hn0)

    print("CONVOLUCIÓN PERIÓDICA")
    print("Vector Resultado:", end=' ')
    for x in Conv:
        print(x, end=' ')
    print("")
    print("Origen: {}, valor -> {}".format(origen, Conv[origen]))
    print("")


    x = [-1, 4]
    xn0 = 0
    h = [3, 6, 2]
    hn0 = 0

    Conv, origen = convolucionCircular(x, xn0, h, hn0)

    print("CONVOLUCIÓN CIRCULAR")
    print("Vector Resultado:", end=' ')
    for x in Conv:
        print(x, end=' ')
    print("")
    print("Origen: {}, valor -> {}".format(origen, Conv[origen]))
    print("")


    xp = [7, 1, -5]
    xn0p = 1
    hp = [10, 1, 1, 2, -2, 3]
    hn0p = 0

    Conv, origen = convolucionCircular(xp, xn0p, hp, hn0p)

    print("CONVOLUCIÓN CIRCULAR")
    print("Vector Resultado:", end=' ')
    for x in Conv:
        print(x, end=' ')
    print("")
    print("Origen: {}, valor -> {}".format(origen, Conv[origen]))
    print("")