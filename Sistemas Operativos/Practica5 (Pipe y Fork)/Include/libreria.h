/*
    \Libreria de funciones para arreglos
    \author: Rojas Zepeda Luis Eduardo
    \version 1.0
    \date Aprl 9 2019

*/

/**
    \brief Función que imprime los elemtos de un arreglo.
    \param cont Entero con valor del tamaño del arreglo.
    \param array Apuntador a entero con direccion del arreglo.
    \param cadena Apuntador a cadena del nombre del arreglo.
*/
void imprimeArreglo(int cont, int* array, char* cadena){
    int i;
    printf("\n");
    for(i=0; i<cont; i++)
        printf("%s[%d] = %d\n", cadena, i, array[i]);    
}

/**
    \brief Función que asigna valores aleatoreos a un arreglo.
    \param random Apuntador a entero con dereccion del arreglo.
    \param tam Entero con valor del tamaño del arreglo.
    \return int entero con valor 0 para falso y algo diferente para verdadero.
*/
void numRandom(int* random, int tam){
    int i;
    for(i=0; i<tam; i++)
        random[i] = rand() % 100;

    imprimeArreglo(tam, random, "random");
}

/**
    \brief Función que asigna los valores impares de un arreglo a otro.
    \param random Apuntador a entero con dereccion del arreglo completo.
    \param impares Apuntador a entero con direccion del arreglo al que solo se le quiere asignar valores impares.
    \param tam Entero con valor del tamaño del arreglo.
    \param cont Entero con valor del numero de numeros impares en el arreglo completo.
*/
void numImpares(int* random, int* impares, int tam, int cont){
    int j=0, i=0;
    for(i=0; i<tam; i++)
        if(random[i]%2){
            impares[j] = random[i];
            j++;
        }

    imprimeArreglo(cont, impares, "impares");
}

/**
    \brief Función que asigna los valores pares de un arreglo a otro.
    \param random Apuntador a entero con dereccion del arreglo completo.
    \param pares Apuntador a entero con direccion del arreglo al que solo se le quiere asignar valores pares.
    \param tam Entero con valor del tamaño del arreglo.
    \param cont Entero con valor del numero de numeros pares en el arreglo completo.
*/
void numPares(int* random, int* pares, int tam, int cont){
    int j=0, i=0;
    for(i=0; i<tam; i++)
        if(!(random[i]%2)){
            pares[j] = random[i];
            j++;
        }

    imprimeArreglo(cont, pares, "pares");

}

/**
    \brief Función que suma todos los elementos de un arreglo.
    \param array Apuntador a entero con dereccion del arreglo.
    \param tam Entero con valor del tamaño del arreglo.
    \return suma Entero con el valor de la suma de los elementos.
*/
int sumaElementos(int* array, int tam){
    int suma=0, i;
    for(i=0; i<tam; i++)
        suma+=array[i];
    return suma;
}