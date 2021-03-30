import random

class heuristica:
    def __init__(self):
        var=""

    @staticmethod
    def num_a_bin(num):
        binario = bin(num)
        binario = binario[2:len(binario)]
        return binario
    
    @staticmethod
    def random_string(lista):
        return random.randint(0, len(lista))
    
    @staticmethod
    def get_locus(cadena):
        return random.randint(0, cadena)

    @staticmethod
    def evolucion(locus, cadena):
        return random.randint(locus, cadena)