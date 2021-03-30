import random

class punto:

    def __init__(self, dimencion):
        self.dimencion = dimencion
        self.lista_xi = [None]*dimencion

    def asigna_todo(self):
        for i in range(0,self.dimencion,1):
            self.lista_xi[i] = (random.randint(-10, 10))
        
    def asigna_index(self, index):
        self.lista_xi[index] = random.randint(-10, 10)

    def evaluar(self):
        func = 0
        for i in range(0, len(self.lista_xi)):
            func += pow(self.lista_xi[i],2)
        return func
