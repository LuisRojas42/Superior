import random
import math
import copy


objetos = [
    [4,  2, 2, 10, 1],  # Beneficio
    [12, 2, 1, 4, 1]    # Peso
]

mochila = [0,0,0,0,0]

peso_maximo = 15

def beneficio(mochila):
    beneficio = 0
    for i in range(0, len(mochila)):
        beneficio += mochila[i] * objetos[0][i]
    return beneficio

def peso(mochila):
    peso = 0
    for i in range(0, len(mochila)):
        peso += mochila[i] * objetos[1][i]
    return peso

def estado_aleatorio():
    random.seed(a = None)
    estado = [0]*len(objetos[0])
    while True:
        for i in range(0, len(estado)):
            estado[i] = random.randint(0, 1)
        if peso(estado) < peso_maximo:
            break
    return estado

def vecino(estado):
    estado_vecino = copy.copy(estado)
    while True:
        posicion_aleatoria = random.randint(0,len(estado)-1)
        posicion_fija = random.randint(0,len(estado)-1)
        if posicion_aleatoria != posicion_fija:
            estado_vecino[posicion_aleatoria] = (estado_vecino[posicion_aleatoria]+1)%2
            if peso(estado_vecino) < peso_maximo and estado != estado_vecino:
                break;
    return estado_vecino


def sa(temperatura_maxima, temperatura_minima, enfriamiento, ciclos_por_temp):
    estado = estado_aleatorio()
    
    print("mochila inicial:"+str(estado))
    print("Temperatura máxima:"+str(temperatura_maxima))
    print("Temperatura mínima:"+str(temperatura_minima))
    print("Enfriamento:"+str(enfriamiento))
    print("\n")

    temperatura = temperatura_maxima
    while temperatura >= temperatura_minima:
        for i in range(ciclos_por_temp):
            estado_vecino = vecino(estado)
            delta = beneficio(estado)-beneficio(estado_vecino)

            print("Estado:"+str(estado)+" Estado vecino:"+str(estado_vecino))
            print("Beneficio:"+str(beneficio(estado))+" Nuevo beneficio:"+str(beneficio(estado_vecino)))
            print("Delta:"+str(delta)+" Temperatura:"+str(temperatura)+" Exp:"+str(math.exp(-delta/temperatura)))

            if delta > 0: 
                if random.uniform(0,1) < math.exp(-delta/temperatura):
                    estado = estado_vecino
                    print("\tSe acepta error, nuevo estado:"+str(estado))
            else:
                estado = estado_vecino
                print("\tNuevo mejor estado: "+str(estado))
            print("\n")
        temperatura = temperatura - enfriamiento
        print("\n")

    return estado

mochila = sa(50,0.01, 0.88, 3)
print(mochila)
