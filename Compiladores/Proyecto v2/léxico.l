%{
  #include <stdlib.h>
  #include "tabla_simbolos.h"
  #include "sintáctico.tab.h"
%}

%%

[ \t]                                           {}

[0-9]+("."[0-9]+)?                              { yylval.NUM = atof( yytext );
                                                  return NUM;
                                                }

[a-zA-Z][a-zA-Z0-9]*                            {
                                                    symrec *s;
                                                    s = getsym(yytext);
                                                    if(s == 0)
                                                        s = putsym (yytext, VAR);
                                                    *((symrec**) &yylval) = s;
                                                    return s->type;
                                                }

[-|+|*|/|\n|=|(|)|^]                            { return *yytext; }

.                                               { fprintf (stderr, "ERROR:\tCaracter desconocido\n"); }

[if]                                            {
                                                    return IF;
                                                }

%%
