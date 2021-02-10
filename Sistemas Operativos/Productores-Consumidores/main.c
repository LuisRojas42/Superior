#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h>
#include <sys/shm.h>

//CABECERAS
key_t genClave();
int genIdMemoria(key_t);
int* getDireccion(int);
void liberaMemoria(int*, int);

int main(){

	//Iniciamos memoria
	key_t Clave = genClave();
	int Id_Memoria = genIdMemoria(Clave);
	int *Memoria = getDireccion(Id_Memoria);

	//Instrucciones
	Memoria[0] = 'a';
	printf("%c\n", Memoria[0]);

	//Liberamos la memoria
	liberaMemoria(Memoria, Id_Memoria);
	return 0;
}

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