from pip._vendor.distlib.compat import raw_input
import xmlrpc.client

# CONEXION
s = xmlrpc.client.ServerProxy('http://192.168.100.188:8000')

def CREATE():
    print("Nombre del Archivo a crear: ")
    arch = input()
    arch = arch + ".txt"
    done = s.create(arch)
    if done:
        print("Creacion exitosa")
    else:
        print("ERROR")


def READandWRITE():
    while True:
        print("Nombre del Archivo: ")
        arch = input()
        arch = arch + ".txt"
        try:
            content = s.leer(arch)
            print(content)
            print("\n1. Escribir")
            print("\n2. Salir")
            opc = input()
            if opc == "1":
                print("Texto: ")
                text = input()
                done = s.escribir(arch, text)
                if done:
                    print("Escritura exitosa")
                else:
                    print("ERROR")
            break;
        except:
            print("\nArchivo no encontrado")
            print("1. Reingresar nombre")
            print("2. Salir")
            opc = input()
            if opc != "1":
                break;


def RENAME():
    while True:
        print("\nNombre del Archivo: ")
        arch = input()
        arch = arch + ".txt"
        print("Nuevo nombre: ")
        newArch = input()
        newArch = newArch + ".txt"
        try:
            done = s.rename(arch, newArch)
            if done:
                print("Se renombro exitosamente")
            else:
                print("ERROR")
            break;
        except:
            print("\nArchivo no encontrado")
            print("1. Reingresar nombre")
            print("2. Salir")
            opc = input()
            if opc != "1":
                break;


def REMOVE():
    while True:
        print("\nNombre del Archivo: ")
        arch = input()
        arch = arch + ".txt"
        try:
            done = s.remove(arch)
            if done:
                print("Se elimino exitosamente")
            else:
                print("ERROR")
            break;
        except:
            print("\nArchivo no encontrado")
            print("1. Reingresar nombre")
            print("2. Salir")
            opc = input()
            if opc != "1":
                break;


def MKDIR():
    print("Nombre de la carpeta a crear: ")
    dir = input()
    done = s.mkdir(dir)
    if done:
        print("Creacion exitosa")
    else:
        print("ERROR")


def RMDIR():
    while True:
        print("\nNombre de la carpeta: ")
        dir = input()
        try:
            done = s.rmdir(dir)
            if done:
                print("Se elimino exitosamente")
            else:
                print("ERROR")
            break;
        except:
            print("\nCarpeta no encontrada")
            print("1. Reingresar nombre")
            print("2. Salir")
            opc = input()
            if opc != "1":
                break;


def READDIR():
    print("Directorios:\n")
    lista = s.readdir()
    for t in lista:
        print("-", t)


def Menu():
    while True:
        print("\n******MENU*******")
        print("\n1. CREATE: Crear un archivo nuevo")
        print("2. READ AND WRITE: Leer y escribir sobre archivo")
        print("3. RENAME: renombrar archivo")
        print("4. REMOVE: Eliminar archivo")
        print("5. MKDIR: Crear subdirectorios")
        print("6. RMDIR: Eliminar subdirectorios")
        print("7. READDIR: Leer lista de directorios")
        print("8. SALIR")
        opc = raw_input('')

        if "0" < opc < "9":
            if opc == "1":
                CREATE()
            if opc == "2":
                READandWRITE()
            if opc == "3":
                RENAME()
            if opc == "4":
                REMOVE()
            if opc == "5":
                MKDIR()
            if opc == "6":
                RMDIR()
            if opc == "7":
                READDIR()
            if opc == "8":
                exit()
        else:
            print("Ingrese una opcion disponible")

Menu()
