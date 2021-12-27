function [indice] = mas_cercano(puntos, punto)
    mas_cercano =  10000;
    indice = 0;
    for i=1:length(puntos)
        h = norm(punto-puntos(i,:));
        %x1 = punto(1,1)
        %y1 = punto(1,2)
        %x2 = puntos(i,1)
        %y2 = puntos(i,2)
        %d = sqrt ((x2-x1)^2 + (y2-y1)^2);
        if h < mas_cercano & h ~= 0
            mas_cercano = h;
            indice = i;
        end
    end
end