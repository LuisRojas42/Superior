#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

/*
	Token con su información
*/
struct  token
{
	int IdEmisor;
	int IdReceptor;	
	int tipo; //0 para información, 1 para confirmación de llegada, 2 para espera
	int posicion;
};

struct tks
{
	struct token t1;
	struct token t2;
};

//###########################################################
/*
	Nodos en red circular
*/

//Nodo uno
void* NodoUnoRC(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 1 && tokens->t1.tipo != 2){
			printf("token 1 en nodo uno\n");
			if(tokens->t1.tipo == 0){
				if(tokens->t1.IdReceptor==1){
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else if(tokens->t1.IdReceptor > 4){
					tokens->t1.posicion = 5;
				}else{
					tokens->t1.posicion = 2;
				}
			}else if(tokens->t1.tipo == 1){
				if(tokens->t1.IdEmisor==1){
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 2;
				}
			}
		}
		if(tokens->t2.posicion == 1 && tokens->t2.tipo != 2){
			printf("token 2 en nodo uno\n");
			if(tokens->t2.tipo == 0){
				if(tokens->t2.IdReceptor==1){
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else if(tokens->t2.IdReceptor > 4){
					tokens->t2.posicion = 5;
				}else{
					tokens->t2.posicion = 4;
				}
			}else if(tokens->t2.tipo == 1){
				if(tokens->t2.IdEmisor==1){
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 4;
				}
			}
		}
	}
}

//Nodo dos
void* NodoDosRC(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 2 && tokens->t1.tipo != 2){
			printf("token 1 en nodo dos\n");
			if(tokens->t1.tipo == 0){
				if(tokens->t1.IdReceptor==2){
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else{
					tokens->t1.posicion = 3;
				}
			}else if(tokens->t1.tipo == 1){
				if(tokens->t1.IdEmisor==2){
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 3;
				}
			}
		}
		if(tokens->t2.posicion == 2 && tokens->t2.tipo != 2){
			printf("token 2 en nodo dos\n");
			if(tokens->t2.tipo == 0){
				if(tokens->t2.IdReceptor==2){
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else{
					tokens->t2.posicion = 1;
				}
			}else if(tokens->t2.tipo == 1){
				if(tokens->t2.IdEmisor==2){
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 1;
				}
			}
		}	
	}
}

//Nodo tres
void* NodoTresRC(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 3 && tokens->t1.tipo != 2){
			printf("token 1 en nodo tres\n");
			if(tokens->t1.tipo == 0){
				if(tokens->t1.IdReceptor==3){
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else{
					tokens->t1.posicion = 4;
				}
			}else if(tokens->t1.tipo == 1){
				if(tokens->t1.IdEmisor==3){
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 4;
				}
			}
		}
		if(tokens->t2.posicion == 3 && tokens->t2.tipo != 2){
			printf("token 2 en nodo tres\n");
			if(tokens->t2.tipo == 0){
				if(tokens->t2.IdReceptor==3){
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else{
					tokens->t2.posicion = 2;
				}
			}else if(tokens->t2.tipo == 1){
				if(tokens->t2.IdEmisor==3){
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 2;
				}
			}
		}
	}
}

//Nodo cuatro
void* NodoCuatroRC(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 4 && tokens->t1.tipo != 2){
			printf("token 1 en nodo cuatro\n");
			if(tokens->t1.tipo == 0){
				if(tokens->t1.IdReceptor==4){
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else{
					tokens->t1.posicion = 1;
				}
			}else if(tokens->t1.tipo == 1){
				if(tokens->t1.IdEmisor==4){
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 1;
				}
			}
		}
		if(tokens->t2.posicion == 4 && tokens->t2.tipo != 2){
			printf("token 2 en nodo cuatro\n");
			if(tokens->t2.tipo == 0){
				if(tokens->t2.IdReceptor==4){
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else{
					tokens->t2.posicion = 3;
				}
			}else if(tokens->t2.tipo == 1){
				if(tokens->t2.IdEmisor==4){
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 3;
				}
			}
		}
	}
}


//###########################################################
/*
	Nodos en red jerarquica
*/
//Nodo uno de red jerarquica, nodo cinco en conjunto
void* NodoUnoRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 5 && tokens->t1.tipo != 2){
			printf("token 1 en nodo uno de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==5){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else if(tokens->t1.IdReceptor < 5){ //el receptor no esta en esta red
					tokens->t1.posicion = 1;
				}else{ //el receptor si esta en esta red
					if(tokens->t1.IdReceptor < 8) //el recptor esta en la rama 1
						tokens->t1.posicion = 6;	
					else if(tokens->t1.IdReceptor < 10) //el recptor esta en la rama 2
						tokens->t1.posicion = 8;	
					else if(tokens->t1.IdReceptor < 12) //el recptor esta en la rama 3
						tokens->t1.posicion = 10;	
				}
			}else if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==5){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else if(tokens->t1.IdEmisor < 5){ //el emisor no esta en esta red
					tokens->t1.posicion = 1;
				}else{
					if(tokens->t1.IdEmisor < 8) //el emisor esta en la rama 1
						tokens->t1.posicion = 6;	
					else if(tokens->t1.IdEmisor < 10) //el emisor esta en la rama 2
						tokens->t1.posicion = 8;	
					else if(tokens->t1.IdEmisor < 12) //el emisor esta en la rama 3
						tokens->t1.posicion = 10;	
				}
			}
		}
		if(tokens->t2.posicion == 5 && tokens->t2.tipo != 2){
			printf("token 2 en nodo uno de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==5){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else if(tokens->t2.IdReceptor < 5){ //el receptor no esta en esta red
					tokens->t2.posicion = 1;
				}else{ //el receptor si esta en esta red
					if(tokens->t2.IdReceptor < 8) //el recptor esta en la rama 1
						tokens->t2.posicion = 6;	
					else if(tokens->t2.IdReceptor < 10) //el recptor esta en la rama 2
						tokens->t2.posicion = 8;	
					else if(tokens->t2.IdReceptor < 12) //el recptor esta en la rama 3
						tokens->t2.posicion = 10;	
				}
			}else if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==5){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else if(tokens->t2.IdEmisor < 5){ //el emisor no esta en esta red
					tokens->t2.posicion = 1;
				}else{
					if(tokens->t2.IdEmisor < 8) //el emisor esta en la rama 1
						tokens->t2.posicion = 6;	
					else if(tokens->t2.IdEmisor < 10) //el emisor esta en la rama 2
						tokens->t2.posicion = 8;	
					else if(tokens->t2.IdEmisor < 12) //el emisor esta en la rama 3
						tokens->t2.posicion = 10;	
				}
			}
		}
	}
}


//Nodo dos de red jerarquica, nodo seis en conjunto
void* NodoDosRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 6 && tokens->t1.tipo != 2){
			printf("token 1 en nodo dos de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==6){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else if(tokens->t1.IdReceptor < 6){ //el receptor esta hacia arriba de la red
					tokens->t1.posicion = 5;
				}else{
					tokens->t1.posicion = 7;
				}
			}
			if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==6){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else if(tokens->t1.IdEmisor < 6){ //el emisor esta hacia arriba de la red
					tokens->t1.posicion = 5;
				}else{
					tokens->t1.posicion = 7;
				}
			}
		}
		if(tokens->t2.posicion == 6 && tokens->t2.tipo != 2){
			printf("token 2 en nodo dos de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==6){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else if(tokens->t2.IdReceptor < 6){ //el receptor esta hacia arriba de la red
					tokens->t2.posicion = 5;
				}else{
					tokens->t2.posicion = 7;
				}
			}
			if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==6){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else if(tokens->t2.IdEmisor < 6){ //el emisor esta hacia arriba de la red
					tokens->t2.posicion = 5;
				}else{
					tokens->t2.posicion = 7;
				}
			}
		}
	}
}

//Nodo tres de red jerarquica, nodo ocho en conjunto
void* NodoTresRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 8 && tokens->t1.tipo != 2){
			printf("token 1 en nodo tres de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==8){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else if(tokens->t1.IdReceptor < 8){ //el receptor esta hacia arriba de la red
					tokens->t1.posicion = 5;
				}else{
					tokens->t1.posicion = 9;
				}
			}
			if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==8){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else if(tokens->t1.IdEmisor < 8){ //el emisor esta hacia arriba de la red
					tokens->t1.posicion = 5;
				}else{
					tokens->t1.posicion = 9;
				}
			}
		}
		if(tokens->t2.posicion == 8 && tokens->t2.tipo != 2){
			printf("token 2 en nodo tres de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==8){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else if(tokens->t2.IdReceptor < 8){ //el receptor esta hacia arriba de la red
					tokens->t2.posicion = 5;
				}else{
					tokens->t2.posicion = 9;
				}
			}
			if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==8){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else if(tokens->t2.IdEmisor < 8){ //el emisor esta hacia arriba de la red
					tokens->t2.posicion = 5;
				}else{
					tokens->t2.posicion = 9;
				}
			}
		}
	}
}

//Nodo cuatro de red jerarquica, nodo diez en conjunto
void* NodoCuatroRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 10 && tokens->t1.tipo != 2){
			printf("token 1 en nodo cuatro de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==10){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else if(tokens->t1.IdReceptor < 10){ //el receptor esta hacia arriba de la red
					tokens->t1.posicion = 5;
				}else if(tokens->t1.IdReceptor < 12){
					tokens->t1.posicion = 11;
				}else{
					tokens->t1.posicion = 12;
				}
			}
			if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==10){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else if(tokens->t1.IdEmisor < 10){ //el emisor esta hacia arriba de la red
					tokens->t1.posicion = 5;
				}else if(tokens->t1.IdEmisor < 12){
					tokens->t1.posicion = 11;
				}else{
					tokens->t1.posicion = 12;
				}
			}
		}
		if(tokens->t2.posicion == 10 && tokens->t2.tipo != 2){
			printf("token 2 en nodo cuatro de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==10){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else if(tokens->t2.IdReceptor < 10){ //el receptor esta hacia arriba de la red
					tokens->t2.posicion = 5;
				}else if(tokens->t2.IdReceptor < 12){
					tokens->t2.posicion = 11;
				}else{
					tokens->t2.posicion = 12;
				}
			}
			if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==10){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else if(tokens->t2.IdEmisor < 10){ //el emisor esta hacia arriba de la red
					tokens->t2.posicion = 5;
				}else if(tokens->t2.IdEmisor < 12){
					tokens->t2.posicion = 11;
				}else{
					tokens->t2.posicion = 12;
				}
			}
		}
	}
}

//Nodo cinco de red jerarquica, nodo siete en conjunto
void* NodoCincoRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 7 && tokens->t1.tipo != 2){
			printf("token 1 en nodo cinco de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==7){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else{
					tokens->t1.posicion = 6;
				}
			}
			if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==7){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 6;
				}
			}
		}
		if(tokens->t2.posicion == 7 && tokens->t2.tipo != 2){
			printf("token 2 en nodo cinco de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==7){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else{
					tokens->t2.posicion = 6;
				}
			}
			if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==7){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 6;
				}
			}
		}
	}
}

//Nodo seis de red jerarquica, nodo nueve en conjunto
void* NodoSeisRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 9 && tokens->t1.tipo != 2){
			printf("token 1 en nodo seis de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==9){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else{
					tokens->t1.posicion = 8;
				}
			}
			if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==9){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 8;
				}
			}
		}
		if(tokens->t2.posicion == 9 && tokens->t2.tipo != 2){
			printf("token 2 en nodo seis de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==9){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else{
					tokens->t2.posicion = 8;
				}
			}
			if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==9){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 8;
				}
			}
		}
	}
}

//Nodo siete de red jerarquica, nodo once en conjunto
void* NodoSieteRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 11 && tokens->t1.tipo != 2){
			printf("token 1 en nodo siete de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==11){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else{
					tokens->t1.posicion = 10;
				}
			}
			if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==11){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 10;
				}
			}
		}
		if(tokens->t2.posicion == 11 && tokens->t2.tipo != 2){
			printf("token 2 en nodo siete de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==11){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else{
					tokens->t2.posicion = 10;
				}
			}
			if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==11){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 10;
				}
			}
		}
	}
}


//Nodo ocho de red jerarquica, nodo doce en conjunto
void* NodoOchoRJ(struct tks *tokens){
	while(1){
		sleep(1); 
		if(tokens->t1.posicion == 12 && tokens->t1.tipo != 2){
			printf("token 1 en nodo ocho de red jerarquica\n");
			if(tokens->t1.tipo == 0){ //busca receptor
				if(tokens->t1.IdReceptor==12){ //este es el receptor
					printf("Token 1 recibido\n");
					tokens->t1.tipo = 1;
				}else{
					tokens->t1.posicion = 10;
				}
			}
			if(tokens->t1.tipo == 1){ //busca emisor
				if(tokens->t1.IdEmisor==12){ //este es el emisor
					printf("Token 1 confirmado\n");
					tokens->t1.tipo = 2;
				}else{
					tokens->t1.posicion = 10;
				}
			}
		}
		if(tokens->t2.posicion == 12 && tokens->t2.tipo != 2){
			printf("token 2 en nodo cinco de red jerarquica\n");
			if(tokens->t2.tipo == 0){ //busca receptor
				if(tokens->t2.IdReceptor==12){ //este es el receptor
					printf("Token 2 recibido\n");
					tokens->t2.tipo = 1;
				}else{
					tokens->t2.posicion = 10;
				}
			}
			if(tokens->t2.tipo == 1){ //busca emisor
				if(tokens->t2.IdEmisor==12){ //este es el emisor
					printf("Token 2 confirmado\n");
					tokens->t2.tipo = 2;
				}else{
					tokens->t2.posicion = 10;
				}
			}
		}
	}
}

void main(){
	pthread_t nodoUnoRC;
	pthread_t nodoDosRC;
	pthread_t nodoTresRC;
	pthread_t nodoCuatroRC;

	pthread_t nodoUnoRJ;
	pthread_t nodoDosRJ;
	pthread_t nodoTresRJ;
	pthread_t nodoCuatroRJ;
	pthread_t nodoCincoRJ;
	pthread_t nodoSeisRJ;
	pthread_t nodoSieteRJ;
	pthread_t nodoOchoRJ;

	//Se inicializa el token 1 (solo se mueve en sentido horario) en el nodo 1
	struct token t1;
	t1.IdEmisor = 1;
	t1.IdReceptor = 3;
	t1.tipo = 0;
	t1.posicion = 1;

	//Se inicializa el token 2 (solo se mueve en sentido antihorario) en el nodo 2
	struct token t2;
	t2.IdEmisor = 6;
	t2.IdReceptor = 11;
	t2.tipo = 0;
	t2.posicion = 2;

	struct tks tokens;
	tokens.t1 = t1;
	tokens.t2 = t2;

	pthread_create(&nodoUnoRC, NULL, (void*)NodoUnoRC, (void*)&tokens);
	pthread_create(&nodoDosRC, NULL, (void*)NodoDosRC, (void*)&tokens);
	pthread_create(&nodoTresRC, NULL, (void*)NodoTresRC, (void*)&tokens);
	pthread_create(&nodoCuatroRC, NULL, (void*)NodoCuatroRC, (void*)&tokens);

	pthread_create(&nodoUnoRJ, NULL, (void*)NodoUnoRJ, (void*)&tokens);
	pthread_create(&nodoDosRJ, NULL, (void*)NodoDosRJ, (void*)&tokens);
	pthread_create(&nodoTresRJ, NULL, (void*)NodoTresRJ, (void*)&tokens);
	pthread_create(&nodoCuatroRJ, NULL, (void*)NodoCuatroRJ, (void*)&tokens);
	pthread_create(&nodoCincoRJ, NULL, (void*)NodoCincoRJ, (void*)&tokens);
	pthread_create(&nodoSeisRJ, NULL, (void*)NodoSeisRJ, (void*)&tokens);
	pthread_create(&nodoSieteRJ, NULL, (void*)NodoSieteRJ, (void*)&tokens);
	pthread_create(&nodoOchoRJ, NULL, (void*)NodoOchoRJ, (void*)&tokens);

	while(1){
		sleep(1);
	}
}