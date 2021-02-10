#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h>
#include <time.h>
#include "cabeceras.h"

int lineasA=0;
int lineasB=0;
int lineasC=0;
int total = 0;

int main(){

	//Iniciamos memoria
	key_t Clave = genClave();
	int Id_Memoria = genIdMemoria(Clave);
	int *Memoria = getDireccion(Id_Memoria);

    //Iniciamos semaforos
	int id = arraySemaforos(Clave);

    //Ficheros
    FILE *a, *b, *c;
    a = fopen ( "a.txt", "w" );   
    b = fopen ( "b.txt", "w" );   
    c = fopen ( "c.txt", "w" );   

    clock_t t,ts;
    int segundos=0;
    ts=clock()+CLOCKS_PER_SEC;

	//Instrucciones
	while(segundos<1){
        
        if(Memoria[0] != ' '){
            setSemSeis_r(id);
                total++;
                escribe(Memoria[0], a, b, c);
                Memoria[0] = ' ';
            setSemSeis_v(id);
        }else if(Memoria[1] != ' '){
            setSemSiete_r(id);
                total++;
                escribe(Memoria[1], a, b, c);
                Memoria[1] = ' ';
            setSemSiete_v(id);
        }else if(Memoria[2] != ' '){
            setSemOcho_r(id);
                total++;
                escribe(Memoria[2], a, b, c);
                Memoria[2] = ' ';
            setSemOcho_v(id);
        }else if(Memoria[3] != ' '){
            setSemNueve_r(id);
                total++;
                escribe(Memoria[3], a, b, c);
                Memoria[3] = ' ';
            setSemNueve_v(id);
        }else if(Memoria[4] != ' '){
            setSemDiez_r(id);
                total++;
                escribe(Memoria[4], a, b, c);
                Memoria[4] = ' ';
            setSemDiez_v(id);
        }

        if((t=clock())>=ts)
        {
            printf("%d\n",++segundos);
            ts=t+CLOCKS_PER_SEC;
        }
    }

    printf("Terminado\n");
    
    fclose ( a ); 
    fclose ( b ); 
    fclose ( c ); 

	//Desasociamos la memoria
	desasociaMemoria(Memoria, Id_Memoria);
 
	return 0;
}


void escribe(char l, FILE *a, FILE *b, FILE *c){
    switch(l){
        case 'a':
            fputc('a', a);
            fputc('\n', a);
            printf("es a\n");
            //lineasA++;
            break;
        case 'b':
            fputc('b', b);
            fputc('\n', b);
            printf("es b\n");
            //lineasB++;
            break;
        case 'c':
            fputc('c', c);
            fputc('\n', c);
            printf("es c\n");
            //lineasC++;
            break;
    }
}