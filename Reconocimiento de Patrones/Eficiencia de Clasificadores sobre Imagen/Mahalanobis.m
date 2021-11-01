function [valor] = Mahalanobis(clases, pixel)
    %fprintf('***** Mahalanobis *****\n') 
    [num_dimen, num_reptes, num_clases] = size(clases);
    distancias = zeros(1, num_clases);
    vector = find(pixel);
    for i = 1:num_clases
        clase = clases(:,:,i);
        
        media = mean(clase, 2, 'omitnan');        
        %dato_x = clase(1,:) - media(1,:);
        %dato_y = clase(2,:) - media(2,:);
        %dato = [dato_x; dato_y];
        dato = clase - media;
        dato_p = dato';
        varianza = (1/num_reptes) * dato * dato_p;
        
        %vector_x = vector(1,:)-media(1,:);
        %vector_y = vector(2,:)-media(2,:);
        vector = pixel - media;
        
        distancia=vector'*inv(varianza)*vector;
        distancias(:,i) = distancia;
    end
    
    distancias;
    dist_minima = min(min(distancias));
    valor = find(distancias==dist_minima);    
end