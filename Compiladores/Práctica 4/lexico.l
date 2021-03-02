%{
  /* Definiciones */
  /*Código C*/
  #include <stdio.h>
%}
D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS		(f|F|l|L)
IS		(u|U|l|L)*
%%
"/*"		  	{ printf("<Salto de linea>\n"); }

"auto"			{ printf("<Especificador de categoria>\n"); }
"break"			{ printf("<Terminar ciclo>\n"); }
"case"			{ printf("<Especificador de caso>\n"); }
"char"			{ printf("<Tipo de dato>\n"); }
"const"			{ printf("<Calificador de constante>\n"); }
"continue"	{ printf("<Pasa iteración en ciclo>\n"); }
"default"		{ printf("<Definir por defecto>\n"); }
"do"			  { printf("<Ciclo>\n"); }
"double"		{ printf("<Tipo de dato>\n"); }
"else"			{ printf("<Condicion en falso>\n"); }
"enum"			{ printf("<Expresión de indexacción>\n"); }
"extern"		{ printf("<Clase de almacenamiento>\n"); }
"float"			{ printf("<Tipo de dato>\n"); }
"for"			  { printf("<Ciclo>\n"); }
"goto"			{ printf("<Instrucción de salto>\n"); }
"if"			  { printf("<Condicion>\n"); }
"int"			  { printf("<Tipo de dato>\n"); }
"long"			{ printf("<Tipo de dato>\n"); }
"register"	{ printf("<Tipo de dato>\n"); }
"return"		{ printf("<Función de retorno>\n"); }
"short"			{ printf("<Tipo de dato>\n"); }
"signed"		{ printf("<Especificador>\n"); }
"sizeof"		{ printf("<Función para tamaño>\n"); }
"static"		{ printf("<Declaración>\n"); }
"struct"		{ printf("<Tipo de dato>\n"); }
"switch"		{ printf("<Condicional>\n"); }
"typedef"		{ printf("<Función para definir tipo de dato>\n"); }
"union"			{ printf("<Función para unir>\n"); }
"unsigned"	{ printf("<Especificador>\n"); }
"void"			{ printf("<Tipo de dato>\n"); }
"volatile"	{ printf("<Palabra reservada>\n"); }
"while"			{ printf("<Ciclo>\n"); }

{L}({L}|{D})*   { printf("Tipo de dato\n"); }

0[xX]{H}+{IS}?		{ printf("Constante hexadecimal\n"); }
0{D}+{IS}?		    { printf("Constantes decimal \n"); }
{D}+{IS}?	    	  { printf("Constante decimal\n"); }
L?'(\\.|[^\\'])+'	{ printf("Constante\n"); }

{D}+{E}{FS}?		        { printf("Constantes notación científica\n"); }
{D}*"."{D}+({E})?{FS}?  { printf("Constantes notación científica\n"); }
{D}+"."{D}*({E})?{FS}?  { printf("Constantes notación científica\n"); }

L?\"(\\.|[^\\"])*\" { printf("Cadenas\n"); }

"..."			    { printf("<Operador>\n"); }
">>="			    { printf("<Asignación con desplazamiento a la derecha>\n"); }
"<<="			    { printf("<Asignación con desplazamiento a la izquierda>\n"); }
"+="			    { printf("<Asignación con suma>\n"); }
"-="			    { printf("<Asignación con resta>\n"); }
"*="			    { printf("<Asignación con multiplicación>\n"); }
"/="		      { printf("<Asignación con dividición>\n"); }
"%="	  	    { printf("<Asignación con modulo>\n"); }
"&="			    { printf("<Asignación con AND>\n"); }
"^="			    { printf("<Asignación con XOR>\n"); }
"|="			    { printf("<Asignación con OR>\n"); }
">>"			    { printf("<Corrimiento a la derecha>\n"); }
"<<"			    { printf("<Corrimiento a la izquierda>\n"); }
"++"			    { printf("<Incremento>\n"); }
"--"			    { printf("<Decremento>\n"); }
"->"			    { printf("<Miembro de puntero>\n"); }
"&&"			    { printf("<Condición and>\n"); }
"||"			    { printf("<Condición or>\n"); }
"<="			    { printf("<Menor igual>\n"); }
">="		      { printf("<Mayor igual>\n"); }
"=="		    	{ printf("<Igual a>\n"); }
"!="			    { printf("<Diferente de>\n"); }
";"			      { printf("<Fin de sentencia>\n"); }
("{"|"<%")		{ printf("<Operador>\n"); }
("}"|"%>")		{ printf("<Operador>\n"); }
","			      { printf("<Coma>\n"); }
":"			      { printf("<Definición>\n"); }
"="			      { printf("<Asignación>\n"); }
"("			      { printf("<Operador>\n"); }
")"			      { printf("<Operador>\n"); }
("["|"<:")		{ printf("<Operador>\n"); }
("]"|":>")		{ printf("<Operador>\n"); }
"."			      { printf("<Selección de elemento por referencia>\n"); }
"&"			      { printf("<And>\n"); }
"!"			      { printf("<Negación>\n"); }
"~"			      { printf("<Not>\n"); }
"-"			      { printf("<Resta>\n"); }
"+"			      { printf("<Suma>\n"); }
"*"			      { printf("<Multiplicación>\n"); }
"/"		     	  { printf("<División>\n"); }
"%"			      { printf("<Módulo>\n"); }
"<"			      { printf("<Menor que>\n"); }
">"			      { printf("<Mayor que>\n"); }
"^"			      { printf("<XOR>\n"); }
"|"			      { printf("<Or>\n"); }
"?"           { printf("<Condicional>\n"); }

[ \t\v\n\f]   { printf("Espacios\n"); }

.             { printf("Caracteres ignorados\n"); }
%%
