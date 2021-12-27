clc
clear all
close all
warning off all

IMAG='Bases Sossa/IMAG';
TIPO = '.BMP';

Tornillos='BasesSossa/Tornillos.BMP';
Rondanas='BasesSossa/Rondanas.BMP';
Llaves='BasesSossa/Llaves.BMP';
Argollas='BasesSossa/Argollas.BMP';
Colas='BasesSossa/Colas.BMP';

props = [1, 4];
clase_1 = zeros(1, 4);
clase_2 = zeros(1, 4);
clase_3 = zeros(1, 4);
clase_4 = zeros(1, 4);
clase_5 = zeros(1, 4);
clase_6 = zeros(1, 4);

for i=1:5    
    switch i
        case 1
            a=imread(Tornillos); %Tornillo
            c=im2bw(a);
            objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox');
            for k=1:length(objetos)
                caja=objetos(k).BoundingBox;
                clase_1(k,1) = objetos(k).Perimeter;
                clase_1(k,2) = objetos(k).Area;
                clase_1(k,4) = k;
                clase_1(k,5) = i;
            end
            
        case 2
            a=imread(Rondanas); %Rondana
            c=im2bw(a);
            objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox');
            for k=1:length(objetos)
                caja=objetos(k).BoundingBox;
                clase_2(k,1) = objetos(k).Perimeter;
                clase_2(k,2) = objetos(k).Area;
                clase_2(k,4) = k;
                clase_2(k,5) = i;
            end
            
        case 3
            a=imread(Llaves); %Armella
            c=im2bw(a);
            objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox');
            for k=1:length(objetos)
                caja=objetos(k).BoundingBox;
                clase_3(k,1) = objetos(k).Perimeter;
                clase_3(k,2) = objetos(k).Area;
                clase_3(k,4) = k;
                clase_3(k,5) = i;
            end
            
        case 4
            a=imread(Argollas); %Llave Alen
            c=im2bw(a);
            objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox');
            for k=1:length(objetos)
                caja=objetos(k).BoundingBox;
                clase_4(k,1) = objetos(k).Perimeter;
                clase_4(k,2) = objetos(k).Area;
                clase_4(k,4) = k;
                clase_4(k,5) = i;
            end

        case 5
            a=imread(Colas); %Cola de pato    
            c=im2bw(a);
            objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox');
            for k=1:length(objetos)
                caja=objetos(k).BoundingBox;
                clase_5(k,1) = objetos(k).Perimeter;
                clase_5(k,2) = objetos(k).Area;
                clase_5(k,4) = k;
                clase_5(k,5) = i;
            end
    end
    
end


figure(1)
char name;
[name,pathname]=uigetfile('*.BMP');
nombre=sprintf('%s%s',pathname,name);
a=imread(nombre);
imshow(a)
figure(2)
c=im2bw(a);
imshow(c)

objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox');
punto = zeros(1, 2);

for k=1:length(objetos)
    
    caja=objetos(k).BoundingBox;        
    rectangle('Position',[caja(1),caja(2),caja(3),caja(4)],'EdgeColor','r','LIneWidth',2);    
        
    punto(1,1) = objetos(k).Perimeter;
    punto(1,2) = objetos(k).Area;
    
    clase = dist_media(clase_1(:, [1,2]), clase_2(:, [1,2]), clase_3(:, [1,2]), clase_4(:, [1,2]), clase_5(:, [1,2]), clase_6(:, [1,2]), punto)
    %clase = knn(clase_1(:, [1,2]), clase_2(:, [1,2]), clase_3(:, [1,2]), clase_4(:, [1,2]), clase_5(:, [1,2]), clase_6(:, [1,2]), punto)
       
    switch clase
        case 1
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Cola de pato','Color','g'); %Tornillos
        case 2
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Rondana','Color','g'); %Rondana
        case 3
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Llave Alen','Color','g'); %Llave
        case 4
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Tornillo','Color','g'); %Argollas
        case 5
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Armella','Color','g'); %Colas
        case 6
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Otros','Color','g');
    end   
    
end



%props