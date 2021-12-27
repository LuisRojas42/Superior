function [clases_p] = k_means(z, k, c)
    [num_muestras, comp]= size(z);
    clases = repmat(99, [num_muestras, comp, k]);
    clases_p = repmat(99, [num_muestras, 5, k]);
    centroides = zeros(k, comp);
    cent_aux = zeros(1, k);
    contadores = repmat(1, [1, k]);
    centroides_ante = zeros(k, comp);
    %centroides = zeros(1,k);
    
    %
    for i=1:k
       clases(1,:,i) = z(i,:);  
       clases_p(1,:,i) = c(i,:);  
       centroides(i,:) = z(i,:);   
    end
    
    %{
    clases(1,:,1) = z(1,:);  
    clases_p(1,:,1) = c(1,:);  
    centroides(1,:) = z(1,:);
    
    clases(1,:,2) = z(3,:);  
    clases_p(1,:,2) = c(3,:);  
    centroides(1,:) = z(3,:);
    
    clases(1,:,3) = z(5,:);  
    clases_p(1,:,3) = c(5,:);  
    centroides(1,:) = z(5,:);
    
    clases(1,:,4) = z(7,:);  
    clases_p(1,:,4) = c(7,:);  
    centroides(1,:) = z(7,:);
    
    clases(1,:,5) = z(13,:);  
    clases_p(1,:,5) = c(13,:);  
    centroides(1,:) = z(13,:);   
    
    clases(1,:,6) = z(15,:);  
    clases_p(1,:,6) = c(15,:);  
    centroides(1,:) = z(15,:);   
    %}
    
    clases;
    clases_p;
    centroides;
    
    ciclo = 1;
    while ciclo > 0
        %fprintf("Iteración %d\n", ciclo);
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
        if centroides_ante == centroides
            ciclo = 0;
        else
            centroides;
            centroides_ante = centroides;
            ciclo = ciclo + 1;
            contadores = repmat(1, [1, k]);
        end
        
    end
    
    clases;
    clases_p;
    centroides;
    
end