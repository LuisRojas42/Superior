#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h> //Memoria compartida
#include <sys/ipc.h>
#include <string.h>
#include <unistd.h> 
#include <sys/types.h> 


#define TAM 1024

int main(){
    int pid, memoriaID;
    char *punteroAMemoriaCompartida = NULL;
    
    if((memoriaID = shmget(1315511,TAM,0664|IPC_CREAT))==-1) { //El primer valor es un identificador unico, puede dar problemas
        fprintf(stderr,"Error al reservar la memoria");
    } //Creo la memoria compartida
    
    pid = fork();
    switch(pid) {
        case -1:
            fprintf(stderr,"Error al hacer el fork");
        break;
        case 0: //El hijo
        	printf("proceso Hijo Iniciado\n\n");
            punteroAMemoriaCompartida = shmat(memoriaID,(void *)0,0); //Asociacion
            strcpy(punteroAMemoriaCompartida,"Iniciando comunicación");
            sleep(2);
            printf("numeros: %s\n", punteroAMemoriaCompartida);
            char *enteros = punteroAMemoriaCompartida;
            int num1 = enteros[0] - '0';
            int num2 = enteros[2] - '0';
            int sum = num1 + num2;
            sprintf(enteros, "%d", sum);
            strcpy(punteroAMemoriaCompartida,enteros);
            sleep(2);
            strcpy(punteroAMemoriaCompartida,"Finalizando comunicación");
        break;
        default:
        	printf("proceso Padre Iniciado\n\n");
            sleep(2); 
            punteroAMemoriaCompartida = shmat(memoriaID,NULL,0); //Asociacion
			if (strcmp(punteroAMemoriaCompartida, "Iniciando comunicación") == 0){
				printf("%s\n", punteroAMemoriaCompartida);
				strcpy(punteroAMemoriaCompartida,"5 6");
			}
			sleep(2);
			printf("Suma = %s\n", punteroAMemoriaCompartida);
			sleep(2);
			printf("%s\n", punteroAMemoriaCompartida);
            shmdt(&punteroAMemoriaCompartida); //Desasociacion
            if(shmctl(memoriaID,IPC_RMID,NULL)==-1){
                fprintf(stderr,"Error al liberar la memoria");
            }
        break;          
    }   
    return 0;
}