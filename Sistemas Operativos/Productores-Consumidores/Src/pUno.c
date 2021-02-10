#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h>
#include "cabeceras.h"

int main(){

	//Iniciamos memoria
	key_t Clave = genClave();
	int Id_Memoria = genIdMemoria(Clave);
	int *Memoria = getDireccion(Id_Memoria);
    Memoria[0] = ' '; Memoria[1] = ' '; Memoria[2] = ' '; Memoria[3] = ' '; Memoria[4] = ' ';

	//crea arreglo de semaforos
	int id = arraySemaforos(Clave);
    iniciaSemaforos(id);

    int producciones = 0;

	//Instrucciones
	while(producciones < 50){

        if(Memoria[0] == ' '){
            setSemUno_r(id);
            Memoria[0] = 'a';
            setSemUno_v(id);
        }else if(Memoria[1] == ' '){
            setSemDos_r(id);
            Memoria[1] = 'a';
            setSemDos_v(id);
        }else if(Memoria[2] == ' '){
            setSemTres_r(id);
            Memoria[2] = 'a';
            setSemTres_v(id);
        }else if(Memoria[3] == ' '){
            setSemCuatro_r(id);
            Memoria[3] = 'a';
            setSemCuatro_v(id);
        }else if(Memoria[4] == ' '){
            setSemCinco_r(id);
            Memoria[4] = 'a';
            setSemCinco_v(id);
        }else{
            producciones--;
        }
        producciones++;
    }

    printf("Terminado\n");

    while(1);
	//Liberamos la memoria
	liberaMemoria(Memoria, Id_Memoria);
	return 0;
}

