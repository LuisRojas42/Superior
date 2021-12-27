function [valor] = dist_media(clase_1, clase_2, clase_3, clase_4, clase_5, clase_6, vector)
    %fprintf('***** Distancia Media *****\n');
    k=6;    
    vector
    Distancias = zeros(1,k);        
    for i = 1:k
        switch i
            case 1
                media=mean(clase_1(:,:))
            case 2
                media=mean(clase_2(:,:))
            case 3
                media=mean(clase_3(:,:))
            case 4
                media=mean(clase_4(:,:))
            case 5
                media=mean(clase_5(:,:))
            case 6
                media=mean(clase_6(:,:))
        end        
        Distancias(:,i) = norm(vector-media);
    end
    dist_minima = min(min(Distancias))
    if dist_minima > 10000
        valor = 6
    else
        valor = find(Distancias == dist_minima);    
    end    
end