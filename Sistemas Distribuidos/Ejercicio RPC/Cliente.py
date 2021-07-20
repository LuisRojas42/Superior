import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://192.168.100.188:8000')

def menu():
    while True:
        print("\n*** CALCULADORA ***\n")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. Divicion")
        print("5. Salir")
        resp = input()
        try:
            resp = int(resp)
            if 0 < resp < 6:
                operacion(resp, s)
            else:
                print("\nIngrese una opción válida\n")
        except ValueError:
            print("\nATENCIÓN: Debe ingresar un número entero.\n")


def parametros(par):
    while True:
        print(par + " valor: \n")
        valor = input()
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("\nATENCIÓN: Debe ingresar un número entero.\n")

def suma(s):
    num1 = parametros("primer")
    num2 = parametros("segundo")
    print(num1, "+", num2, ": ", s.add(num1,num2))


def resta(s):
    num1 = parametros("primer")
    num2 = parametros("segundo")
    print(num1, "-", num2, ": ", s.res(num1,num2))


def multiplicacion(s):
    num1 = parametros("primer")
    num2 = parametros("segundo")
    print(num1, "*", num2, ": ", s.mul(num1,num2))


def divicion(s):
    num1 = parametros("primer")
    num2 = parametros("segundo")
    print(num1, "÷", num2, ": ", s.div(num1, num2))


def operacion(resp, s):
    if resp == 1:
        suma(s)
    elif resp == 2:
        resta(s)
    elif resp == 3:
        multiplicacion(s)
    elif resp == 4:
        divicion(s)
    elif resp == 5:
        exit()
    else:
        print("Ocurrio un error")


menu()


