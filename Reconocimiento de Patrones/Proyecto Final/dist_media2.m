function [valor] = dist_media2(clases, vector)
    %fprintf('***** Distancia Media *****\n') 
    [num_dimen, num_reptes, num_clases]= size(clases);
    Distancias = zeros(1,num_clases);            

    for i = 1:num_clases
        
        for j=1:1000
            vector = clases(j,:,i);
            if isequal(vector, [99 99 99])
                clase = clases(1:j-1,:,i)                          
                media=mean(clase(:,:),'omitnan');
                Distancias(:,i) = norm(vector-media);
                break
            end
        end                           
    end
    dist_minima = min(min(Distancias));
    valor = find(Distancias == dist_minima);    
end

%{

media1=mean(Z1,'omitnan');
media2=mean(Z2,'omitnan');
media3=mean(Z3,'omitnan');

dist1=norm(punto-media1);
dist2=norm(punto-media2);
dist3=norm(punto-media3);

dis_total = [dist1 dist2 dist3]
%}