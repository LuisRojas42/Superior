function [valor] = knn(clases, vector, k)
    fprintf('***** KNN *****\n') 
    [num_dimen, num_reptes, num_clases]= size(clases);
    Distancias = zeros(num_clases,num_reptes);
    
    for i = 1:num_clases
        distancias_clase = vecnorm(vector-clases(:,:,i));
        Distancias(i,:) = distancias_clase;
    end
             
    valores = zeros(k,3);
    
    for i=1:k
        [minimos, clases] = min(Distancias);
        minimo = min(minimos);
        clase = clases(find(minimos == minimo));
        % remove for the next iteration the last smallest value:
        Distancias(Distancias == minimo) = [9999];
        valores(i,:) = [i, minimo, clase];
    end
    
    valores
    clases_nn = valores(:,3)
    clase_nn = mode(clases_nn)
    valor = clase_nn
    
end