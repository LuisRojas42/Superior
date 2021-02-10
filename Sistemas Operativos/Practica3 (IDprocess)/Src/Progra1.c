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

int main(){
	
	while(1){
		printf("Aqui estoy\n");
		printf ( "Id: %d\n", getpid());
	}
	return 0;
}