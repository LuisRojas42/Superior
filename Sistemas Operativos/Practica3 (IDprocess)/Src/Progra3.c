/**
programa: Practica 3 programa 3
Autor: Rojas Zepeda Luis Eduardo
Fecha: 18/03/2019
Descripcion: Ciclo durante 30 segundos imprimiendo un mensaje y el proceso del id. 
			Esta la posibilidad de interruptir el programa con CTRL+C mostrando un mensaje.
*/


#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "../Include/tiempo.h"
#include <signal.h>

/**
 *@brief INThandler se manda a llamar cada que se presiona CTRL+C e imprime un mensaje y termina el programa. 
 *@param numero entero para identificar la señal
 *@return vacio
 */
void INThandler(int);

int main(){
		
	double utime0, stime0, wtime0,utime1, stime1, wtime1; //Variables para medición de tiempos	
		
	uswtime(&utime0, &stime0, &wtime0);
	
	signal(SIGINT, INThandler);
	
	while((wtime1 - wtime0) < 30 ){
		printf("Aqui estoy\n");
		printf("Id: %d\n", getpid());
		uswtime(&utime1, &stime1, &wtime1);
	}
	
	printf("Terminacion normal");
	
	return 0;
}


void INThandler(int sig)
{
     signal(sig, SIG_IGN);
     printf("Terminacion por interrupcion del SO\n\n");
     exit(0);
}
