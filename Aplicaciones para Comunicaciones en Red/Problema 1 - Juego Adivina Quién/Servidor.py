# !/usr/bin/env python3

import socket
import sys
import threading
import time
import random
import pickle

# VARIABLES DE CONEXION
HOST = " 192.168.100.53"
PORT = 54321
bufferSize = 1024

# VARIABLES DE JUEGO
global tablero
numJugadores = ""

class Turnos(object):
    def __init__(self, start=0):
        self.iniciaJuego = threading.Condition()
        self.numJugadores = 0
        self.conectados = 0
        self.pocision = 1
        self.tablero = []
        self.personajes = "/Users/luisrojas/Desktop/Aplicaciones para comunicaciones en Red/Parte Ubuntu/Aplicaciones para comunicaciones en Red/Problema_Uno_Servidor/personajes"
        self.personaje = ""
        self.ganador = ""

    def iniJuego(self, conn, hilo):
        aux = ""
        while True:
            with self.iniciaJuego:
                if self.numJugadores > self.conectados:
                    msj = "\n\nEsperando jugadores ("+str(self.conectados)+"/"+str(self.numJugadores)+")\n"
                    if aux != msj and hilo == 1:
                        print(msj)
                    aux = msj
                    response = bytes(msj, 'ascii')
                    conn.sendall(response)
                    time.sleep(2)
                    self.iniciaJuego.wait(0)
                else:
                    msj = "\nEsperando jugadores (" + str(self.conectados) + "/" + str(self.numJugadores) + ")\n"
                    if hilo == 1:
                        print(msj)
                    response = bytes(msj, 'ascii')
                    conn.sendall(response)
                    time.sleep(1)
                    msj = "Inicia"
                    if hilo == 1:
                        print(msj)
                    response = bytes(msj, 'ascii')
                    conn.sendall(response)
                    self.iniciaJuego.notify()
                    break;

    def setPosicion(self):
        if (self.pocision) < self.numJugadores:
            self.pocision += 1
        else:
            self.pocision = 1

    def getPosicion(self):
        return (self.pocision)

    def setConectados(self):
        self.conectados += 1

    def getConectados(self):
        return (self.conectados)

    def setNumJugadores(self):
        self.numJugadores += 1

    def getNumJugadores(self):
        return (self.numJugadores)

    def getTablero(self):
        return self.tablero

    def espera(self, turnoHilo, conn):
        while True:
            time.sleep(1)
            if self.pocision != turnoHilo:
                response = bytes(str(self.pocision), 'ascii')
                conn.sendall(response)
            else:
                response = bytes(str(self.pocision), 'ascii')
                conn.sendall(response)
                break

    def armaTablero(self):
        arch = open(self.personajes, 'r')
        for line in arch:
            valores = line.split(",")
            self.tablero.append(valores)
        arch.close()
        for i in range(10):
            print(self.tablero[i])

    def setPersonaje(self, personaje):
        self.personaje = personaje

    def getPersonaje(self):
        return self.personaje

    def setGanador(self, ganador):
        self.ganador = ganador

    def getGanador(self):
        return self.ganador

def servirPorSiempre(socketTcp, listaconexiones, turnos, bloqueo):
    try:
        while True:
            client_conn, client_addr = socketTcp.accept() # Acepta conexion
            print("Conectado a", client_addr)
            gestion_conexiones(listaConexiones, client_conn)
            thread_read = threading.Thread(target=recibir_datos, args=[client_conn, listaConexiones, turnos, bloqueo])
            thread_read.start() # Inicia hilo nuevo para cada conexion
    except Exception as e:
        print(e)


def gestion_conexiones(listaconexiones, client_conn):
    listaconexiones.append(client_conn) # Forma nueva conexion en arreglo de conexiones
    for conn in listaconexiones:
        if conn.fileno() == -1: # Remueve las conexiones finalizadas
            listaconexiones.remove(conn)
    #print("conexiones: ", len(listaconexiones))


def recNumJugadores(conn):
    try:
        global numJugadores
        while True:
            # RECIBE
            time.sleep(1)
            data = conn.recv(1024)
            if not data:
                break
            print("numero de jugadores : ", data.decode('UTF-8'), "")
            numJugadores = repr(data)

            #ENVIA
            response = bytes("Numero de jugadores establecido", 'ascii')
            conn.sendall(response)
            return numJugadores

    except Exception as e:
        print("error en recNumJugadores()")


def armaTablero():
    tablero = "\nTABLERO\n"
    return tablero


def enviaTurno(conn, turnoHilo):
    time.sleep(1)
    response = bytes(str(turnoHilo), 'ascii')
    conn.sendall(response)

def valVictoria(conn, turnos):
    if turnos.getGanador() != "":
        msj = "Fin del juego\n Ha ganado el jugador " + str(turnos.getGanador())
        print(msj)
        response = bytes(msj, 'ascii')
        conn.sendall(response)
        return -1


def personaje(num, turnos):
    if num == 1:
        turnos.setPersonaje("Alex")
    if num == 2:
        turnos.setPersonaje("Luis")
    if num == 3:
        turnos.setPersonaje("Ana")
    if num == 4:
        turnos.setPersonaje("Alexa")
    if num == 5:
        turnos.setPersonaje("Beto")
    if num == 6:
        turnos.setPersonaje("David")
    if num == 7:
        turnos.setPersonaje("Eric")
    if num == 8:
        turnos.setPersonaje("Kenia")
    if num == 9:
        turnos.setPersonaje("Jorge")
    if num == 10:
        turnos.setPersonaje("Maria")
    if 0 >= num or num > 10 :
        turnos.setPersonaje("Maria")
    print("Personaje seleccionado: ", turnos.getPersonaje())

def validarCararcteristica(caract, turnos):
    print(caract)
    for i in range(10):
        if (turnos.tablero[i])[0] == turnos.getPersonaje():
            fila = turnos.tablero[i]
            for j in range(5):
                if caract == fila[j]:
                    return 1
    return 0


def validarPersonaje(personaje, turnos, hilo):
    if personaje == turnos.getPersonaje():
        turnos.setGanador(hilo)
    return 0


def tipoTiro(tiro, turnos, hilo):
    if tiro[0:18] == "tu personaje tiene":
        i = validarCararcteristica(tiro[19:len(tiro)], turnos)
    if tiro[0:15] == "tu personaje es":
        i = validarPersonaje(tiro[16:len(tiro)], turnos, hilo)
    return i

# Hilo para cada conexion
def recibir_datos(conn, listaconexiones, turnos, bloqueo):
    try:
        # VARIABLES DEL HILO
        global tablero
        turnoHilo = len(listaconexiones)
        cur_thread = threading.current_thread()
        turnos.setConectados()
        print("Jugadores conectados: ", turnos.getConectados())

        if len(listaConexiones) == 1: # Si es el primero establece dificultad y numero de jugadores
            response = bytes("1", 'ascii') # Envia "1" para notificar al cliente que es el primero
            conn.sendall(response)
            turnos.armaTablero()
            tablero = turnos.getTablero()
            numJugadores = recNumJugadores(conn)
            for x in range(int(numJugadores[2])):
                turnos.setNumJugadores()
            num = random.randrange(10)
            personaje(num, turnos)
            #print("getNumJugadores: ", turnos.getNumJugadores())

        else: # Si no, lo incorpora a la partida actual
            # ENVIA
            time.sleep(1)
            response = bytes(str(tablero), 'ascii')
            conn.sendall(response)

        time.sleep(1)
        response = bytes(str(tablero), 'ascii')
        conn.sendall(response)

        turnos.iniJuego(conn, turnoHilo)  # Espera a que todos los jugadores se unan

        enviaTurno(conn, turnoHilo)

        while True:
            time.sleep(1)
            v = valVictoria(conn, turnos)
            if v == -1:
                turnos.setPosicion()
                break
            if turnoHilo == 1:
                print("Turno: ", turnos.getPosicion())

            turnos.espera(turnoHilo, conn) # Verifica turno y espera si no lo es

            # RECIBE
            tiro = conn.recv(bufferSize).decode("utf-8")
            if not tiro:
                print("Fin\n\n")
                break
            print("tiro de {}".format(cur_thread.name), ": ", tiro, "")
            i = tipoTiro(tiro, turnos, turnoHilo)

            # ENVIA
            v = valVictoria(conn, turnos)
            if v == -1:
                turnos.setPosicion()
                break
            if i == 1:
                response = bytes("si", 'ascii')
            else:
                response = bytes("no", 'ascii')
            conn.sendall(response)

            # turnos.turno()
            turnos.setPosicion()


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
turnos = Turnos()
bloqueo = threading.Condition()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPServerSocket.bind(serveraddr)
    TCPServerSocket.listen(int(numConn))
    print("El servidor TCP está disponible y en espera de solicitudes\n\n")

    servirPorSiempre(TCPServerSocket, listaConexiones, turnos, bloqueo)