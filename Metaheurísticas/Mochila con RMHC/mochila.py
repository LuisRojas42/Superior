import objeto

class mochila:
    lista_objetos = []
    capacidad = 0

    def __init__(self, lista_objetos, capacidad):
        self.lista_objetos = lista_objetos
        self.capacidad = capacidad

    def agregar_elemento(self, peso, beneficio):
        objeto_nuevo = objeto.objeto(peso,beneficio)
        self.lista_objetos.append(objeto_nuevo)

    def obtener_beneficio(self):
        beneficio=0
        for i in self.lista_objetos:
            if i.seleccionado:
                beneficio += i.beneficio
        return beneficio

    def obtener_peso(self):
        peso = 0
        for i in self.lista_objetos:
            if i.seleccionado:
                peso += i.peso
        return peso

    def obtener_lista_objetos(self):
        lista = ""
        num = 1
        for i in self.lista_objetos:
            lista += "Objeto " + str(num) + ", " + i.detalles() + "\n"
            num+=1
        return lista

    def obtener_objetos_seleccionados(self):
        objetos = ""
        num = 1
        for i in self.lista_objetos:
            if i.seleccionado:
                objetos += "Objeto "+ str(num) + ": "+i.detalles()+"\n"
                num+=1
        return objetos
