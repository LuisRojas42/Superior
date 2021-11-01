function [avg_pred] = holdinone(clases, k)
    fprintf('***** Hold in one *****\n') 
    [num_dimen, num_reptes, num_clases] = size(clases);    
    presiciones = zeros(num_clases, 4, num_reptes);      
    
    for c = 1:num_reptes        
        train = zeros(2, num_reptes-1, num_clases);
        test = zeros(2, 1, num_clases);        
        
        for i = 1:num_clases
            %clases(:,:,i) = clases(:, randperm(num_reptes), i);
            clase_aux = clases(:,:,:);
            clase_aux(:,c,:) = [];
            train = clase_aux;
            test = clases(:,c,:);
        end                              

        clases;
        train;
        test;

        matrices_conf = zeros(num_clases, num_clases, 4);
        for i = 1:num_clases
            for j = 1:1
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

        for i = 1:4        
            for j = 1:num_clases
                presiciones(j,i,c) = matrices_conf(j,j,i) * 100 / (1);            
            end
        end

        c;
        presiciones(:,:,c);
    
    end
    %M = mean(presiciones);
    %presiciones = [presiciones; M];
    
    sum_pred = zeros(num_clases, 4);
    for i = 1:num_reptes
        sum_pred = sum_pred + presiciones(:,:,i);
    end
    avg_pred = sum_pred / num_reptes;
    M = mean(avg_pred);
    avg_pred = [avg_pred; M];
    
end