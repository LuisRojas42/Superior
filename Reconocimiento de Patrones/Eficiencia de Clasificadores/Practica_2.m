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
    dispersion=input('¿Qué factor de dispersión deseas?\n');    
    vector_aux=(randn(2,num_reptes)*dispersion) + centroide;
    clases(:,:,i) = vector_aux;
end

clases;
loop = 1;

figure(1)
grid on
hold on
for i = 1:num_clases        
    plot(clases(1,:,i),clases(2,:,i),'ro','MarkerSize',10,'MarkerFaceColor',rand(1,3))
    lgd{i} = strcat('Clase ',num2str(i)) ;
end
xlabel('atributo1');
ylabel('atributo2');
title('GRAFICANDO %d CLASES DE DATOS', num_clases)
legend(lgd)

vector_clases = [1:1:num_clases+1];
for l = 1:num_clases
    arrow{l} = string(strcat('C', string(l)));
end
arrow{num_clases+1} = 'AVG';
arrow;

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

for i = 1:4
    figure(i+1)
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



