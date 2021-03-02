a.out: main.o lex.yy.o sintáctico.tab.o tabla_simbolos.o
	gcc main.o lex.yy.o sintáctico.tab.o tabla_simbolos.o -lm -ll

main.o: main.c sintáctico.tab.c
	gcc -c main.c

tabla_simbolos.o: tabla_simbolos.c
	gcc -c tabla_simbolos.c

lex.yy.o: lex.yy.c
	gcc -c lex.yy.c

sintáctico.tab.o: sintáctico.tab.c
	gcc -c sintáctico.tab.c

lex.yy.c: léxico.l sintáctico.tab.c
	flex léxico.l

sintáctico.tab.c: sintáctico.y
	bison -d sintáctico.y

clean:
	rm -f a.out main.o sintáctico.tab.* lex.yy.* tabla_simbolos.o

run: a.out
	./a.out
