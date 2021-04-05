# !/usr/bin/env python3

import socket
from pip._vendor.distlib.compat import raw_input

# VARIABLES DE CONEXION
HOST = "192.168.100.188"
PORT = 54321
bufferSize = 1024

# VARIABLES DE JUEGO
# Dificultad = 0


def Menu():
    while True:
        print("\n******GATO DUMMY*******")
        print("\n1. Conectar")
        print("2. Salir")
        opc = raw_input('')

        if opc == "1" or opc == "2":
            if opc == "2":
                print("\nHasta luego")
                exit()
            else:
                return
        else:
            print("Ingrese una opcion disponible")


def Conexion():
    print("\n HOST:")
    HOST = raw_input('')
    print("\n Puerto:")
    PORT = raw_input('')
    # return HOST, int(PORT)
    return "192.168.100.188", 54321


def RecibeDificultad():
    while True:
        print("\nDificultad:")
        print("\n1. Principiante")
        print("2. Avanzado")
        dificultad = raw_input('')

        if dificultad == "1" or dificultad == "2":
            return dificultad
        else:
            print("\nIngrese una dificultad valida")


def DeterminaDificultad(data):
    if len(data.decode('UTF-8')) < 18:
        dificultad = bytes("1", 'ascii')
    else:
        dificultad = bytes("2", 'ascii')
    return dificultad

def tiroCliente(dificultad, TCPClientSocket):
    while True:
        print("\nIngrese su tiro")
        tiro = raw_input('')
        if dificultad.decode('UTF-8') == "1":
            if (tiro[0] == "A" or tiro[0] == "B" or tiro[0] == "C") \
                    and (tiro[1] == "1" or tiro[1] == "2" or tiro[1] == "3"):
                TCPClientSocket.sendall(bytes(tiro, 'ASCII'))
                return
            else:
                print("Ingrese una pocision válida (A1-C3)")
        else:
            if (tiro[0] == "A" or tiro[0] == "B" or tiro[0] == "C" or tiro[0] == "D" or tiro[0] == "E") \
                    and (tiro[1] == "1" or tiro[1] == "2" or tiro[1] == "3" or tiro[1] == "4" or tiro[1] == "5"):
                TCPClientSocket.sendall(bytes(tiro, 'ascii'))
                return
            else:
                print("Ingrese una pocision válida (A1-E5)")


def tiroServidor(TCPClientSocket):
    data = TCPClientSocket.recv(bufferSize)
    if data.decode('UTF-8')[0] != "0":
        print(data.decode('UTF-8'))
    else:
        print(data.decode('UTF-8')[1:])
        return 1


def Inicia(serverAddressPort):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
        TCPClientSocket.connect(serverAddressPort)
        data = TCPClientSocket.recv(bufferSize)

        if data.decode('UTF-8') == "1":
            dificultad = bytes(RecibeDificultad(), 'ascii')
            TCPClientSocket.sendall(dificultad)
            data = TCPClientSocket.recv(bufferSize)
            print(data.decode('UTF-8'))
        else:
            dificultad = DeterminaDificultad(data)
            print(data.decode('UTF-8'))

        while True:
            tiroCliente(dificultad, TCPClientSocket)
            victoria = tiroServidor(TCPClientSocket)
            if victoria:
                print("\nFIN DEL JUEGO")
                break

Menu()
serverAddressPort = Conexion()
Inicia(serverAddressPort)

