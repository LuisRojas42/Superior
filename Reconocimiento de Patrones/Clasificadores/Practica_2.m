clc % limpia pantalla
clear all % limpia todo
close all %cierra todo
warning off all  % apaga los warnings

num_clases=input('¿Cuántas clases quieres?\n')
num_reptes=input('¿Cuántos representantes quieres por cada clase?\n')
clases = zeros(2, num_reptes, num_clases);
lgd = cell(num_clases,1);
 
for i = 1:num_clases
    fprintf('\n***Clase número %d***\n\n',i)
    fprintf("¿Dónde deseas el centroide?\n");
    centroide_x=input('x=');
    centroide_y=input('y=');
    centroide = [centroide_x;centroide_y];
    dispersion=input('¿Qué factor de dispersión deseas?\n')    
    vector_aux=(randn(2,num_reptes)*dispersion) + centroide;
    clases(:,:,i) = vector_aux;
end

clases;
loop = 1;


while loop>0
    %ENTRADA DEL VECTOR DESCONOCIDO:
    vx=input('dame coord del vector en x=')
    vy=input('dame coord del vector en y=')
    vector=[vx;vy];
 
    figure(1)
    grid on
    hold on
    for i = 1:num_clases        
        plot(clases(1,:,i),clases(2,:,i),'ro','MarkerSize',10,'MarkerFaceColor',rand(1,3))
        lgd{i} = strcat('Clase ',num2str(i)) ;
    end
    plot(vector(1,:),vector(2,:),'ko','MarkerSize',10,'MarkerFaceColor','b')
    xlabel('atributo1');
    ylabel('atributo2');
    title('GRAFICANDO %d CLASES DE DATOS', num_clases)
    legend(lgd)
    
    fprintf("¿Qué clasificador deseas usar? 1:Distancia mínina, 2:Bayesiano, 3:Mahalanobis, 4:Knn 5:Todos\n");
    clasificador=input('');
    
    if clasificador == 1
        valores = [dist_media(clases, vector)];
    elseif clasificador == 2
        valores = [bayes(clases, vector)];
    elseif clasificador == 3
        valores = [Mahalanobis(clases, vector)];
    elseif clasificador == 4        
        k=input('dame el número de vecinos k=')
        valores = [knn(clases, vector, k)];
    elseif clasificador == 5
        k=input('dame el número de vecinos k=')
        valores = [dist_media(clases, vector) bayes(clases, vector) Mahalanobis(clases, vector) knn(clases, vector, k)];
    end
    
    [num_filas, num_valores] = size(valores);
    if clasificador <= 4
       fprintf('el vector desconocido pertenece a la clase=%d\n\n',valores) 
    elseif clasificador == 5 
        fprintf('Por distancia media el vector desconocido pertenece a la clase=%d\n\n',valores(1, 1)) 
        fprintf('Por Bayes el vector desconocido pertenece a la clase=%d\n\n',valores(1, 2)) 
        fprintf('Por Mahalanobis el vector desconocido pertenece a la clase=%d\n\n',valores(1, 3)) 
        fprintf('Por KNN el vector desconocido pertenece a la clase=%d\n\n',valores(1, 4)) 
    end    
    
    loop=input('¿Deseas probar otro vector? Si=1, No=0\n')    
end
