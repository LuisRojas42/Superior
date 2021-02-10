#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h>
#include <sys/shm.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/sem.h>
#include "cabeceras.h"

key_t genClave(){
	key_t Clave;
	Clave = ftok ("/bin/ls", 24);
	if (Clave == -1)
	{
		printf("No consigo clave para memoria compartida\n");
		exit(0);
	}
	return Clave;
}

int genIdMemoria(key_t Clave){
	int Id_Memoria;
	Id_Memoria = shmget (Clave, sizeof(char)*5, 0777 | IPC_CREAT);
	if (Id_Memoria == -1)
	{
		printf("No consigo Id para memoria compartida\n");
		exit (0);
	}
	return Id_Memoria;
}

int* getDireccion(int Id_Memoria){
	int *Memoria = NULL;
	Memoria = (int *)shmat (Id_Memoria, (char *)0, 0);
	if (Memoria == NULL)
	{
		printf("No consigo memoria compartida\n");
		exit (0);
	}
	return Memoria;
}

void liberaMemoria(int* Memoria, int Id_Memoria){
	shmdt ((char *)Memoria);
	shmctl (Id_Memoria, IPC_RMID, (struct shmid_ds *)NULL);
}

void desasociaMemoria(int* Memoria, int Id_Memoria){
	if (Id_Memoria != -1)
	{
		shmdt ((char *)Memoria);
	}
}

int arraySemaforos(int Clave){
    int id = semget(Clave, 10, 0666 | IPC_CREAT);
    if(id < 0)
    {
        perror("semget"); exit(11);
    }
    return id;
}

//Semaforo 1
struct sembuf semUno_r = { 0, -1, SEM_UNDO}; //semaforo uno en rojo
struct sembuf semUno_v = { 0, +1, SEM_UNDO}; //semaforo uno en verde
//Semaforo 2
struct sembuf semDos_r = { 1, -1, SEM_UNDO}; 
struct sembuf semDos_v = { 1, +1, SEM_UNDO}; 
//Semaforo 3
struct sembuf semTres_r = { 2, -1, SEM_UNDO}; 
struct sembuf semTres_v = { 2, +1, SEM_UNDO}; 
//Semaforo 4
struct sembuf semCuatro_r = { 3, -1, SEM_UNDO};
struct sembuf semCuatro_v = { 3, +1, SEM_UNDO};
//Semaforo 5
struct sembuf semCinco_r = { 4, -1, SEM_UNDO};
struct sembuf semCinco_v = { 4, +1, SEM_UNDO};
//Semaforo 6
struct sembuf semSeis_r = { 5, -1, SEM_UNDO}; 
struct sembuf semSeis_v = { 5, +1, SEM_UNDO}; 
//Semaforo 7
struct sembuf semSiete_r = { 6, -1, SEM_UNDO};
struct sembuf semSiete_v = { 6, +1, SEM_UNDO};
//Semaforo 8
struct sembuf semOcho_r = { 7, -1, SEM_UNDO}; 
struct sembuf semOcho_v = { 7, +1, SEM_UNDO}; 
//Semaforo 9
struct sembuf semNueve_r = { 8, -1, SEM_UNDO};
struct sembuf semNueve_v = { 8, +1, SEM_UNDO};
//Semaforo 10
struct sembuf semDiez_r = { 9, -1, SEM_UNDO}; 
struct sembuf semDiez_v = { 9, +1, SEM_UNDO}; 

void iniciaSemaforos(int id){
    union semun u;
    u.val = 1;
    if(semctl(id, 0, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 1, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 2, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 3, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 4, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 5, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 6, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 7, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 8, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
    if(semctl(id, 9, SETVAL, u) < 0)
    {
        perror("semctl"); exit(12);
    }
}

void setSemUno_r(int id){
    if(semop(id, &semUno_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemUno_v(int id){
    if(semop(id, &semUno_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemDos_r(int id){
    if(semop(id, &semDos_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemDos_v(int id){
    if(semop(id, &semDos_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemTres_r(int id){
    if(semop(id, &semTres_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemTres_v(int id){
    if(semop(id, &semTres_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemCuatro_r(int id){
    if(semop(id, &semCuatro_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemCuatro_v(int id){
    if(semop(id, &semCuatro_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemCinco_r(int id){
    if(semop(id, &semCinco_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemCinco_v(int id){
    if(semop(id, &semCinco_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemSeis_r(int id){
    if(semop(id, &semSeis_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemSeis_v(int id){
    if(semop(id, &semSeis_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemSiete_r(int id){
    if(semop(id, &semSiete_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemSiete_v(int id){
    if(semop(id, &semSiete_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemOcho_r(int id){
    if(semop(id, &semOcho_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemOcho_v(int id){
    if(semop(id, &semOcho_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemNueve_r(int id){
    if(semop(id, &semNueve_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemNueve_v(int id){
    if(semop(id, &semNueve_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}

void setSemDiez_r(int id){
    if(semop(id, &semDiez_r, 1) < 0){
        perror("semop p"); exit(13);
    }
}

void setSemDiez_v(int id){
    if(semop(id, &semDiez_v, 1) < 0){
        perror("semop p"); exit(14);
    }   
}
