# !/usr/bin/env python3

import socket
import sys
import threading
from random import randint

# VARIABLES DE CONEXION
HOST = "192.168.100.188"
PORT = 54321
bufferSize = 1024

# VARIABLES DE JUEGO
global tablero
dificultad = ""


def servirPorSiempre(socketTcp, listaconexiones):
    try:
        while True:
            client_conn, client_addr = socketTcp.accept() # Acepta conexion
            print("Conectado a", client_addr)
            gestion_conexiones(listaConexiones, client_conn)
            thread_read = threading.Thread(target=recibir_datos, args=[client_conn, listaConexiones])
            thread_read.start() # Inicia hilo nuevo para cada conexion
    except Exception as e:
        print(e)


def gestion_conexiones(listaconexiones, client_conn):
    listaconexiones.append(client_conn) # Forma nueva conexion en arreglo de conexiones
    for conn in listaconexiones:
        if conn.fileno() == -1: # Remueve las conexiones finalizadas
            listaconexiones.remove(conn)
    print("conexiones: ", len(listaconexiones))


def recDificultad(conn):
    try:
        global dificultad
        while True:
            # RECIBE
            data = conn.recv(1024)
            if not data:
                break
            print("dificultad : ", repr(data), "")
            dificultad = repr(data)

            #ENVIA
            response = bytes("Dificultad establecida", 'ascii')
            conn.sendall(response)
            return dificultad

    except Exception as e:
        print("error en recDificultad()")


def armaTablero(dificultad):
    if dificultad == "b'1'":
        tablero = "\n---\n---\n---"
    elif dificultad == "b'2'":
        tablero = "\n-----\n-----\n-----\n-----\n-----"
    return tablero


def tiroCliente(tiro, dificultad):
    if dificultad == "b'1'":
        if tiro[0] == "A":
            lugar = 4 * (int(tiro[1]) - 1) + 1
        if tiro[0] == "B":
            lugar = 4 * (int(tiro[1]) - 1) + 2
        if tiro[0] == "C":
            lugar = 4 * (int(tiro[1]) - 1) + 3
        if tiro[0] == "D":
            lugar = 4 * (int(tiro[1]) - 1) + 4
        if tiro[0] == "E":
            lugar = 4 * (int(tiro[1]) - 1) + 5
    elif dificultad == "b'2'":
        if tiro[0] == "A":
            lugar = 6 * (int(tiro[1]) - 1) + 1
        if tiro[0] == "B":
            lugar = 6 * (int(tiro[1]) - 1) + 2
        if tiro[0] == "C":
            lugar = 6 * (int(tiro[1]) - 1) + 3
        if tiro[0] == "D":
            lugar = 6 * (int(tiro[1]) - 1) + 4
        if tiro[0] == "E":
            lugar = 6 * (int(tiro[1]) - 1) + 5
    else:
        lugar = 99
    return lugar


def tiroServidor(lugar, posiciones, dificultad):
    while True:
        if dificultad == "b'1'":
            numran = randint(1, 3)
            if numran == 1:
                numran = randint(1, 3)
            if numran == 2:
                numran = randint(5, 7)
            if numran == 3:
                numran = randint(9, 11)
            if numran != lugar:
                if posiciones.find(str(numran)) < 0:
                    return numran
        elif dificultad == "b'2'":
            numran = randint(1, 5)
            if numran == 1:
                numran = randint(1, 5)
            if numran == 2:
                numran = randint(7, 11)
            if numran == 3:
                numran = randint(13, 17)
            if numran == 4:
                numran = randint(19, 23)
            if numran == 5:
                numran = randint(25, 29)
            if numran != lugar:
                if posiciones.find(str(numran)) < 0:
                    return numran


def insLugares(lugarCliente, lugarServidor, tablero, posiciones):
    aux = 0
    nuevoTablero = ""
    for x in tablero:
        if aux == lugarCliente:
            nuevoTablero = nuevoTablero + "x"
            posiciones = posiciones + str(aux) + "-"
        elif aux == lugarServidor:
            nuevoTablero = nuevoTablero + "o"
            posiciones = posiciones + str(aux) + "-"
        else:
            nuevoTablero = nuevoTablero + x
        aux = aux + 1
    tablero = nuevoTablero
    return tablero, posiciones


def actTablero(tablero, tiro, posiciones, dificultad):
    lugarCliente = tiroCliente(tiro, dificultad)
    lugarServidor = tiroServidor(lugarCliente, posiciones, dificultad)
    tablero, posiciones = insLugares(lugarCliente, lugarServidor, tablero, posiciones)
    print("Lugar cliente: ", lugarCliente, " y lugar servidor: ", lugarServidor)
    print("ocupados: ", posiciones)
    print(tablero)
    return tablero, posiciones


def valVictoria(dificultad, tab):
    if dificultad == "b'1'":
        if tab[1] == tab[2] and tab[2] == tab[3] and tab[1] != "-":
            return True
        if tab[5] == tab[6] and tab[6] == tab[7] and tab[5] != "-":
            return True
        if tab[9] == tab[10] and tab[10] == tab[11] and tab[9] != "-":
            return True
        if tab[1] == tab[5] and tab[5] == tab[9] and tab[1] != "-":
            return True
        if tab[2] == tab[6] and tab[6] == tab[10] and tab[2] != "-":
            return True
        if tab[3] == tab[7] and tab[7] == tab[11] and tab[3] != "-":
            return True
    elif dificultad == "b'2'":
        if tab[1:6].find("xxxxx") >= 0 or tab[7:12].find("xxxxx") >= 0 or tab[13:18].find("xxxxx") >= 0 \
                or tab[19:24].find("xxxxx") >= 0 or tab[25:30].find("xxxxx") >= 0:
            return True
        if tab[1] == tab[7] and tab[7] == tab[13] and tab[13] == tab[19] \
                and tab[19] == tab[25] and tab[1] != "-":
            return True
        if tab[2] == tab[8] and tab[8] == tab[14] and tab[14] == tab[20] \
                and tab[20] == tab[26] and tab[2] != "-":
            return True
        if tab[3] == tab[9] and tab[9] == tab[15] and tab[15] == tab[21] \
                and tab[21] == tab[27] and tab[3] != "-":
            return True
        if tab[4] == tab[10] and tab[10] == tab[16] and tab[16] == tab[22] \
                and tab[22] == tab[28] and tab[4] != "-":
            return True
        if tab[5] == tab[11] and tab[11] == tab[17] and tab[17] == tab[23] \
                and tab[23] == tab[29] and tab[29] != "-":
            return True

# Hilo para cada conexion
def recibir_datos(conn, listaconexiones):
    try:
        # VARIABLES DEL HILO
        global dificultad
        global tablero
        global posiciones
        cur_thread = threading.current_thread()

        if len(listaConexiones) == 1: # Si es el primero establece dificultad
            response = bytes("1", 'ascii')
            conn.sendall(response)
            dificultad = recDificultad(conn)
            tablero = armaTablero(dificultad)
            posiciones = ""
        else: # Si no incorpora a la partida actual
            # ENVIA
            response = bytes(tablero, 'ascii')
            conn.sendall(response)
        while True:
            # RECIBE
            tiro = conn.recv(bufferSize).decode("utf-8")
            if not tiro:
                print("Fin\n\n")
                break
            print("tiro de {}".format(cur_thread.name), ": ", tiro, "")

            tablero, posiciones = actTablero(tablero, tiro, posiciones, dificultad)
            victoria = valVictoria(dificultad, tablero)

            # ENVIA
            if victoria == True:
                tablero = "0"+tablero
                response = bytes(tablero, 'ascii')
            else:
                response = bytes(tablero, 'ascii')
            conn.sendall(response)

    except Exception as e:
        print(e)
    finally:
        conn.close()


listaConexiones = [] # Arreglo conexiones
host, port, numConn = sys.argv[1:4]

if len(sys.argv) != 4: # Parametros de inicio
    print("usage:", sys.argv[0], "<host> <port> <num_connections>")
    sys.exit(1)

serveraddr = (host, int(port)) # Tupla de datos de conexion

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPServerSocket.bind(serveraddr)
    TCPServerSocket.listen(int(numConn))
    print("El servidor TCP está disponible y en espera de solicitudes\n\n")

    servirPorSiempre(TCPServerSocket, listaConexiones)
