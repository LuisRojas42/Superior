#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include "Lista.h"

//Orden parametros de txt: idProceso, Llegada, Duracion

/**Cabecera funcion listaJobs*/
Lista listaJobs();

/**Cabecera funcion imprimeCola*/
void imprimeLista(Lista);

int main(){
	int tiempo=0, ejecutandose=0;
	Lista jobs = listaJobs();
	Lista ready = vacia();	
	imprimeLista(jobs);

	while(ejecutandose!=0 || !esVacia(jobs) || !esVacia(ready)){
		if(!esVacia(jobs)){
			ejecutandose++;
			//hilo
			printf("\nProceso %d\n", idProceso(jobs));
			while(duracion(jobs)!=0){
				printf("duracion %d\n", duracion(jobs));
				jobs->duracion--;
				sleep(1);
			}
		}
		ejecutandose--;
		jobs = resto(jobs);
	}	

	return 0;
}

/*	*\brief Imprime en formato de tabla la cola de procesos actual.
  	*\param ready Es una cola con los procesos listos para ejecutare esperando su turno.
*/
void imprimeLista(Lista jobs){
	printf("IdProceso\tHoraLLegada\tDuracion\n");
	impLista(jobs);
	printf("\n");
}

/*	*\brief Obtiene de un archivo de texto los procesos con sus respectivos valores y los enlista segun su duracion
	*\return jobs Es una lista con todos los procesos y sus atributos ordenados segun su duracion
*/

void *thread_routine(void *arg){
	//printf("Hilo %d ejecutandose\n", idProceso(*((Lista*)arg)));
	printf("Hilo %d ejecutandose\n", *((int*)arg));
}

Lista listaJobs(){

	int tam=0;
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
		tam++;
	}
	fclose ( fp );

	pthread_t thread[tam];
	int id[tam];
	Lista hilos = jobs; 
	for(int j = 0; j<tam; j++){
		id[j]=hilos->idProceso;
		if(0 != pthread_create(&thread[j], NULL, thread_routine, (void*)&id[j])){
			printf("error\n");
		}
		if(!esVacia(resto(hilos)))
			hilos = resto(hilos);
		
	}

	for(int j = 0; j<tam; j++){
		pthread_join(thread[j], NULL);
	}

	return jobs;
}