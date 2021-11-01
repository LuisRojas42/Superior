clc
clear all
close all
warning off all
%Programa que convierte las coord espaciales del plano cartesiano a las coord de una imagen

h=imread('Railay.jpg');
figure(1)
[m,n]=size(h);
imshow(h)

figure(2)
dato= imref2d(size(h))
%convierte coordenadas del plano a los de imagen

imshow(h,dato) 

%al convertir es necesario especificar las coord
% de la imagen original, a las coord a desplegar

figure(3)

impixel(h)

c1x=randi([0,3550],2,100);
c1y=randi([2400,2650],2,100);

c2x=randi([0,3550],2,100);
c2y=randi([1700,2400],2,100);

c3x=randi([0,3550],2,100);
c3y=randi([0,650],2,100);

%Graficando sobre el plao de la imagen coord pixelares

z1=impixel(h,c1x(1,:),c1y(2,:));
z2=impixel(h,c2x(1,:),c2y(2,:));
z3=impixel(h,c3x(1,:),c3y(2,:));

grid on
hold on

plot(c1x(1,:),c1y(2,:),'ob','MarkerSize',10)
plot(c2x(1,:),c2y(2,:),'or','MarkerSize',10)
plot(c3x(1,:),c3y(2,:),'or','MarkerSize',10)

%media1=mean(z1,'omitnan');
%media2=mean(z2,'omitnan');
%media3=mean(z3,'omitnan');

%dist1= norm(punto, media1)

%px=input('dame coord del vector en x= ')
%py=input('dame coord del vector en y= ')

%punto=[px,py];

%P1=impixel(h,punto(1,:),punto(2,:));

%disp('fin de proceso')


%whos (en la terminal de matlab) describe imagen cargada

%h(1:5,2:5) leer imagen desde la fila 1 a la 5 y columnas de la 2: a la 5