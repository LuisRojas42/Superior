/*
    \mainpage
    \author: Rojas Zepeda Luis Eduardo
    \version 1.0
    \date April 19 2019

*/
#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h> 
#include<sys/types.h> 
#include<string.h> 
#include <time.h>
#include<sys/wait.h> 
#include "../Include/libreria.h"

/**Cabecera funcion numRandom*/
void numRandom(int*, int);
/**Cabecera funcion numPares*/
void numPares(int*, int*, int, int);
/**Cabecera funcion numImpares*/
void numImpares(int*, int*, int, int);
/**Cabecera funcion imprimeArreglo*/
void imprimeArreglo(int, int*, char*);
/**Cabecera funcion sumaElementos*/
int sumaElementos(int*, int);

/**\brief Programa principal. */
int main() 
{ 
    int fd1[2];  
    int fd2[2];  
    int fd3[2];
    int fd4[2];
    int aux1[2];
    int aux2[2];

    srand(time(NULL));
    fflush(stdin);

    pid_t p;
    pid_t p2; 
    int n;
  
    if (pipe(fd1)==-1) 
    { 
        fprintf(stderr, "Error al iniciar pipe"); 
        return 1; 
    } 
    if (pipe(fd2)==-1) 
    { 
        fprintf(stderr, "Error al iniciar pipe"); 
        return 1; 
    } 
    if (pipe(fd3)==-1) 
    { 
        fprintf(stderr, "Error al iniciar pipe"); 
        return 1; 
    } 
    if (pipe(fd4)==-1) 
    { 
        fprintf(stderr, "Error al iniciar pipe"); 
        return 1; 
    } 
    if (pipe(aux1)==-1) 
    { 
        fprintf(stderr, "Error al iniciar pipe"); 
        return 1; 
    }
    if (pipe(aux2)==-1) 
    { 
        fprintf(stderr, "Error al iniciar pipe"); 
        return 1; 
    }

    printf("Numeros aleatorios:\n");
    scanf("%d", &n); 
  
    //Primer hijo
    p = fork(); 
  
    if (p < 0) 
    { 
        fprintf(stderr, "Error al iniciar fork"); 
        return 1; 
    }  
    else if (p > 0) 
    { 
        int random[n], cont=0, i, suma;
        //Se llana un arreglo con n numeros aleatoreos
        numRandom(random, n);

        for(i=0; i<n; i++)
            if(random[i]%2)
                cont++;

        int impares[cont];    
        //Se llena un arreglo con los valores impares del arreglo inicial
        numImpares(random, impares, n, cont);
  
        close(fd1[0]);  
        close(aux1[0]);
  
        write(aux1[1], &cont, sizeof(cont)); 
        write(fd1[1], impares, sizeof(impares)+1); 
        close(aux1[1]);
        close(fd1[1]); 
  
        wait(NULL); 
    
        close(fd2[1]);  
 
        read(fd2[0], &suma, sizeof(suma)); 
        printf("Suma de impares: %d\n", suma); 
        close(fd2[0]); 

        //Segundo hijo
        p2 = fork(); 
  
        if (p2 < 0) 
        { 
            fprintf(stderr, "Error al iniciar fork" ); 
            return 1; 
        } 
        else if (p2 > 0) 
        {       
            cont = n - cont;
            int pares[cont], suma;
            numPares(random, pares, n, cont);

            close(fd3[0]);  
            close(aux2[0]);
      
            write(aux2[1], &cont, sizeof(cont)); 
            write(fd3[1], pares, sizeof(pares)+1); 
            close(aux2[1]);
            close(fd3[1]); 
      
            wait(NULL); 
      
            close(fd4[1]); 
     
            read(fd4[0], &suma, sizeof(suma)); 
            printf("Suma de pares: %d\n", suma); 
            close(fd4[0]); 
        } 
        else
        { 
            close(fd3[1]);  
            close(aux2[1]);

            int cont, suma;

            read(aux2[0], &cont, sizeof(cont));
            int pares[cont];
            read(fd3[0], pares, sizeof(pares)); 
      
            suma = sumaElementos(pares, cont);
      
            close(fd3[0]); 
            close(fd4[0]); 
      
            write(fd4[1], &suma, sizeof(suma)); 
            close(fd4[1]); 
      
            exit(0); 
        }

    } 
    else
    { 
        close(fd1[1]); 
        close(aux1[1]);
  
        int cont, suma;

        read(aux1[0], &cont, sizeof(cont));
        int impares[cont];
        read(fd1[0], impares, sizeof(impares)); 
  
        suma = sumaElementos(impares, cont);
  
        close(fd1[0]); 
        close(fd2[0]); 
  
        write(fd2[1], &suma, sizeof(suma)); 
        close(fd2[1]); 
  
        exit(0); 
    } 
} 