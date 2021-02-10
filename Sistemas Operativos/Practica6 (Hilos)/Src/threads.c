/*
    \mainpage
    \author: Rojas Zepeda Luis Eduardo
    \version 1.0
    \date May 9 2019

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

/**
    \brief Estructura que servirá para parámetro de los hilos
*/
struct  filas
{
	int* filaA;
	int* filaB;	
	int columnas;
};


/**
    \brief Función que obtiene las dimensiones de la matriz de un archivo.
    \param name[30] Nombre del archivo.
    \return char* Dimensión de la matriz.
*/
char* getDimension(char name[30]){
	FILE *fp;
	char file[80];
	char pal[80];
	char *str;
	int filas;

	strcpy(file,name);
	strcat(file, ".txt");
	fp = fopen ( file, "r" );        
	if (fp==NULL) {fputs ("File error",stderr); exit (1);}

	if(fscanf(fp, "%s ", pal)!=EOF){
		str = (char *) malloc(sizeof(char) * sizeof(pal));
		strcpy(str, pal);
	}

	return str;
}


/**
    \brief Función que lee la matriz de un archivo.
    \param name[30] Nombre del archivo.
    \return int* Apuntador a la matriz generada a partir del archivo.
*/
int** leerArchivos(char name[30]){
	FILE *fp;
	char file[80];
	char pal[80];
	int i = 0, j = 0, k = 0, l=0, filas, columnas;
	int **matriz;

	strcpy(file,name);
	strcat(file, ".txt");
	fp = fopen ( file, "r" );        
	if (fp==NULL) {fputs ("File error",stderr); exit (1);}
	
	while(fscanf(fp, "%s ", pal)!=EOF){
		if(j==0){
			filas = pal[0] - '0';
			columnas = pal[2] -'0';
			matriz = (int **)malloc(filas*sizeof(int));
			for(i=0; i<filas; i++)
				matriz[i] = (int *)malloc(columnas*sizeof(int));
			
		}else{
			for(k=0; k<columnas; k++){
				matriz[j-1][k] = pal[l] - '0';
				l=l+2;
			}
		}
		l=0;
		j++;
	}

	printf("****  Matriz %s  ****\n", file);
	for (i = 0; i < filas; ++i){
		for (j = 0; j < columnas; ++j)
			printf("%d\t", matriz[i][j]);
		printf("\n");
	}
	printf("\n\n");

	fclose (fp);
	return matriz;
}


/**
    \brief Función que ejecutará cada hilo que se cree.
    \param *f estructura con una fila de dos diferentes matrices que se sumarán.
    \return filaSum fila resultante de sumar las filas de los parámetros.
*/
void *thread_routine(struct filas *f){
	int *filaSum = (int*)malloc(sizeof(int) * f->columnas), i;
	for(i = 0; i<f->columnas; i++)
		filaSum[i] = f->filaA[i] + f->filaB[i];
	
	pthread_exit(filaSum);
}


/**\brief Programa principal. */
int main(int argc, char *argv[]){
	
	int filas = 0, columnas, i, j, status;	
	int **mA = leerArchivos(argv[1]);
	int **mB = leerArchivos(argv[2]);
	int **mS;
	char *dimA = getDimension(argv[1]), *dimB = getDimension(argv[2]);

	if(argc < 2){
		printf("Argumentos incompletos \n");
		return -1;
	}
	if(*dimA!=*dimB){
		printf("dimensiones diferentes de las matrices\n");
		return -1;
	}

	filas = dimA[0] - '0';
	columnas = dimA[2] - '0';
	pthread_t thread[filas];
	mS = (int **)malloc(filas*sizeof(int));
	for(i=0; i<filas; i++)
		mS[i] = (int *)malloc(columnas*sizeof(int));

	for(i = 0; i < filas; i++){
		printf("creando hilo para fila %d\n", i);
		struct filas f = {mA[i], mB[i], columnas};
		int *filaSum = (int*)malloc(sizeof(int) * f.columnas);
		status = pthread_create(&thread[i], NULL, (void*)thread_routine, (void*)&f);
		pthread_join(thread[i], (void **) &filaSum);
		for(j = 0; j<columnas; j++)
			mS[i][j] = filaSum[j];

	}

	printf("\n");
	for (i = 0; i < filas; ++i){
		for (j = 0; j < columnas; ++j)
			printf("%d\t", mS[i][j]);
		printf("\n");
	}

	return 0;
}