function [clases_p] = k_means(z, k, c)
    [num_muestras, comp]= size(z);
    clases = repmat(99, [num_muestras, comp, k]);
    clases_p = repmat(99, [num_muestras, 2, k]);
    centroides = zeros(k, comp);
    cent_aux = zeros(1, k);
    contadores = repmat(1, [1, k]);
    %centroides = zeros(1,k);
    
    for i=1:k
       clases(1,:,i) = z(i,:);  
       clases_p(1,:,i) = c(i,:);  
       centroides(i,:) = z(i,:);   
    end
    
    clases;
    clases_p;
    centroides;
    
    for i=k+1:num_muestras
        vector = z(i,:);
        cord = c(i,:);
        for j=1:k
            %media = mean(clases(:,:,j),'omitnan');
            %centroides(:,k) = norm(vector-media);
            cent_aux(:,j) = norm(vector -  centroides(j, :));
        end
        cent_aux;
        dist_minima = min(min(cent_aux));
        indice = find(cent_aux == dist_minima);
        contadores(:, indice(1)) = contadores(:, indice(1)) + 1;
        clases(contadores(:, indice(1)),:,indice(1)) = vector;
        clases_p(contadores(:, indice(1)),:,indice(1)) = cord;
        centroides(indice(1),:) = (vector +  centroides(indice(1), :)) / 2;
    end
    
    clases;
    clases_p;
    centroides;
    
end