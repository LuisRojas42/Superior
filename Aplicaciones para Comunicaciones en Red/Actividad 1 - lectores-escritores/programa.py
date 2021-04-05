import thread
import time

# Indica si ha terminado el hilo
hilo_terminado = False
ban = True

def lector(ban, bloqueo, num):
    while True:
        ban = bloqueo.acquire()
        if ban:
            print "lector " + num + " accedio a la BD \n"
            time.sleep(2)
            bloqueo.release()
            break
        else:
            print "lector " + num + " intento acceder \n"


def Escritor(ban, bloqueo, num):
    while True:
        ban = bloqueo.acquire()
        if ban:
            print "escritor " + num + " accedio a la BD \n"
            time.sleep(2)
            bloqueo.release()
            break
        else:
            print "escritor " + num + " intento acceder \n"



if __name__ == '__main__':

    bloqueo = thread.allocate_lock()

    thread.start_new_thread(Escritor, (ban, bloqueo, "1"))  # Lanzamos un hilo
    thread.start_new_thread(Escritor, (ban, bloqueo, "2"))  # Lanzamos un hilo
    thread.start_new_thread(lector, (ban, bloqueo, "1"))  # Lanzamos un hilo
    thread.start_new_thread(lector, (ban, bloqueo, "2"))  # Lanzamos un hilo

    while (not hilo_terminado):  # Espera a que termine el hilo
        pass
