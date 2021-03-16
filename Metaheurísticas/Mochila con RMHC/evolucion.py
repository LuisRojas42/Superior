import random

class evolucion:
    cadena = ""

    def __init__(self):
        self.cadena = ""

    def recorrer(num):
        str = []
        if num == 0:
            return [0]
        while num > 0:
            if num%2 == 0:
               str.append(0)
            else:
                str.append(1)
            num/=2
        return str;

    def cadena_random(lista):
        return random.randint(0, len(lista))

    def obtner_b(cadena):
        return random.randint(0, cadena-1)

    def evolucion(b, cadena):
        return random.randint(b, cadena)
