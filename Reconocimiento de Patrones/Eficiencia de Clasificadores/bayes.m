function [valor] = bayes(clases, vector)
    %fprintf('***** Bayes *****\n');
    [num_dimen, num_reptes, num_clases] = size(clases);
    probabilidades = zeros(1, num_clases);
    probabilidades_n = zeros(1, num_clases);
    
    for i = 1:num_clases
        clase = clases(:,:,i);
        
        media=mean(clase, 2);      
        dato1_x = clase(1,:) - media(1,:);
        dato1_y = clase(2,:) - media(2,:);
        dato1 = [dato1_x; dato1_y];
        dato2 = dato1';
        varianza = (1/num_reptes) * dato1 * dato2;
        
        dato1 = ((2*pi)^(-num_dimen/2)) * det(varianza)^(-0.5);
        
        h = vector - media;
        hp = h';        
        varianza_inv = inv(varianza);
        dato2 = exp(-0.5 * hp * varianza_inv * h);

        probabilidad = dato1 * dato2;
        probabilidades(:,i) = probabilidad;
    end
    
    for i = 1:num_clases        
       probabilidad_n = probabilidades(:,i) * 100 / sum(probabilidades);
       probabilidades_n(:,i) = probabilidad_n;
    end    
    probabilidades_n;
    prob_maxima = max(max(probabilidades_n));
    if prob_maxima < 10 || isnan(prob_maxima)
        valor = -1
    else
        valor = find(probabilidades_n==prob_maxima);
    end
end