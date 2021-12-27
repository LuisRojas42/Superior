clc
clear all
close all
warning off all

% PROGRAMA PARA IDENTIFICAR Y RECONOCER OBJETOS GEOMÉTRICOS DENTRO DE UNA
% IMAGEN BINARIA

figure(1)
char name;
[name,pathname]=uigetfile('*.BMP');
nombre=sprintf('%s%s',pathname,name);
a=imread(nombre);
imshow(a)
figure(2)
c=im2bw(a);
imshow(c)

%analizando las propiedades geométricas de las imágenes de la figura
objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox', 'Circularity');
cuadrados = 0;
triangulos = 0;
circulos = 0;


for k=1:length(objetos)
    caja=objetos(k).BoundingBox;
    
    if(objetos(k).Area>10000)
        rectangle('Position',[caja(1),caja(2),caja(3),caja(4)],'EdgeColor','b','LIneWidth',2);
    else
        rectangle('Position',[caja(1),caja(2),caja(3),caja(4)],'EdgeColor','r','LIneWidth',2);
    end
    
    
    if(objetos(k).Perimeter^2/objetos(k).Area>18)
        text(objetos(k).Centroid(1),objetos(k).Centroid(2),'TRIANGULO','Color','r');
        triangulos = triangulos + 1;
        
    elseif(objetos(k).Perimeter^2/objetos(k).Area<14.3)
        text(objetos(k).Centroid(1),objetos(k).Centroid(2),'CIRCULO','Color','g');
        circulos = circulos + 1;
    else
        text(objetos(k).Centroid(1),objetos(k).Centroid(2),'CUADRADO','Color','g');
        cuadrados = cuadrados + 1;
    end           
    
end

fprintf('Cuadrados encontrados: %d\n\n',cuadrados) 
fprintf('Circulos encontrados: %d\n\n',circulos) 
fprintf('Triangulos encontrados: %d\n\n',triangulos) 
fprintf('Total encontrados: %d\n\n',triangulos+circulos+cuadrados) 

disp('fin de proceso...')