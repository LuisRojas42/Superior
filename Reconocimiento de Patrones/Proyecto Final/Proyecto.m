clc
clear all
close all
warning off all

% ubicando el directorio donde esté la imagen o el conjunto de imágenes de
% nuestro interés

char name;
[name,pathname]=uigetfile('*.png');
nombre=sprintf('%s%s',pathname,name);
h=imread(nombre);
%figure(1)
%imshow(h)

dato=imref2d(size(h));
figure(2)
[m,n]=size(h);
imshow(h,dato)

%lanzando los puntos aleatorios sobre una imagen:

c1y=randi([1,(n/3)],1,300);
c1x=randi([1,m],1,300);
c1=[c1y;c1x];

%graficando sobre el plano de la imagen
z1=impixel(h,c1(1,:),c1(2,:));
figure(2)
grid on
hold on
plot(c1(1,:),c1(2,:),'ob','MarkerSize',10,'MarkerFaceColor','b')

z=impixel(h,c1(1,:),c1(2,:));

k = input('¿Cuántas grupos quieres?\n');
muestras = zeros(k, 3);
puntos = zeros(k,2);
[clases, clases_p] = k_means(z, k, c1');
aux = zeros(k, 3);
nom_clases = zeros(k,3);
bandera = 1;

% 154, 170, 57 pasto (1) 143.0549  176.0793   51.7744
% 175,220,246 Cielo (2) 170.9044  222.0147  243.8897 o 226.1722  231.3111
% 236.1167 o 241.9103  199.6667  137.4359
% 136,129,119 piedra (3) 118.1583   99.5667  122.7250
% 33,122,202 mar (4) 87.7674  194.4264  210.1705
% 255,251,227 arena (6) 217.3000  250.6900  251.7000
nom_cla = [143.0549  176.0793   51.7744; 170.9044  222.0147  243.8897; 118.1583   99.5667  122.7250; 87.7674  194.4264  210.1705; 217.3000  250.6900  251.7000];

for i=1:k
    for j=1:1000
        vector = clases(j,:,i);
        if isequal(vector, [99 99 99])
            clase = clases(1:j-1,:,i);  
            clase_p = clases_p(1:j-1,:,i);  
            
            nom_clases(i,:) = mean(clase(:,:),'omitnan');
            muestras(i,:) = clase(50,:);   
            puntos(i,:) = clase_p(50,:);
            punto = clase_p(50,:);
            plot(punto(:,1),punto(:,2),'ob','MarkerSize',10,'MarkerFaceColor','r')
            color = rand(1,3);
            
            while length(clase_p) > 2
                indice = mas_cercano(clase_p, punto);
                if indice ~= 0                     
                    plot(clase_p(indice,1),clase_p(indice,2),'ob','MarkerSize',10,'MarkerFaceColor',color)
                    clase_p(indice,:) = [];
                    pause(0.04)
                else
                    break
                end
            end
            
            break
        end
    end            
end

clases2 = [154 170 57; 175 220 246; 136 129 119; 33 122 202; 73 107 81; 255 251 227];

%indice = mas_cercano(c1', puntos(1,:))
%{
for i=1:k
    bandera = 1;
    while bandera == 1   
        for j=1:length(c1)
            
        end
        bandera = 0;
    end   
end
%}
if k == 3
    disp('Es una playa')    
else
    auxx = zeros(1, k);
    for i=1:k
        media = mean(clases(:,:,i),'omitnan');
        indice = mas_cercano(nom_cla, media);     
        if indice == 1
            disp('Es una Pradera')
            break
        end            
    end
    if indice ~= 1                     
        disp('Es una montaña')
    end
end    
disp('proceso terminado....')


%{
while bandera==1
    for i=1:k
        idx=randperm(length(z),1);
        muestras(i,:) = z(idx,:);   
        puntos(i,:) = c1(:,idx);
        z(idx,:) = [];
        c1(:,idx) = [];
        aux(i,:) = dist_media(nom_clases, z(idx,:));
    end
    if length(unique(aux)) == k
        bandera = 0;
    end       
end
%}
