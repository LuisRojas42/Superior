/*
	\Libreria del TDA cola
	\author: Rojas Zepeda Luis Eduardo
	\version 1.0
	\date March 31 2019

*/

typedef int Elem;

/**
	\brief Estructura que funciona como un nodo de la Cola circular, contien los atributos de cada proceso 
	y un apuntador al nodo del siguiente proceso.
*/
typedef struct nodo{
    Elem idProceso;
    Elem horaLlegada;
    Elem duracion;
	struct nodo *sig;
}*apNodo;

/**
	\brief Estructura que apunta al primer y ultimo elemento de la Cola.
*/
typedef struct CNodo{
	apNodo prim;
	apNodo ult;
}*Cola;

/**
	\brief Inicializa una Cola vacia.
	\return NULL representa el valor vacio de la Cola.
*/
Cola nueva(){
	Cola t=(Cola)malloc(sizeof(struct CNodo));
	t->prim=t->ult=NULL;
	return t;
}

/**
	\brief Función observadora que permite saber si la Cola esta vacia.
	\param q Cola que se desea observar.
	\return int entero con valor 0 para falso y algo diferente para verdadero.
*/
int esNueva(Cola q){
	return (q->prim==NULL)&&(q->ult==NULL);
}

/**
	\brief Funcion que permite agregar elementos a la estructura.
	\param q Cola a la que se formara el proceso.
	\param idProceso Identificador del proceso.
	\param horaLlegada Hora de llegada del proceso.
	\param duracion Duracion del procesos.
	\return q Cola con el proceso agragado.
*/
Cola formar(Cola q, Elem idProceso, Elem horaLlegada, Elem duracion){
	apNodo t=(apNodo)malloc(sizeof(struct nodo));
	t->idProceso = idProceso;
    t->horaLlegada = horaLlegada;
    t->duracion = duracion;
	if(esNueva(q)){
		q->prim=q->ult=t;
		t->sig=NULL;
	}else{
		q->ult->sig=t;
		q->ult=t;
		t->sig=NULL;
	}
	return q;
}

/**
	\brief Función que permite acceder al identificador del primer elemento de la Cola.
	\param q Cola que se consultará.
	\return idProceso Identificador del proceso consultado.
*/
Elem idProcesoC(Cola q){
	return q->prim->idProceso;
}

/**
	\brief Función que permite acceder a la hora de llegada del primer elemento de la Cola.
	\param q COla que se consultará.
	\return horaLlegada Hora de llegada del proceso consultado.
*/
Elem horaLlegadaC(Cola q){
	return q->prim->horaLlegada;
}

/**
	\brief Función que permite acceder a la duración del primer elemento de la Cola.
	\param q Cola que se consultará.
	\return duracion Duración del proceso consultado.
*/
Elem duracionC(Cola q){
	return q->prim->duracion;
}

/**
	\brief Función que reduce en una unidad la duración del primer elemento de la Cola.
	\param q Cola que se modificará.
*/
void restaDuracion(Cola q){
	q->prim->duracion--;
}

/**
	\brief Función que desforma el primer elemento de la Cola.
	\param q Cola que se modificará.
	\return q Cola con el primer elemento retirado.
*/
Cola desformar(Cola q){
	if(q->prim==q->ult){
		q->prim=q->ult=NULL;
	}else{
		q->prim=q->prim->sig;
	}
	return q;
}

/**
	\brief Imprime los datos de un proceso.
	\param idProceso Identificador que se desea imprimir.
	\param duracion Duracion que se desea imprimir.
	\param horaLlegada Hora de llegada que se desea imprimir.
*/
void impElemC(Elem idProceso, Elem horaLlegada, Elem duracion){
	printf("%d\t\t%d\t\t%d\n",idProceso, horaLlegada, duracion);
}

/**
	\brief Imprime una Cola.
	\param q COla que desea imprimir.
*/
void impCola(Cola q){
	if(!esNueva(q)){
		Cola t=(Cola)malloc(sizeof(struct CNodo));
		impElemC(idProcesoC(q), horaLlegadaC(q), duracionC(q));
		t->prim=q->prim;
		t->ult=q->ult;
		impCola(desformar(t));
	}
}

/**
	\brief Función que desforma el primer elemento de la Cola y lo forma nuevamente pero hasta el final de esta.
	\param q Cola que se modificará.
	\return Cola modificada.
*/
Cola rotar(Cola q){
	if(esNueva(q)){
		return q;
	}else{
		return formar(desformar(q),idProcesoC(q), horaLlegadaC(q), duracionC(q));
	}
}