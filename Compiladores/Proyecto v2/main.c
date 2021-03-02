extern int yyparse();
#include <stdio.h>
#include <math.h>
#include <string.h>
#include "tabla_simbolos.h"
#include "sintáctico.tab.h"

symrec *sym_table;

int main(void){

  yyparse();  //Detona al analizador sintáctico

  return 0;
}
