class objeto:
    peso = 0
    beneficio = 0
    seleccionado = False

    def __init__(self, peso, beneficio):
        self.peso = peso
        self.beneficio = beneficio

    def detalles(self):
        if self.seleccionado:
            return "Sel: True pe: "+self.peso+" ben: "+self.beneficio
        else:
            return "Sel: False, pe: " + str(self.peso) + ", ben: " + str(self.beneficio)
