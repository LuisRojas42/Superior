import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def grafica(x, xn0, h, hn0, y, yn0):
    gs = gridspec.GridSpec(2,2)
    

    aux = 0
    xy = []
    for i in x:
        xy.append(aux - xn0)
        aux += 1
    plt.subplot(gs[0,0])
    plt.bar(xy, x, width=0.05)
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.grid()
    plt.xticks(np.arange(min(xy), max(xy)+1, step=1))
    plt.yticks(np.arange(min(x), max(x)+1, step=1))

    aux = 0
    hy = []
    for i in h:
        hy.append(aux - hn0)
        aux += 1
    plt.subplot(gs[0,1])
    plt.bar(hy, h, width=0.05)
    plt.xlabel('n')
    plt.ylabel('h(n)')
    plt.grid()
    plt.xticks(np.arange(min(hy), max(hy)+1, step=1))
    plt.yticks(np.arange(min(h), max(h)+1, step=1))

    aux = 0
    yy = []
    for i in y:
        yy.append(aux - yn0)
        aux += 1
    plt.subplot(gs[1, :])
    plt.bar(yy, y, width=0.05)
    plt.xlabel('n')
    plt.ylabel('y(n)')
    plt.grid()
    plt.xticks(np.arange(min(yy), max(yy)+1, step=1))
    plt.yticks(np.arange(min(y), max(y)+1, step=1))

    # MOSTRAR LEYENDA, CUADRICULA Y FIGURA
    plt.legend()
    plt.show()

