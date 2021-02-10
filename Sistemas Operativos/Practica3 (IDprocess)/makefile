CFLAGS = -c

progra1.o: Src/Progra1.c
	$(CC)  $(CFLAGS) Src/Progra1.c -o Lib/Progra1.o
	
progra1: progra1.o Lib/Progra1.o
	$(CC) Lib/Progra1.o -o Bin/Progra1
	
runProgra1:
	Bin/Progra1
	
progra2.o: Src/Progra2.c Src/tiempo.c Include/tiempo.h
	$(CC)  $(CFLAGS) Src/Progra2.c -o Lib/Progra2.o
	$(CC)  $(CFLAGS) Src/tiempo.c -o Lib/tiempo.o

progra2: progra2.o Lib/Progra2.o
	$(CC) Lib/Progra2.o Lib/tiempo.o -o Bin/Progra2
	
runProgra2:
	Bin/Progra2
	
progra3.o: Src/Progra3.c Src/tiempo.c Include/tiempo.h
	$(CC)  $(CFLAGS) Src/Progra3.c -o Lib/Progra3.o
	$(CC)  $(CFLAGS) Src/tiempo.c -o Lib/tiempo.o

progra3: progra3.o Lib/Progra3.o
	$(CC) Lib/Progra3.o Lib/tiempo.o -o Bin/Progra3
	
runProgra3:
	Bin/Progra3

clean:
	-rm -f Bin/*
	-rm -f Lib/*