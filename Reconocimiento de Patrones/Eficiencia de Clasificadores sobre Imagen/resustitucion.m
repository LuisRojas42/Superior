function [presiciones] = resustitucion(clases, k)
    fprintf('***** Resustitución *****\n') 
    [num_dimen, num_reptes, num_clases] = size(clases);
    train = clases;
    test = clases;   
    
    clases;
    train;
    test;
    
    matrices_conf = zeros(num_clases, num_clases, 4);
    for i = 1:num_clases
        for j = 1:num_reptes
            clasificacion = [dist_media(train, test(:,j,i))];
            matrices_conf(i, clasificacion, 1) = matrices_conf(i, clasificacion, 1) + 1;
            clasificacion = [bayes(train, test(:,j,i))];
            matrices_conf(i, clasificacion, 2) = matrices_conf(i, clasificacion, 2) + 1;
            clasificacion = [Mahalanobis(train, test(:,j,i))];
            matrices_conf(i, clasificacion, 3) = matrices_conf(i, clasificacion, 3) + 1;
            clasificacion = [knn(train, test(:,j,i), k)];
            matrices_conf(i, clasificacion, 4) = matrices_conf(i, clasificacion, 4) + 1;
        end
    end
    
    matrices_conf;
    presiciones = zeros(num_clases, 4);          
    
    for i = 1:4        
        for j = 1:num_clases
            presiciones(j,i) = matrices_conf(j,j,i) * 100 / (num_reptes);            
        end
    end
    
    presiciones;
    M = mean(presiciones);
    presiciones = [presiciones; M];
    
end