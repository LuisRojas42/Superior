#! /usr/bin/env python
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from AlgoritmosConvolucion import *
from grafica import *
from PyQt5 import uic, QtWidgets

class Menu():
    global Co 
    global Or 

    def __init__(self):  	
    	self.raiz=Tk()

    	self.x= StringVar(value='0')
    	self.h= StringVar(value='0')
    	self.xo=IntVar(value=1)   
    	self.ho=IntVar(value=1)
    	self.xp = BooleanVar()  
    	self.hp = BooleanVar()  

    	self.raiz.title("Convolución discreta")
    	self.raiz.resizable(0,0)
    	self.raiz.geometry("800x500")

    	self.back = ttk.Frame()

    	self.back.config(width="800", height="500") 
    	miImagen=PhotoImage(file='back.png')
    	Label(self.back, image=miImagen, bg="white",font=(18)).place(x=0, y=0)

    	self.g_x = ttk.Entry(self.back,textvariable=self.x)
    	self.g_x.place(x = 180, y=230)
    	self.g_xo = ttk.Entry(self.back,textvariable=self.xo)
    	self.g_xo.place(x = 330, y=270)
    	self.g_xp = Checkbutton(self.back, variable=self.xp, onvalue=True, offvalue=False, bg="white")
    	self.g_xp.place(x = 620, y=270)

    	self.g_h = ttk.Entry(self.back,textvariable=self.h)
    	self.g_h.place(x = 180, y=320)
    	self.g_hp = ttk.Entry(self.back,textvariable=self.ho)
    	self.g_hp.place(x = 330, y=360)
    	self.g_hp = Checkbutton(self.back, variable=self.hp, onvalue=True, offvalue=False, bg = "white")
    	self.g_hp.place(x = 620, y=360)

    	self.conv = ttk.Button(self.back, text="Convolución",command=self.convolucion)
    	self.conv.place(x=500, y= 410)
    	self.graf= ttk.Button(self.back, text="Graficar", command=self.graficar, state=DISABLED)  
    	self.graf.place(x=630, y= 410)

    	self.back.pack()  

    	self.raiz.mainloop() 

    def recolectar(self, *args):    
        error_dato = False
        try:
            xo = int(self.xo.get())
            ho = int(self.ho.get())
        except:
            error_dato = True 
            messagebox.showinfo(message="Error en el punto origen", title="¡Error!")
        x = self.x.get()
        h = self.h.get()   
        if not error_dato:
            if(xo > len(x) or xo == 0):
                messagebox.showinfo(message="El origen de x(n) esta fuera del rango de la secuencia", title="¡Error!")
                error_dato = True
                return error_dato, x, h 
            elif(ho > len(h) or ho == 0):
                messagebox.showinfo(message="El origen de h(n) esta fuera del rango de la secuencia", title="¡Error!")
                error_dato = True
                return error_dato, x, h 
            x = x.split(',')  
            h = h.split(',') 
            for i in range(0,len(x)):
                try:
                    x[i] = float(x[i])
                except:
                    f = x[i].split('/')
                    if(len(f) == 2):
                        try:
                            x[i]=int(f[0])/int(f[1])
                        except:
                            error_dato = True
                            messagebox.showinfo(message="Error en x(n)", title="¡Error!")
                            return error_dato, x, h 
                    else:
                        error_dato = True
                        messagebox.showinfo(message="Error en x(n)", title="¡Error!")
                        return error_dato, x, h 

            for i in range(0,len(h)):
                try:
                    h[i] = float(h[i])
                except:
                    f = h[i].split('/')
                    if(len(f) == 2):
                        try:
                            h[i]=int(f[0])/int(f[1])
                        except:
                            error_dato = True
                            messagebox.showinfo(message="Error en h(n)", title="¡Error!")
                            return error_dato, x, h
                    else:
                        error_dato = True
                        messagebox.showinfo(message="Error en h(n)", title="¡Error!")
                        return error_dato, x, h
            return error_dato, x, h
        return error_dato, x, h   

    def convolucion(self, *args):
        error,x,h = self.recolectar(self, *args)
        if not error:
            xp = self.xp.get()
            hp = self.hp.get()
            if(xp & hp):
                Conv, origen = convolucionCircular(x, self.xo.get()-1, h, self.ho.get()-1)

                print("CONVOLUCIÓN CIRCULAR")
                print("Vector Resultado:", end=' ')
                for x in Conv:
                    print(x, end=' ')
                print("")
                print("Origen: {}, valor -> {}".format(origen+1, Conv[origen]))
                print("")
                Conv = Conv + Conv
            elif(xp & (not hp)):
                Conv, origen = convolucionPeriodica(x, self.xo.get()-1, h, self.ho.get()-1)

                print("CONVOLUCIÓN PERIÓDICA")
                print("Vector Resultado:", end=' ')
                for x in Conv:
                    print(x, end=' ')
                print("")
                print("Origen: {}, valor -> {}".format(origen+1, Conv[origen]))
                print("")

            elif((not xp) & hp):
                Conv, origen = convolucionPeriodica(h, self.ho.get()-1, x, self.xo.get()-1)

                print("CONVOLUCIÓN PERIÓDICA")
                print("Vector Resultado:", end=' ')
                for x in Conv:
                    print(x, end=' ')
                print("")
                print("Origen: {}, valor -> {}".format(origen+1, Conv[origen]))
                print("")
            elif((not xp) & (not hp)): 
                Conv, origen = convolucionFinita(x, self.xo.get()-1, h, self.ho.get()-1)

                print("CONVOLUCIÓN FINITA")
                print("Vector Resultado:", end=' ')
                for x in Conv:
                    print(x, end=' ')
                print("")
                print("Origen: {}, valor -> {}".format(origen+1, Conv[origen]))
                print("")
            for x in Conv:
                    x+=x
            messagebox.showinfo(message=str(Conv), title="Resultado")
            messagebox.showinfo(message="Origen: {}, valor -> {}".format(origen+1, Conv[origen]), title="Resultado")
            self.graf['state'] = 'normal'
            self.Co = Conv
            self.Or = origen
            

    def graficar(self, *args):
        error,x,h = self.recolectar(self, *args)
        grafica(x, self.xo.get()-1, h, self.ho.get()-1, self.Co, self.Or)
        self.graf.config(state = DISABLED)
        
    

def main():
    men = Menu()
    return 0

if __name__ == '__main__':
    main()