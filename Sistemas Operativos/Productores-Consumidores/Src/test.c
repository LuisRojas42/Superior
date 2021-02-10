#include<stdlib.h> 
#include<unistd.h>
#include<stdio.h>

void main(){
	FILE *a, *b, *c;
    a = fopen ( "a.txt", "w" );   
    for(int i=0; i<10; i++){
    	fputc('a', a);
    	fputc('\n', a);
    }     
    fclose ( a );
}