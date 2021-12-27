clc
clear all
close all
warning off all

IMAG='BasesSossa/IMAG';
TIPO = '.BMP';
cont = 1;
fila = 1;
props = zeros(1, 5);

for i=1:120
    
    if cont <= 9
        numero_img = strcat('00',int2str(cont));
    elseif cont <= 99
        numero_img = strcat('0',int2str(cont));
    else
        numero_img = strcat('',int2str(cont));
    end
    
    ruta = strcat(IMAG,numero_img,TIPO);
    
    if isfile(ruta)
        a=imread(ruta);
        c=im2bw(a);
        
        objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox', 'EulerNumber');
    
        for k=1:length(objetos)
            caja=objetos(k).BoundingBox;

            props(fila,1) = objetos(k).Perimeter;
            props(fila,2) = objetos(k).Area;
            props(fila,3) = objetos(k).EulerNumber;
            props(fila,4) = cont;
            props(fila,5) = k;
            %props(i,3) = objetos(k).Centroid;
            %props(i,4) = objetos(k).BoundingBox;        

            %if i > 1 and (props(i, 1)-props(i-1, 1) <  )

            %end
            fila = fila + 1;
        end
        
    end
               
    cont = cont + 1;
end

puntos = props(:, [1,3]);

k = 6;
clases = k_means(puntos, k, props);
clase_1 = zeros(1, 5);
clase_2 = zeros(1, 5);
clase_3 = zeros(1, 5);
clase_4 = zeros(1, 5);
clase_5 = zeros(1, 5);
clase_6 = zeros(1, 5);

for i=1:k
   clase_aux = clases(:,:,i);
   
   [num_muestras, comp]= size(clase_aux);
   for j=1:num_muestras         
   
       if clase_aux(j,:) == [99 99 99 99 99]
           break
       else
            switch i
                case 1
                    clase_1(j,:) = clase_aux(j,:); %Tornillo
                case 2
                    clase_2(j,:) = clase_aux(j,:); %Rondana
                case 3
                    clase_3(j,:) = clase_aux(j,:); %Armella
                case 4
                    clase_4(j,:) = clase_aux(j,:); %Llave Alen
                case 5
                    clase_5(j,:) = clase_aux(j,:); %Cola de pato
                case 6
                    clase_6(j,:) = clase_aux(j,:); %Otros
                    %RowIdx = find(ismember(puntos, clase_aux(j,:),'rows'))
            end
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

objetos=regionprops(c,'Perimeter','Area','Centroid','BoundingBox', 'EulerNumber');
punto = zeros(1, 3);

Colas = 0;
Rondanas = 0;
Llaves = 0;
Tornillos = 0;
Armellas = 0;
Otros = 0;

for k=1:length(objetos)
    
    caja=objetos(k).BoundingBox;        
    rectangle('Position',[caja(1),caja(2),caja(3),caja(4)],'EdgeColor','r','LIneWidth',2);    
        
    punto(1,1) = objetos(k).Perimeter;
    punto(1,2) = objetos(k).Area;
    punto(1,3) = objetos(k).EulerNumber;
    
    clase = dist_media(clase_1(:, [1,2,3]), clase_2(:, [1,2,3]), clase_3(:, [1,2,3]), clase_4(:, [1,2,3]), clase_5(:, [1,2,3]), clase_6(:, [1,2,3]), punto)
    %clase = knn(clase_1(:, [1,2,3]), clase_2(:, [1,2,3]), clase_3(:, [1,2,3]), clase_4(:, [1,2,3]), clase_5(:, [1,2,3]), clase_6(:, [1,2,3]), punto)    
       
    switch clase
        case 1
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Cola de pato','Color','g'); %Cola de pato
            Colas = Colas + 1
        case 2
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Rondana','Color','g'); %Rondana
            Rondanas = Rondanas + 1
        case 3
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Llave Alen','Color','g'); %Llave Alen
            Llaves = Llaves + 1
        case 4
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Tornillo','Color','g'); %Tornillo
            Tornillos = Tornillos + 1
        case 5
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Armella','Color','g'); %Armella
            Armellas = Armellas + 1
        case 6
            text(objetos(k).Centroid(1),objetos(k).Centroid(2),'Otros','Color','g');
            Otros = Otros + 1
    end   
    
end

fprintf("Total de Colas de Patos: %d\n", Colas)
fprintf("Total de Rondana: %d\n", Rondanas)
fprintf("Total de Llave Alen: %d\n", Llaves)
fprintf("Total de Tornillo: %d\n", Tornillos)
fprintf("Total de Armella: %d\n", Armellas)
fprintf("Total de Otros: %d\n", Otros)

fprintf("Total: %d\n", Colas + Rondanas + Llaves + Tornillos + Armellas + Otros)
