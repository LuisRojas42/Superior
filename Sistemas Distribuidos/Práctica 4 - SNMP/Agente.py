from shutil import copyfile
import socket

HOST = "192.168.100.53"
PORT = 54321
bufferSize = 1024
MIB = '/Users/luisrojas/Desktop/Aplicaciones para comunicaciones en Red/practica4_Cliente/MIB.txt'
msgFromServer = "empty"

def abrir_MIB(ruta, permiso): # r: leer, w: escribir, r+: leer y escribir
    MIB = open(ruta, permiso)
    return MIB

def get(MIB, OID):
    contenido = MIB.read()
    return contenido

def set(archivo, texto):
    archivo.write('\n'+ texto)

def buscaOID(rutaOID):
    arch = abrir_MIB(MIB, 'r')
    for line in arch:
        valores = line.split("-")
        if valores[0] == rutaOID:
            print("encontrada")
            try:
                encontrado = valores[1] + ": " + valores[2]
            except:
                encontrado = valores[1]
            arch.close()
            return encontrado
    encontrado = "OID no encontrada"
    arch.close()
    print(encontrado)
    return encontrado

def modificaOID(param):
    param = param.split("-")
    arch = abrir_MIB(MIB, 'r')
    lineas = arch.readlines()
    arch.close()
    arch = abrir_MIB(MIB, 'w')
    for line in lineas:
        valores = line.split("-")
        if valores[0] != param[1]:
            arch.write(line)
        else:
            arch.write(valores[0] + "-" + valores[1].rstrip('\n') + "-" + param[2] + "\n")

    arch.close()
    encontrado = "exito"
    print(encontrado)
    arch.close()
    return encontrado

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.bind((HOST, PORT))

    print("UDP server up and listening")

    while True:

        data,address = UDPServerSocket.recvfrom(bufferSize)

        print("Client IP Address:{}".format(address))
        if (data.decode('UTF-8'))[0] == "1": # GET
            msgFromServer = buscaOID((data.decode('UTF-8'))[1:])
        if (data.decode('UTF-8'))[0] == "2": # SET
            msgFromServer = modificaOID((data.decode('UTF-8')))

        bytesToSend = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)