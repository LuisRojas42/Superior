mov ax, 0x07C0 ;Funcion de cargar caracteres
mov ds, ax
;mos si, msg

cld ;pone en cero el bit correspondiente a la bandera de dirección. 

escribe_c: 

	lodsb ;toma la cadena que se encuentre en la dirección especificada por SI, 
		  ;la carga al registro AL (o AX) y suma o resta 1 (segun el estado de DF)
		  ;a SI si la transferencia es de bytes o 2 si la transferencia es de palabras.
	or al, al
	jz boot_strap
	mov ah, 0x0E

	mov bh, 0 
	int 0x10
jmp escribe_c

boot_strap:
	jmp boot_strap
	msg db "Mi emnsage0", 13, 10, 0

	times 510-($-$$) db 0

db 0x55
db 0xAA 
