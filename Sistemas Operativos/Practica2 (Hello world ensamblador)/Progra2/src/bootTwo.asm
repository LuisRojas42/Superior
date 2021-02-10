Mov ax, 0x07C0
Mov ds, ax

xor ax,ax
mov ds,ax
mov es,ax

mov bx,0x8000
cli

mov ss,bx
mov sp,ax
sti

cld
clc

xor ah,ah
int 13h

mov bx,0x07E0
mov es,bx

xor bx,bx

mov ah,0x2 ;function
mov al,0x5 ;sectors to read
mov ch,0x0 ;track
mov cl,0x2 ;sector
mov dh,0x0 ;head

int 13h

jmp imprimir


imprimir:
	xor bx,bx
	mov ax,0xb890
	mov es,ax


	mov ah,0x40 ;colour is now in AH, not AL 
	mov al,'H'  ;character is now in AL, not AH

	mov WORD [es:bx], ax
	add bx,8               


	mov ah,0x40 ;colour is now in AH, not AL 
	mov al,'O'  ;character is now in AL, not AH

	mov WORD [es:bx], ax
	add bx,8               


	mov ah,0x40 ;colour is now in AH, not AL 
	mov al,'L'  ;character is now in AL, not AH

	mov WORD [es:bx], ax
	add bx,8               


	mov ah,0x40 ;colour is now in AH, not AL 
	mov al,'A'  ;character is now in AL, not AH

	mov WORD [es:bx], ax
	add bx,8               

end:
        cli
        hlt


times 510-($-$$) db 0
	db 0x55
	db 0xAA

