#!/usr/bin/env python
import math
import cmath

__author__ = "Isaac Martínez, Luis Rojas y Rafael Barajas"


# Para definir el número deseado de decimales en el flotante
def truncar(numero, digitos) -> float:
    aux = 10.0 ** digitos
    return math.trunc(aux * numero) / aux


def obtener_wn(tam_secuencia):
    j_cmplx = complex(0, 1)  # Constante j
    w_n = cmath.exp((((-1) * j_cmplx) * (2 * math.pi)) / tam_secuencia)
    # Truncamos el valor solo a 4 digitos para su manejo futuro.
    wn_real = truncar(w_n.real, 4)
    wn_imag = truncar(w_n.imag, 4)
    return complex(wn_real, wn_imag)


def fft(secuencia):
    cont_aux_u = 0  # Contador para los pares dentro de cada mariposa
    cont_aux_d = 0  # Contador para los impares dentro de cada mariposa
    no_mariposas = 0  # Número total de mariposas por etapa --> N/2^n donde n = etapa

    division_par_impar = 0
    secuencia_auxiliar = []
    tam_secuencia = int(len(secuencia))  # Obtenemos el tamaño de la secuencia

    for value in secuencia:
        secuencia_auxiliar.append(value[
                                      0])  # Los valores de la secuencia estan guardados como [value], por eso hay que obtenerlos individualmente

    etapas = int(math.log(tam_secuencia, 2))  # Calculamos el número de etapas con el log2(N)
    w_n = obtener_wn(tam_secuencia)

    i = 1  # Para etapas
    j = 0  # Para mariposas
    k = 0  # Para sumatoria dentro de las mariposas
    exp_wn = 0

    for i in range(1, etapas + 1):
        no_mariposas = int(tam_secuencia / (math.pow(2, i)))
        division_par_impar = int((math.pow(2, i)) / 2)
        cont_aux = 0
        cont_aux_u = 0
        cont_aux_d = division_par_impar
        exp_wn = 0
        for j in range(0, no_mariposas):
            cont_aux_x = cont_aux
            for k in range(0, pow(2, (i - 1))):
                if division_par_impar == 1:
                    secuencia[cont_aux] = secuencia_auxiliar[cont_aux_u] + (pow(w_n, exp_wn)) * (
                    secuencia_auxiliar[cont_aux_d])
                    secuencia[cont_aux + division_par_impar] = (secuencia_auxiliar[cont_aux_u]) + (
                                (-1) * (pow(w_n, exp_wn))) * (secuencia_auxiliar[cont_aux_d])
                else:
                    secuencia[cont_aux_x] = secuencia_auxiliar[cont_aux_u] + (pow(w_n, exp_wn)) * (
                    secuencia_auxiliar[cont_aux_d])
                    secuencia[cont_aux_x + division_par_impar] = secuencia_auxiliar[cont_aux_u] + (
                                (-1) * (pow(w_n, exp_wn))) * (secuencia_auxiliar[cont_aux_d])
                    if ((exp_wn + no_mariposas) < (tam_secuencia / 2)):
                        exp_wn = exp_wn + no_mariposas
                    cont_aux_x = cont_aux_x + 1
                    cont_aux_u = cont_aux_u + 1
                    cont_aux_d = cont_aux_d + 1

                k = k + 1

            cont_aux = cont_aux + division_par_impar * 2
            cont_aux_u = cont_aux
            cont_aux_d = cont_aux_u + division_par_impar
            exp_wn = 0
            j = j + 1

        i = i + 1
        secuencia_auxiliar = secuencia.copy()

    ii = 0
    for ii in range(0, len(secuencia_auxiliar)):
        real = truncar(secuencia_auxiliar[ii].real, 4)
        imag = truncar(secuencia_auxiliar[ii].imag, 4)
        new_cmplx = complex(real, imag)
        secuencia_auxiliar[ii] = new_cmplx
    return secuencia_auxiliar


def ifft(secuencia):
    cont_aux_u = 0  # Contador para los pares dentro de cada mariposa
    cont_aux_d = 0  # Contador para los impares dentro de cada mariposa
    no_mariposas = 0  # Número total de mariposas por etapa --> N/2^n donde n = etapa

    division_par_impar = 0
    secuencia_auxiliar = []
    tam_secuencia = int(len(secuencia))  # Obtenemos el tamaño de la secuencia

    for value in secuencia:
        secuencia_auxiliar.append(value[
                                      0])  # Los valores de la secuencia estan guardados como [value], por eso hay que obtenerlos individualmente

    etapas = int(math.log(tam_secuencia, 2))  # Calculamos el número de etapas con el log2(N)
    w_n = obtener_wn(tam_secuencia)

    i = 1  # Para etapas
    j = 0  # Para mariposas
    k = 0  # Para sumatoria dentro de las mariposas
    exp_wn = 0

    for i in range(1, etapas + 1):
        no_mariposas = int(tam_secuencia / (math.pow(2, i)))
        division_par_impar = int((math.pow(2, i)) / 2)
        cont_aux = 0
        cont_aux_u = 0
        cont_aux_d = division_par_impar
        exp_wn = 0
        for j in range(0, no_mariposas):
            cont_aux_x = cont_aux
            for k in range(0, pow(2, (i - 1))):
                if division_par_impar == 1:
                    secuencia[cont_aux] = secuencia_auxiliar[cont_aux_u] + ((pow(w_n, exp_wn)).conjugate()) * (
                    secuencia_auxiliar[cont_aux_d])
                    secuencia[cont_aux + division_par_impar] = (secuencia_auxiliar[cont_aux_u]) + (
                        ((-1) * (pow(w_n, exp_wn))).conjugate()) * (secuencia_auxiliar[cont_aux_d])
                else:
                    secuencia[cont_aux_x] = secuencia_auxiliar[cont_aux_u] + ((pow(w_n, exp_wn)).conjugate()) * (
                    secuencia_auxiliar[cont_aux_d])
                    secuencia[cont_aux_x + division_par_impar] = secuencia_auxiliar[cont_aux_u] + (
                        ((-1) * (pow(w_n, exp_wn))).conjugate()) * (secuencia_auxiliar[cont_aux_d])
                    if ((exp_wn + no_mariposas) < (tam_secuencia / 2)):
                        exp_wn = exp_wn + no_mariposas
                    cont_aux_x = cont_aux_x + 1
                    cont_aux_u = cont_aux_u + 1
                    cont_aux_d = cont_aux_d + 1

                k = k + 1

            cont_aux = cont_aux + division_par_impar * 2
            cont_aux_u = cont_aux
            cont_aux_d = cont_aux_u + division_par_impar
            exp_wn = 0
            j = j + 1

        i = i + 1
        secuencia_auxiliar = secuencia.copy()

    # Los valores obtenidos pueden contener muchos digitos después del punto por ello truncamos cada valor a 4 decimales.
    ii = 0
    for ii in range(0, len(secuencia_auxiliar)):
        secuencia_auxiliar[ii] = secuencia_auxiliar[ii] * (1 / tam_secuencia)
        real = truncar(secuencia_auxiliar[ii].real, 4)
        imag = truncar(secuencia_auxiliar[ii].imag, 4)
        new_cmplx = complex(real, imag)
        secuencia_auxiliar[ii] = new_cmplx

    return secuencia_auxiliar


# Partimos nuestra secuencia en un dos arreglos (Derecha/Izquiera) || (Pares/Impares)
def particion(secuencia):
    i = 0
    par = []
    impar = []
    cont_par = 0
    cont_impar = 1

    tam = len(secuencia)

    while (i < tam) and (cont_par < tam) and (cont_impar < tam):
        par.append(secuencia[cont_par])
        impar.append(secuencia[cont_impar])
        cont_par = cont_par + 2
        cont_impar = cont_impar + 2
        i = i + 1

    return par, impar


def desagrupar(
        secuencia_ordenada):  # Anteriormente se añadieron arreglos de dos elementos; hay que fragmentar cada pedazo
    auxiliar = []
    for elm in secuencia_ordenada:
        auxiliar.append(elm[0])
        auxiliar.append(elm[1])
    return auxiliar


def bit_inverso(secuencia, aux):
    resultado = particion(secuencia)

    if (len(resultado[0]) == 1 and len(resultado[1]) == 1):
        return resultado
    else:
        res = bit_inverso(resultado[0], aux)
        if not res is None:
            aux.append(res)
        res2 = bit_inverso(resultado[1], aux)
        if not res2 is None:
            aux.append(res2)


def FFT(secuencia):
    secuencia_ordenada = []  # fila 1 pares, fila 2 impares
    secuencia_ordenada_a = bit_inverso(secuencia, secuencia_ordenada)

    if (secuencia_ordenada_a is None):  # 4 o más terminos en la secuencia x(n)
        secuencia_ordenada = desagrupar(secuencia_ordenada)  # Recuperamos la forma original de secuencia
        fft_res = fft(secuencia_ordenada)
        print(fft_res)
        return fft_res
        # ifft_res = ifft(secuencia_ordenada)
        # print(ifft_res)
    else:  # Solo dos terminos en la secuencia x(n)
        fft_res = fft(secuencia_ordenada_a)
        print(fft_res)
        return fft_res

def IFFT(secuencia):
    secuencia_ordenada = []  # fila 1 pares, fila 2 impares
    secuencia_ordenada_a = bit_inverso(secuencia, secuencia_ordenada)

    if (secuencia_ordenada_a is None):  # 4 o más terminos en la secuencia x(n)
        secuencia_ordenada = desagrupar(secuencia_ordenada)  # Recuperamos la forma original de secuencia
        #fft_res = fft(secuencia_ordenada)
        #print(ifft_res)
        #return fft_res
        ifft_res = ifft(secuencia_ordenada)
        print(ifft_res)
        return ifft_res
    else:  # Solo dos terminos en la secuencia x(n)
        fft_res = fft(secuencia_ordenada_a)
        print(fft_res)
        return fft_res


def main():
    # --SECUENCIAS EMPLEADAS PARA PRUEBAS DEL ALGORITMO FFT
    # secuencia = [1,2,0,-1]
    # secuencia = [0,1,2,3]
    # secuencia = [-4,-4,-12,-16]
    # secuencia = [-1,2,0,0,4,0,-3,-1]
    # secuencia = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    # --SECUENCIAS EMPLEADAS PARA PRUEBAS DEL ALGORITMO IFFT
    secuencia = [-36, (8 - 12j), 4, (8 + 12j)]
    # secuencia = [-36,(8-12j),4,(8+12j)]
    # secuencia = [(1+0j), (-4.292886437822-5.121228897821999j), (6-2.9999424599999998j), (-5.707099999739877+0.8786967084518778j), (-1+0j), (-5.707113562178-0.8786560221780002j), (6+2.9999424599999998j), (-4.292900000260123+5.121188211548121j)]
    FFT(secuencia)


if __name__ == "__main__":
    main()
