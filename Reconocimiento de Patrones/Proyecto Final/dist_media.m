function [valor] = dist_media(clases, vector)
    %fprintf('***** Distancia Media *****\n');
    [num_clases, num_dimen]= size(clases);
    Distancias = zeros(1,num_clases);
    for i = 1:num_clases
        %media=mean(clases(i,:),2);
        Distancias(:,i) = norm(vector-clases(i,:));
    end
    dist_minima = min(min(Distancias));
    if dist_minima > 100
        valor = -1
    else
        valor = find(Distancias == dist_minima);    
    end    
end