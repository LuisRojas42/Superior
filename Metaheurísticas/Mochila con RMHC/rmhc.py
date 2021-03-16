import mochila
import evolucion

class rmhc:
    mochila = mochila.mochila([],0)
    lim_iteraciones = 0
    evolucion = evolucion.evolucion

    def __init__(self,capacidad,lim_iteraciones):
        self.mochila = mochila.mochila([],capacidad)
        self.lim_iteraciones = lim_iteraciones

    def agregar_objeto(self,peso,beneficio):
        self.mochila.agregar_elemento(peso, beneficio)

    def rmhc(self):
        self.nueva_solucion = mochila.mochila(self.mochila.lista_objetos,self.mochila.capacidad)
        self.mejor_solucion = 0
        i = 0
        self.mejor_iteracion = [-1]

        while True:
            self.mejor_solucion = self.evolucion.cadena_random(self.mochila.lista_objetos)
            cadena = self.evolucion.recorrer(self.mejor_solucion)

            cont = 1
            for i in cadena:
                if i==1:
                    self.nueva_solucion.lista_objetos[cont].seleccionado = True
                    cont+=1

            if self.nueva_solucion.obtener_peso()<=self.nueva_solucion.capacidad \
                    and self.nueva_solucion.obtener_peso()>0:
                break
            else:
                for i in self.nueva_solucion.lista_objetos:
                    i.seleccionado = False

        f_best=self.nueva_solucion.obtener_beneficio()
        str = "Solución inicial: "+ self.nueva_solucion.obtener_objetos_seleccionados()+"\n"\
              +"Peso total: "+self.nueva_solucion.obtener_peso()+"\n"\
              +"Beneficio total: "+self.nueva_solucion.obtener_beneficio()+"\n"

        while i<self.lim_iteraciones:
            locus = self.evolucion.obtner_b(self.mejor_solucion)
            nuevo_mejor = int(self.evolucion(locus, self.mejor_solucion))

            for j in nuevo_mejor:
                self.nueva_solucion.lista_objetos[j].seleccionado = not self.nueva_solucion.lista_objetos[j].seleccionado

            f_new = self.nueva_solucion.obtener_beneficio()
            peso_new = self.nueva_solucion.obtener_peso()
            if f_new >= f_best and peso_new<=self.nueva_solucion.capacidad:
                self.mejor_iteracion.append(i)
                if f_new==f_best:
                    self.mejor_iteracion.pop()
                self.mejor_solucion=nuevo_mejor
                f_best=f_new
            else:
                for j in nuevo_mejor:
                    self.nueva_solucion.lista_objetos[j].seleccionado = not self.nueva_solucion.lista_objetos[j].seleccionado
            i+=1
        str +=  "\n\nSolucion encontrada\n"+self.nueva_solucion\
                +"\nPeso total: "+self.nueva_solucion.obtener_peso()\
                +"\nBeneficio: "+self.nueva_solucion.obtener_beneficio()

        return str