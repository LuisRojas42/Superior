typedef int Elem;

/**
	\brief Estructura que funciona como un nodo de la lista enlazada en un solo sentido, contien los atributos de cada proceso 
	y un apuntador al nodo del siguiente proceso.
*/
typedef struct Nodo{
    Elem idProceso;
    Elem horaLlegada;
    Elem duracion;
	struct Nodo *sig;
}*Nodo;

typedef Nodo Lista;

/**
	\brief Inicializa una lista vacia.
	\return NULL representa el valor vacio de la lista.
*/
Lista vacia(){
	return NULL;
}

/**
	\brief Función observadora que permite saber si la Lista esta vacia.
	\param l Lista que se desea observar.
	\return int entero con valor 0 para falso y algo diferente para verdadero.
*/
int esVacia(Lista l){
	return l==NULL;
}

/**
	\brief Funcion que permite agregar elementos a la estructura.
	\param idProceso Identificador del proceso.
	\param horaLlegada Hora de llegada del proceso.
	\param duracion Duracion del procesos.
	\param l Lista a la que se formara el proceso.
	\return t Lista con el proceso agragado.
*/
Lista cons(Elem idProceso, Elem horaLlegada, Elem duracion, Lista l){
    Lista t=(Lista)malloc(sizeof(struct Nodo));
    t->idProceso = idProceso;
    t->horaLlegada = horaLlegada;
    t->duracion = duracion;
    t->sig=l;
    return t;
}

/**
	\brief Función que permite acceder al identificador del primer elemento de la lista.
	\param l Lista que se consultará.
	\return idProceso Identificador del proceso consultado.
*/
Elem idProceso(Lista l){
	return l->idProceso;
}

/**
	\brief Función que permite acceder a la hora de llegada del primer elemento de la lista.
	\param l Lista que se consultará.
	\return horaLlegada Hora de llegada del proceso consultado.
*/
Elem horaLlegada(Lista l){
	return l->horaLlegada;
}

/**
	\brief Función que permite acceder a la duración del primer elemento de la lista.
	\param l Lista que se consultará.
	\return duracion Duración del proceso consultado.
*/
Elem duracion(Lista l){
	return l->duracion;
}

/**
	\brief FUncion que desenlista al primer elemento de la lista.
	\param l Lista que modificará.
	\return l->sig lista con el primer elemento retirado.
*/
Lista resto(Lista l){
	return l->sig;
}

/**
	\brief Imprime un dato.
	\param e Dato que se desea imprimir.
*/
void impElem(Elem idProceso, Elem horaLlegada, Elem duracion){
	printf("%d\t\t%d\t\t%d\n",idProceso, horaLlegada, duracion);
}

/**
	\brief Imprime una lista.
	\param l Lista que desea imprimir.
*/
void impLista(Lista l){
	if(!esVacia(l)){
		Lista t=(Lista)malloc(sizeof(struct Nodo));
		impElem(idProceso(l), horaLlegada(l), duracion(l));
		t->sig=l->sig;
		impLista(resto(t));
	}
}
/**
	\brief Compara dos datos para saber cual es mayor.
	\param e primer dato a comparar.
	\param e1 segundo dato a comparar.
	\return entero con valor 0 si es falso y cualquier otro valor para verdadero.
*/
int EsMoI(Elem e,Elem e1){
	return e<e1;
}

/**
	\brief Inserta en orden un proceso segun su hora de llegada en una lista de procesos. 
	\param idP Identificador del proceso.
	\param horaLl Hora de llegada del proceso.
	\param dcn Duración del proceso.
	\param l Lista a la que se desea insertar el proceso.
	\return Lista con el nuevo proceso insertado
*/
Lista InsOrd(Elem idP, Elem horaLl, Elem dcn, Lista l){
	return (esVacia(l))?(cons(idP, horaLl, dcn,vacia())):((EsMoI(dcn,duracion(l)))?
		(cons(idP, horaLl, dcn, l)):(cons(idProceso(l), horaLlegada(l), duracion(l), 
			InsOrd(idP, horaLl, dcn, resto(l)))));
}
