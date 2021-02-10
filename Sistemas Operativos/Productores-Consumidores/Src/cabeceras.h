//CABECERAS
key_t genClave();
int genIdMemoria(key_t);
int* getDireccion(int);
void liberaMemoria(int*, int);
void desasociaMemoria(int*, int);
int arraySemaforos(int);
void iniciaSemaforos(int);
void setSemUno_r(int);
void setSemUno_v(int);
void setSemDos_r(int);
void setSemDos_v(int);
void setSemTres_r(int);
void setSemTres_v(int);
void setSemCuatro_r(int);
void setSemCuatro_v(int);
void setSemCinco_r(int);
void setSemCinco_v(int);
void setSemSeis_v(int);
void setSemSeis_r(int);
void setSemSiete_v(int);
void setSemSiete_r(int);
void setSemOcho_v(int);
void setSemOcho_r(int);
void setSemNueve_v(int);
void setSemNueve_r(int);
void setSemDiez_v(int);
void setSemDiez_r(int);
void escribe(char, FILE *, FILE *, FILE *);

union semun {
    int val;
    struct semid_ds *buf;
    unsigned short  *array;
};
