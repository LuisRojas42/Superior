# !/usr/bin/env python3

import socket
# from pip._vendor.distlib.compat import raw_input
import time
import ast
import speech_recognition as sr

r = sr.Recognizer()

# VARIABLES DE CONEXION
HOST = "192.168.100.53"
PORT = 54321
bufferSize = 1024

# VARIABLES DE JUEGO
NumMaxJugadores = 4


# done
def Menu():
    while True:
        print("\n******Adivina Quien*******")
        print("\n1. Conectar")
        print("2. Salir")
        # opc = raw_input('')
        opc = str(input(''))

        if opc == "1" or opc == "2":
            if opc == "2":
                print("\nHasta luego")
                exit()
            else:
                return
        else:
            print("Ingrese una opcion disponible")


# done
def Conexion():
    print("\n HOST:")
    # HOST = raw_input('')
    HOST = input('')
    print("\n Puerto:")
    # PORT = raw_input('')
    PORT = input('')
    return HOST, int(PORT)
    # return "192.168.100.188", 54321


# done
def RecibeNumJugadores():
    while True:
        print("\nNumero de jugadores:")
        # numJugadores = int(raw_input(''))
        numJugadores = int(input(''))

        if numJugadores > 0 and numJugadores < NumMaxJugadores:
            return str(numJugadores)
        else:
            print("\nIngrese un numero valido (1-3)")


# done
def esPrimerJugador(TCPClientSocket):
    data = TCPClientSocket.recv(bufferSize)
    if data.decode('UTF-8') == "1":
        numJugadores = bytes(RecibeNumJugadores(), 'ascii')
        TCPClientSocket.sendall(numJugadores)
        data = TCPClientSocket.recv(bufferSize)
        print(data.decode('UTF-8'))
    else:
        try:
            tab = ast.literal_eval(data.decode('UTF-8'))
            #for i in range(10):
                #print(tab[i])
        except:
            print("..", tab)


# done
def esperaJugadores(TCPClientSocket):
    aux = ""
    while True:
        espera = TCPClientSocket.recv(bufferSize)
        if aux != espera:
            print(espera.decode('UTF-8'))
        aux = espera
        if espera.decode('UTF-8') == "Inicia":
            print("\n**REGLAS**")
            print("1. Para tirar: ¿Tu jugador tiene...?")
            print("2. Para ganar: ¿tu personaje es...?\n")
            break;


def recibeTablero(TCPClientSocket):
    while True:
        tablero = TCPClientSocket.recv(bufferSize)
        if tablero.decode('UTF-8') != "0":
            #for i in range(10):
                #print(tablero[i])
            #print(ast.literal_eval(tablero.decode('UTF-8')))
            return ast.literal_eval(tablero.decode('UTF-8'))


# done
def recibeTurno(TCPClientSocket):
    while True:
        turno = TCPClientSocket.recv(bufferSize)
        if turno.decode('UTF-8') != "0":
            print("Turno asignado: ", turno.decode('UTF-8'))
            return turno.decode('UTF-8')


# done
def validaTurno(TCPClientSocket, turno):
    aux = ""
    while True:
        posicion = TCPClientSocket.recv(bufferSize)
        if posicion.decode('UTF-8') != turno:
            msj = "En turno: " + str(posicion.decode('UTF-8'))
            if aux != msj:
                print(msj)
                print("Espere su turno\n")
            aux = msj
        else:
            print("Tu turno")
            break;
        time.sleep(.1)


def validaVoz(text):
    if text[0:18] == "tu personaje tiene" or text[0:15] == "tu personaje es":
        return 1
    else:
        return 0

# not yet
def tiroCliente(TCPClientSocket):
    while True:
        try:
            with sr.Microphone() as source:
                print("Di algo!")
                audio = r.listen(source)
                text = r.recognize_google(audio, language="es-ES")
                i = validaVoz(text)
                if i:
                    print("Dijiste: ", text)
                    break;
                else:
                    print("No te entendí, prueba de nuevo, (", text, ")")
        except:
            print("Error, prueba de nuevo")

    TCPClientSocket.sendall(bytes(text, 'ASCII'))
    return text

def actTablero(tablero, tiro):
    aux = []
    for i in range(len(tablero)):
        for j in range(6):
            if tablero[i][j] == tiro:
                aux.append(tablero[i])
    print("-> ",tiro)
    print("\n\n\n", tablero, "\n\n\n")
    print(aux, "\n\n\n")
    return aux

# not yet
def respServidor(TCPClientSocket, tablero, tiro):
    tab = TCPClientSocket.recv(bufferSize)
    if tab.decode('UTF-8')[0] != "0":
        try:
            tab = ast.literal_eval(tab.decode('UTF-8'))
            for i in range(10):
                print(tab[i])
            return tablero
        except:
            print("Respuesta: ", tab.decode('UTF-8'))
            if tab.decode('UTF-8') == "si":
                aux = actTablero(tablero, tiro[19:len(tiro)])
                return aux
            return tablero
    else:
        print(tab.decode('UTF-8')[1:])  # codigo "1" para victoria
        return 1


def Inicia(serverAddressPort):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
        TCPClientSocket.connect(serverAddressPort)

        # Verifica si es primer jugador
        esPrimerJugador(TCPClientSocket)

        # Recibe tablero
        tablero = recibeTablero(TCPClientSocket)

        # Espera a que todos los jugadores se conecten para empezar
        esperaJugadores(TCPClientSocket)

        # Recibe turno
        turno = recibeTurno(TCPClientSocket)

        # Comienza juego
        while True:
            # Valida turno
            validaTurno(TCPClientSocket, turno)
            time.sleep(1)

            tiro = tiroCliente(TCPClientSocket)
            tablero = respServidor(TCPClientSocket, tablero, tiro)
            if tablero == 1:
                print("\nFIN DEL JUEGO")
                break

            for i in range(len(tablero)):
                print(tablero[i])

Menu()
serverAddressPort = Conexion()
Inicia(serverAddressPort)