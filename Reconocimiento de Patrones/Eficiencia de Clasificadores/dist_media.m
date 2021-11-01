function [valor] = dist_media(clases, vector)
    %fprintf('***** Distancia Media *****\n');
    [num_dimen, num_reptes, num_clases]= size(clases);
    Distancias = zeros(1,num_clases);
    for i = 1:num_clases
        media=mean(clases(:,:,i),2);
        Distancias(:,i) = norm(vector-media);
    end
    dist_minima = min(min(Distancias));
    if dist_minima > 100
        valor = -1
    else
        valor = find(Distancias == dist_minima);    
    end    
end