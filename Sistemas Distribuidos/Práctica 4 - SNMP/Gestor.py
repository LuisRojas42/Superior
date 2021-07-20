import socket

HOST = "192.168.100.53"
PORT = 54321
serverAddressPort = (HOST, 54321)
bufferSize = 1024


def menu():
    while True:
        print("1. Conectar")
        print("2. Salir")
        resp = input()
        if resp == "1":
            return
        if resp == "2":
            exit()
        print("\nIngrese una opción válida")

def conexion(OID):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPClientSocket:
        bytesToSend = str.encode(OID)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        return msgFromServer

def Get():
    print("Ingrese la OID:")
    OID = input()
    datos = conexion("1"+OID)
    print(datos[0])

def Set():
    print("Ingrese la OID:")
    OID = input()
    datos = conexion("1"+OID)
    print(datos[0])
    if datos[0] != "b'OID no encontrada'":
        print("Ingrese el nuevo valor:")
        newOID = input()
        datos = conexion("2-"+OID+"-"+newOID)
        print(datos[0])

def opciones():
    while True:
        print("\n1. Get")
        print("2. Set")
        print("3. Salir")
        opc = input()
        if opc == "1":
            Get()
        elif opc == "2":
            Set()
        elif opc == "3":
            exit()
        else:
            print("\nIngrese una opción válida")


menu()
opciones()
