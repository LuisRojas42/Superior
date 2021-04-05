
import time
import socket
import sys
import threading

# Indica si ha terminado el hilo
hilo_terminado = False

def lector(blockLector, blockEscritor, num):
    while True:
        ban = blockEscritor.acquire(0)
        if not ban:
            ban2 = blockLector.acquire(0)
            if ban2:
                blockLector.release()
                ban = True
        if ban:
            print("lector " + num + " accedio a la BD \n")
            time.sleep(.01)
            try:
                blockEscritor.release()
            except:
                print ("0")
            break
        else:

            print("lector " + num + " intento acceder \n")


def Escritor(blockLector, blockEscritor, num):
    worker_id = barrier.wait()
    while True:
        ban = blockEscritor.acquire(0)
        ban2 = blockLector.acquire(0)
        if ban:
            print ("escritor " + num + " accedio a la BD \n")
            time.sleep(.01)
            blockEscritor.release()
            blockLector.release()
            print("liberado\n")
            break
        else:
            print ("escritor " + num + " intento acceder \n")



if __name__ == '__main__':

    blockLector = threading.Lock()
    blockEscritor = threading.Lock()

    threads = []  # Arreglo hilos
    NUM_THREADS = 2
    barrier = threading.Barrier(NUM_THREADS)

    threads.append(threading.Thread(target = Escritor, args=(blockLector, blockEscritor, "1"))) # Lanzamos un hilo
    threads.append(threading.Thread(target = Escritor, args=(blockLector, blockEscritor, "2")))  # Lanzamos un hilo
    threads.append(threading.Thread(target =  lector, args=(blockLector, blockEscritor, "1")))  # Lanzamos un hilo
    threads.append(threading.Thread(target = lector, args=(blockLector, blockEscritor, "2")))  # Lanzamos un hilo

    for t in threads:
        t.start()

    for t in threads:  # espera que todos esten listos
        t.join()

    while (not hilo_terminado):  # Espera a que termine el hilo
        pass
