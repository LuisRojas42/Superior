#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import math
import cmath
from FFT import *


def formato(secuencia):
    if secuencia.find("j") == -1:
        secuencia = list(map(int, secuencia.split(',')))
    else:
        secuencia = secuencia.split(',')
        cont = 0
        for i in secuencia:
            if i.find("j") != -1:
                i = i.replace(" ", "")  # will do nothing if unneeded
                secuencia[cont] = complex(i)
            else:
                secuencia[cont] = int(i)
            cont += 1

    return secuencia


class Menu():

    def __init__(self):
        self.raiz = Tk()

        self.x = StringVar(value='0')
        self.xp = BooleanVar()
        self.hp = BooleanVar()

        self.raiz.title("Convolucion discreta")
        self.raiz.resizable(0, 0)
        self.raiz.geometry("400x300")

        self.back = ttk.Frame()

        self.back.config(width="400", height="300")
        miImagen = PhotoImage(file='back2.png')
        Label(self.back, image=miImagen, bg="white", font=(18)).place(x=0, y=0)

        self.g_x = ttk.Entry(self.back, textvariable=self.x)
        self.g_x.place(x=95, y=130)
        self.g_xp = Checkbutton(self.back, variable=self.xp, onvalue=True, offvalue=False, bg="white")
        self.g_xp.place(x=95, y=160)
        self.g_hp = Checkbutton(self.back, variable=self.hp, onvalue=True, offvalue=False, bg="white")
        self.g_hp.place(x=185, y=160)

        self.graf = ttk.Button(self.back, text="Resultado", command=self.recolectar)
        self.graf.place(x=135, y=190)

        self.back.pack()

        self.raiz.mainloop()

    def recolectar(self, *args):
        xp = self.xp.get()
        hp = self.hp.get()
        if (xp & hp):
            messagebox.showinfo(message="Solo debe marcar una opción", title="Resultado")
            return;
        if ((not xp) & (not hp)):
            messagebox.showinfo(message="Debe marcar una opción", title="Resultado")
            return;
        if (xp & (not hp)):
            x = self.x.get()
            messagebox.showinfo(message=FFT(formato(x)), title="Resultado")
        if ((not xp) & hp):
            x = self.x.get()
            messagebox.showinfo(message=IFFT(formato(x)), title="Resultado")


def main():
    men = Menu()
    return 0


if __name__ == '__main__':
    main()