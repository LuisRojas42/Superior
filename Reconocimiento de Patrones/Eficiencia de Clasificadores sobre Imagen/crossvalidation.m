function [avg_pred] = crossvalidation(clases, k)
    fprintf('***** Cross-Validation *****\n') 
    [num_dimen, num_reptes, num_clases] = size(clases);
    presiciones = zeros(num_clases, 4, 20);   
    
    for c = 1:20
        train = zeros(3, num_reptes/2, num_clases);
        test = zeros(3, num_reptes/2, num_clases);            

        for i = 1:num_clases
           clases(:,:,i) = clases(:, randperm(num_reptes), i);
           train(:,:,i) = clases(:,1:num_reptes/2,i);
           test(:,:,i) = clases(:,(num_reptes/2)+1:num_reptes,i);
        end        

        clases;
        train;
        test;

        matrices_conf = zeros(num_clases, num_clases, 4);
        for i = 1:num_clases
            for j = 1:num_reptes/2
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
                presiciones(j,i,c) = matrices_conf(j,j,i) * 100 / (num_reptes/2);            
            end
        end

        presiciones(:,:,c);
    end
    
    sum_pred = zeros(num_clases, 4);
    for i = 1:20
        sum_pred = sum_pred + presiciones(:,:,i);
    end
    avg_pred = sum_pred / 20;
    M = mean(avg_pred);
    avg_pred = [avg_pred; M];
end