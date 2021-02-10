// 
// Programa de prueba para la memoria compartida.
// Javier Abellán, 10 de Mayo de 2002
//
#include <sys/shm.h>
#include<stdio.h> 
#include<stdlib.h> 
#include <unistd.h>

void main()
{
	key_t Clave;
	int Id_Memoria;
	int *Memoria = NULL;
	int i,j;

	//
	//	Igual que en p1.cc, obtenemos una clave para la memoria compartida
	//
	Clave = ftok ("/bin/ls", 33);
	if (Clave == -1)
	{
		printf("No consigo clave para memoria compartida\n");
		exit(0);
	}

	//
	//	Igual que en p1.cc, obtenemos el id de la memoria. Al no poner
	//	el flag IPC_CREAT, estamos suponiendo que dicha memoria ya está
	//	creada.
	//
	Id_Memoria = shmget (Clave, sizeof(int)*100, 0777 );
	if (Id_Memoria == -1)
	{
		printf("No consigo Id para memoria compartida\n");
		exit (0);
	}

	//
	//	Igual que en p1.cc, obtenemos un puntero a la memoria compartida
	//
	Memoria = (int *)shmat (Id_Memoria, (char *)0, 0);
	if (Memoria == NULL)
	{
		printf("No consigo memoria compartida\n");
		exit (0);
	}

	//
	//	Vamos leyendo el valor de la memoria con esperas de un segundo
	//	y mostramos en pantalla dicho valor. Debería ir cambiando según
	//	p1 lo va modificando.
	//
	for (i=0; i<10; i++)
	{
		//cout << "Leido " << Memoria[0] << endl;
		printf("Leido %d\n", Memoria[i]);
		sleep (1);
	}


	//
	//	Desasociamos nuestro puntero de la memoria compartida. Suponemos
	//	que p1 (el proceso que la ha creado), la liberará.
	//
	if (Id_Memoria != -1)
	{
		shmdt ((char *)Memoria);
	}
}
