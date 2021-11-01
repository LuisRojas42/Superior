clc
clear all
close all
warning off all
%este programa convierte las coord espaciales del plano cartesiano a las
% coord de una imagen 

h=imread('Railay.jpg');
%figure(1)
[m,n]=size(h);
%imshow(h)

figure(2)
dato=imref2d(size(h));
imshow(h,dato)

% figure(3)
% impixel(h)

c1X=randi([0,3550],2,100);
c1Y=randi([0,650],2,100);

c2X=randi([0,3550],2,100);
c2Y=randi([650,1700],2,100);

c3X=randi([0,3550],2,100);
c3Y=randi([1700,2400],2,100);

c4X=randi([0,3550],2,100);
c4Y=randi([2400,2650],2,100);

%%% GRAFICANDO SOBRE EL PLANO DE LA IMAGEN COOR PIXELARES

Z1=impixel(h,c1X(1,:),c1Y(2,:));
Z2=impixel(h,c2X(1,:),c2Y(2,:));
Z3=impixel(h,c3X(1,:),c3Y(2,:));
Z4=impixel(h,c4X(1,:),c4Y(2,:));

grid on
hold on
plot(c1X(1,:),c1Y(2,:),'ob','MarkerSize',10)
plot(c2X(1,:),c2Y(2,:),'or','MarkerSize',10)
plot(c3X(1,:),c3Y(2,:),'og','MarkerSize',10)
plot(c4X(1,:),c4Y(2,:),'oc','MarkerSize',10)
legend('clase1', 'clase2', 'clase3', 'clase4', 'punto')
title('objetos presentes en una imagen')

num_clases=4;
num_reptes=100;
clases = zeros(3, num_reptes, num_clases);

   
clases(:,:,1) = Z1';
clases(:,:,2) = Z2';
clases(:,:,3) = Z3';
clases(:,:,4) = Z4';
    
loop = 1;


    %ENTRADA DEL VECTOR DESCONOCIDO:  
    %{
    px=input('dame la coord del vector en x = ')
    py=input('dame la coord del vector en y = ')

    punto=[px;py]

    P1=impixel(h,punto(1,:),punto(2,:))
    plot(punto(1,:),punto(2,:),'oy','MarkerSize',10,'MarkerFaceColor','y')      
    
    fprintf("¿Qué clasificador deseas usar? 1:Distancia mínina, 2:Bayesiano, 3:Mahalanobis, 4:Knn 5:Todos\n");
    clasificador=input('');
    
    if clasificador == 1
        valores = [dist_media(clases, punto)];
    elseif clasificador == 2
        valores = [bayes(clases, punto, P1')];
    elseif clasificador == 3
        valores = [Mahalanobis(clases, punto, P1')];
    elseif clasificador == 4        
        k=input('dame el número de vecinos k=')
        valores = [knn(clases, punto, k, P1')];
    elseif clasificador == 5
        k=input('dame el número de vecinos k=')
        valores = [dist_media(clases, punto) bayes(clases, punto, P1') Mahalanobis(clases, punto, P1') knn(clases, punto, k, P1')];
    end
    %}
    
    %valores = [dist_media(clases, punto) bayes(clases, punto, P1') Mahalanobis(clases, punto, P1') knn(clases, punto, k, P1')];
    
    vector_clases = [1:1:num_clases+1];
    arrow = {'C1', 'C2', 'C3', 'C4', 'AVG'};
    metodos = {'Distancia mas Cercana', 'Bayes', 'Mahalanobis', 'KNN'};
    str = string(metodos);

    presiciones_rs = resustitucion(clases, 3);
    fprintf('*** Resultados del método de Resustitución: ***\n') 
    rs_table = array2table(presiciones_rs,'VariableNames', str, 'RowNames', string(arrow))
    
    presiciones_ho = holdinone(clases, 3);
    fprintf('*** Resultados del método Hold in one: ***\n') 
    ho_table = array2table(presiciones_ho,'VariableNames', str, 'RowNames', string(arrow))

    presiciones_cv = crossvalidation(clases, 3);
    fprintf('*** Resultados del método de Cross-Validation: ***\n') 
    cv_table = array2table(presiciones_cv,'VariableNames', str, 'RowNames', string(arrow))
    
    %{
    [num_filas, num_valores] = size(valores);
    if clasificador <= 4
       fprintf('el vector desconocido pertenece a la clase = %d\n\n',valores) 
    elseif clasificador == 5 
        fprintf('Por distancia media el vector desconocido pertenece a la clase = %d\n\n',valores(1, 1)) 
        fprintf('Por Bayes el vector desconocido pertenece a la clase = %d\n\n',valores(1, 2)) 
        fprintf('Por Mahalanobis el vector desconocido pertenece a la clase = %d\n\n',valores(1, 3)) 
        fprintf('Por KNN el vector desconocido pertenece a la clase = %d\n\n',valores(1, 4)) 
        clase_moda = mode([valores(1, 1) valores(1, 2) valores(1, 3) valores(1, 4)]);
        fprintf('La clase moda es = %d\n\n',clase_moda) 
    end    
    
    %loop=input('¿Deseas probar otro vector? Si=1, No=0\n')    
    %}
    %ioop = 0
    
    for i = 1:4
        figure(i+2)
        grid on
        hold on                
        plot(vector_clases, presiciones_rs(:, i), 'r-o', 'MarkerSize', 10, 'MarkerFaceColor', rand(1,3))
        plot(vector_clases, presiciones_ho(:, i), 'r-o', 'MarkerSize', 10, 'MarkerFaceColor', rand(1,3))
        plot(vector_clases, presiciones_cv(:, i), 'r-o', 'MarkerSize', 10, 'MarkerFaceColor', rand(1,3))
        %lgd{i} = strcat('Clase ', num2str(i)) ;  
        xlabel('presicion');
        ylabel('recall');
        legend('Resustitución', 'Hold in one', 'Cross-Validation')
        ylim([0, 110]);
        %str = strcat('Método ', str(:, i));
        title(metodos(i))
    end

disp('fin de proceso...')