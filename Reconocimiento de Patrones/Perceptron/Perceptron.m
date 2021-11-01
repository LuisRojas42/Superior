clear all;              %borra el espacio de trabajo
clc;                    %borra la ventana de comandos
close all               %cierra todo
warning off all         % apaga los warnings

salir = 1;
while(salir == 1)
    opcion=input('Selecciona operación: \n\ 1:Compuerta AND \n\ 2:Cubo\n')       

    if opcion == 1
        AND()
    elseif opcion == 2
        CUBO()
    end
    
    
    salir = input('Deseas continuar? \n\ 1:Continuar \n\ 2:Salir ')
end