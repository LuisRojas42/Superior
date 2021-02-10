#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h>
#include "cabeceras.h"

int main(){

	//Iniciamos memoria
	key_t Clave = genClave();
	int Id_Memoria = genIdMemoria(Clave);
	int *Memoria = getDireccion(Id_Memoria);

	//crea arreglo de semaforos
	int id = arraySemaforos(Clave);

    int producciones = 0;

	//Instrucciones
	while(producciones < 50){

        if(Memoria[0] == ' '){
            setSemUno_r(id);
            Memoria[0] = 'b';
            setSemUno_v(id);
        }else if(Memoria[1] == ' '){
            setSemDos_r(id);
            Memoria[1] = 'b';
            setSemDos_v(id);
        }else if(Memoria[2] == ' '){
            setSemTres_r(id);
            Memoria[2] = 'b';
            setSemTres_v(id);
        }else if(Memoria[3] == ' '){
            setSemCuatro_r(id);
            Memoria[3] = 'b';
            setSemCuatro_v(id);
        }else if(Memoria[4] == ' '){
            setSemCinco_r(id);
            Memoria[4] = 'b';
            setSemCinco_v(id);
        }else{
            producciones--;
        }
        producciones++;
    }

    printf("Terminado\n");

	//Liberamos la memoria
	desasociaMemoria(Memoria, Id_Memoria);
	return 0;
}

