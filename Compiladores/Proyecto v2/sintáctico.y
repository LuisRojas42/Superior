
%{

  #include <stdio.h>
  #include <stdlib.h>
  #include <math.h>
  #include <string.h>
  #include "tabla_simbolos.h"

  int yylex(void);
  int yyparse(void);

  /* Manejador de errores */
  void yyerror(char *mensaje) {
    printf("ERROR: %s\n", mensaje);
    exit(0);
  }

%}

%define api.value.type union
%token <double>  NUM
%token <symrec*> VAR FNCT
%token IF OP
%type  <double>  exp


%precedence '='
%left '-' '+'
%left '*' '/'
%precedence NEG
%right '^'

%%

input:
%empty
| input line
;

line:
'\n'
| exp '\n'   { printf ("%.10g\n", $1); }
| error '\n' { yyerrok;                }
| if '\n'
;

if:
IF '(' exp '=' exp')'        { printf("if detect"); }

exp:
NUM                { $$ = $1;                         }
| VAR                { $$ = $1->value.var;              }
| VAR '=' exp        { $$ = $3; $1->value.var = $3;     }
| FNCT '(' exp ')'   { $$ = (*($1->value.fnctptr))($3); }
| exp '+' exp        { $$ = $1 + $3;                    }
| exp '-' exp        { $$ = $1 - $3;                    }
| exp '*' exp        { $$ = $1 * $3;                    }
| exp '/' exp        { $$ = $1 / $3;                    }
| '-' exp  %prec NEG { $$ = -$2;                        }
| exp '^' exp        { $$ = pow ($1, $3);               }
| '(' exp ')'        { $$ = $2;                         }
;



%%
