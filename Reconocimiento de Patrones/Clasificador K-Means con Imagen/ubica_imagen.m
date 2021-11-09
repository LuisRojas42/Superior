clc
clear all
close all
warning off all

% ubicando el directorio donde esté la imagen o el conjunto de imágenes de
% nuestro interés

char name;
[name,pathname]=uigetfile('*.jpg');
nombre=sprintf('%s%s',pathname,name);
h=imread(nombre);
%figure(1)
%imshow(h)

dato=imref2d(size(h));
figure(2)
[m,n]=size(h);
imshow(h,dato)

%lanzando los puntos aleatorios sobre una imagen:

c1y=randi([1,(n/3)],1,1000);
c1x=randi([1,m],1,1000);
c1=[c1y;c1x];

%graficando sobre el plano de la imagen
k = input('¿Cuántas grupos quieres?\n')
%k = 4
z=impixel(h,c1(1,:),c1(2,:));
clases = k_means(z, k, c1');
figure(2)
grid on
hold on

for i=1:k
    for j=1:1000
        vector = clases(j,:,i);
        if isequal(vector, [99 99])
            clase = clases(1:j-1,:,i);  
            
            %CALCULANDO LA MULTIRESOLUCION:
            imaR=h(:,:,1);
            fprintf('Clase: %d\n\n', i)
            [num_muestras, comp]= size(clase);
            fprintf('puntos: %d\n\n', num_muestras)            
            fprintf('Media:')
            mean(mean(clase))
            fprintf('Desviación:')
            mean(std(clase))
            
            break
        end
    end        
    plot(clase(:,1),clase(:,2),'ob','MarkerSize',10,'MarkerFaceColor',rand(1,3))
    lgd{i} = strcat('Clase ',num2str(i)) ;
end
legend(lgd)
%plot(c1(1,:),c1(2,:),'ob','MarkerSize',10,'MarkerFaceColor','b')

%CALCULANDO LA MULTIRESOLUCION:
tamVentana=10;
Num_ventanas=50;

imaR=h(:,:,1);
for j=1:k
    %fprintf('Clase: %d\n\n', j)
    for i=1: Num_ventanas
        ventanaR=imcrop(imaR,[c1y(i),c1x(i),tamVentana-1,tamVentana-1]);

        %extrayendo características a cada ventana
        R_media(i)=mean(ventanaR(:));
        R_desviacion(i)=std(double(ventanaR(:)));
        arreglo(i).ventanaR=ventanaR;
    end
    %fprintf('Media:')
    %mean(R_media)
    %fprintf('Desviación:')
    %mean(R_desviacion)
end

disp('proceso terminado....')