/*
	\mainpage
	\author: Rojas Zepeda Luis Eduardo
	\version 1.0
	\date March 31 2019

*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "../Include/Cola.h"
#include "../Include/Lista.h"

/**Cabecera funcion listaJobs*/
Lista listaJobs();
/**Cabecera funcion imprimeCola*/
void imprimeCola(Cola);

/**\brief Programa principal. */
int main(int argc, char *argv[]){
	
	/**

		\details
		Una vez que se obtienen la lista de procesos y la cola de preocesos, se simula el algoritmo de Round Robin
		mediante un ciclo while, un contador y el tiempo de ejecución.

	*/

	int chunk=0;
	int tiempo=0;
	int contador=0;
	Lista jobs = listaJobs();	
	Cola ready = nueva();
	//impLista(jobs);

	printf("Chunk: ");
	scanf("%d", &chunk);

	/** \details 
		Algoritmo de Round Robin
	*/
	while(!esVacia(jobs) || !esNueva(ready)){
		if(!esVacia(jobs))
			if(horaLlegada(jobs) == tiempo){
				ready = formar(ready, idProceso(jobs), horaLlegada(jobs), duracion(jobs));
				printf("\n%d Aqui estoy (se formo este preoceso)\n\n", idProceso(jobs));
				imprimeCola(ready);
				jobs = resto(jobs);
			}
		if(esNueva(ready))
			printf("No ha llegado ningun proceso\n");
		else{
			if(contador<chunk){
				if(duracionC(ready)!=0){
					printf("Soy el proceso %d\n", idProcesoC(ready));
					restaDuracion(ready);
					//printf("duracion: %d\n\n", duracionC(ready));
				}else{
					printf("\n");
					printf("%d Adios\n\n", idProcesoC(ready));
					if(!esNueva(ready))
						ready = desformar(ready);
				}
			}else{
				contador=-1;
				//printf("rota proceso\n");
				if(!esNueva(ready))
					ready = rotar(ready);
			}
		}
		contador++;
		tiempo++;

	}
	
	return 0;
}

/*	*\brief Imprime en formato de tabla la cola de procesos actual.
  	*\param ready Es una cola con los procesos listos para ejecutare esperando su turno.
*/
void imprimeCola(Cola ready){
	printf("IdProceso\tHoraLLegada\tDuracion\n");
	impCola(ready);
	printf("\n");
}

/*	*\brief Obtiene de un archivo de texto los procesos con sus respectivos valores y los enlista segun su tiempo de llegada
	*\return jobs Es una lista con todos los procesos y sus atributos ordenados segun su hora de llegada
*/
Lista listaJobs(){

	char pal[80], *w;
	char delim[] = ",";
	FILE *fp;        
	int idProceso = 0, horaLlegada = 0, duracion = 0;
	Lista jobs = vacia();
	int i;
	
	fp = fopen ( "procesos.txt", "r" );
	if (fp==NULL) {
		fputs ("File error", stderr); 
		exit (1);
	}
	
	while (fscanf(fp, "%s", pal) != EOF) {
		w=(char*)malloc(sizeof(char)*10);
		strcpy(w, pal);
		char *ptr = strtok(pal, delim);
		i=0;
		while(ptr != NULL)
		{
			if(i==0) idProceso = atoi(ptr);
			if(i==1) horaLlegada = atoi(ptr);
			if(i==2) duracion = atoi(ptr);	
			ptr = strtok(NULL, delim);
			i++;
		}
		jobs = InsOrd(idProceso, horaLlegada, duracion, jobs);
	}
	fclose ( fp );

	return jobs;
}