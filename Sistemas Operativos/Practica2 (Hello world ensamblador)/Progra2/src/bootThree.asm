Mov ax, 0x07C0
Mov ds, ax

cld

push ds 	 ;Asegurar que DS=ES
pop es				 

;INT 10h AX=1100h - Cambiar fuente de vídeo (Modo Texto)

mov ax,1100h	;Funcion de cargar caracteres
mov bp,caract1	;Tabla de caracteres
mov cx,1 	 ;Cargar 1 carácter
mov dx,61	 ;Cambiar el carácter 61
mov bh,14	 ;14 bytes por carácter
xor bl,bl	 ;Bloque 0
int 10h 	 ;Llamamos a la INT 10h
mov ah,0Eh 	 ;Funcion teletype
mov al,61 	 ;Mostrar el carácter cambiado
int 10h 	 ;Llamamos a la INT 10h


mov ax,1100h	 ;Funcion de cargar caracteres
mov bp,caract2	 ;Tabla de caracteres
mov cx,1	 ;Cargar 1 carácter
mov dx,62	 ;Cambiar el carácter 61
mov bh,14	 ;14 bytes por carácter
xor bl,bl	 ;Bloque 0
int 10h 	 ;Llamamos a la INT 10h
mov ah,0Eh 	 ;Funcion teletype
mov al,62 	 ;Mostrar el carácter cambiado
int 10h 	 ;Llamamos a la INT 10h


mov ax,1100h	 ;Funcion de cargar caracteres
mov bp,caract3	 ;Tabla de caracteres
mov cx,1 	 ;Cargar 1 carácter
mov dx,63	 ;Cambiar el carácter 61
mov bh,14	 ;14 bytes por carácter
xor bl,bl	 ;Bloque 0
int 10h 	 ;Llamamos a la INT 10h
mov ah,0Eh 	 ;Funcion teletype
mov al,63 	 ;Mostrar el carácter cambiado
int 10h 	 ;Llamamos a la INT 10h


mov ax,1100h	 ;Funcion de cargar caracteres
mov bp,caract4	 ;Tabla de caracteres
mov cx,1 	 ;Cargar 1 carácter
mov dx,64	 ;Cambiar el carácter 61
mov bh,14	 ;14 bytes por carácter
xor bl,bl	 ;Bloque 0
int 10h 	 ;Llamamos a la INT 10h
mov ah,0Eh 	 ;Funcion teletype
mov al,64 	 ;Mostrar el carácter cambiado
int 10h 	 ;Llamamos a la INT 10h



caract1: 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
	db	11111111b
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 


caract2: 
	db	11111111b
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
        db	11000011b 
	db	11111111b


caract3: 
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11000000b
	db	11111111b


caract4:

        db	11111111b 
	db	11111111b
	db	11000011b
	db	11000011b
	db	11000011b
	db	11111111b
	db	11111111b
	db	11000011b
	db	11000011b
	db	11000011b
	db	11000011b
	db	11000011b
	db	11000011b
	db	11000011b




times 510-($-$$) db 0
	db 0x55
	db 0xAA

