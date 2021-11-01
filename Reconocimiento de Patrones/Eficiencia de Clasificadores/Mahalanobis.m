function [valor] = Mahalanobis(clases, vector)
    %fprintf('***** Mahalanobis *****\n') ;
    [num_dimen, num_reptes, num_clases] = size(clases);
    distancias = zeros(1, num_clases);

    for i = 1:num_clases
        clase = clases(:,:,i);
        
        media = mean(clase, 2);        
        dato_x = clase(1,:) - media(1,:);
        dato_y = clase(2,:) - media(2,:);
        dato = [dato_x; dato_y];
        dato_p = dato';
        varianza = (1/num_reptes) * dato * dato_p;
        
        vector_x = vector(1,:)-media(1,:);
        vector_y = vector(2,:)-media(2,:);
        
        distancia=[vector_x vector_y]*inv(varianza)*[vector_x;vector_y];
        distancias(:,i) = distancia;
    end
    
    distancias;
    dist_minima = min(min(distancias));
    if dist_minima > 100
        valor = -1;
    else
        valor = find(distancias==dist_minima);
    end
end