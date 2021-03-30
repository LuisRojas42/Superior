import heuristicas
import punto

class Main:

    def __init__(self, dimencion=1, iterciones=100):
        self.dimencion = dimencion
        self.iterciones = iterciones
        self.lista_xi = punto.punto(self.dimencion)
        self.evolucion = heuristicas.heuristica()

    def rmhc(self):
        self.lista_xi.asigna_todo()
        print("incial: ",self.lista_xi.lista_xi)
        lista_puntos = [None]*self.dimencion
        best_solution = self.evolucion.random_string(self.lista_xi.lista_xi)
        cadena = self.evolucion.num_a_bin(best_solution)
        for i in range(len(cadena)):
            self.lista_xi.asigna_index(i)
        f_best = self.lista_xi.evaluar()
        k=0
        self.mejor_iteracion=[-1]

        print("best solution: ",best_solution, " cadena: ",cadena, " fbest: ",f_best)
        print(f"Primer solución minima: {self.lista_xi.lista_xi} con valor: {f_best}\n")
        print("Iteraciones: ",self.iterciones)

        while k < self.iterciones:
            locus = self.evolucion.get_locus(best_solution)
            new_best = int(self.evolucion.evolucion(locus, best_solution))
            cadena = self.evolucion.num_a_bin(new_best)
            
            print("locus: ",locus," new best: ",new_best," cadena: ",cadena)

            for i in range(len(cadena)):
                lista_puntos[i]=self.lista_xi.lista_xi[i]
                self.lista_xi.asigna_index(i)
            
            f_new = self.lista_xi.evaluar()
            
            print("fbest: ",f_best," fnew: ",f_new, " lista p: ",lista_puntos, " lista x: ",self.lista_xi.lista_xi)
            if f_new <= f_best:
                self.mejor_iteracion.append(i)
                if f_new == f_best:
                    self.mejor_iteracion.pop()
                best_solution = new_best
                f_best = f_new
            else:
                for i in range(len(cadena)):
                    self.lista_xi.lista_xi[i] = lista_puntos[i]
                    lista_puntos[i] = 0
            k+=1

        print(f"Mejor solución minima: {self.lista_xi.lista_xi} con valor: {f_best} en la iteracion {self.mejor_iteracion[-1]}")

main = Main(5, 5)
main.rmhc()