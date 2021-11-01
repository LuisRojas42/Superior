function [] = CUBO(c1, c2, c3, Wo)

    % *** Cubo 3D ***
    %fprintf('\n*** Ingrese las clases en forma de vectores ***') 
    c1_c = [1 0 1 1; 0 0 0 1; 1 0 0 0]
    c2_c = [0 0 1 0; 0 1 1 1; 1 1 1 0]    
    %c1 = input('\n\ Clase 1:\ ')
    %c2 = input('\n\ Clase 2:\ ')    
    x = [c1_c'; c2_c']
    
    %fprintf('\n*** Ingrese el bias y los targets en forma de vectores ***') 
    b = [1; 1; 1; 1; 1; 1; 1; 1]
    t = [0; 0; 0; 0; 1; 1; 1; 1]    
    %b = input('\n\ Bias:\ ')
    %t = input('\n\ Targets:\ ')   

    %fprintf('\n*** Ingrese los pesos en forma de vector y el factor de aprendizaje ***')     
    Wo = [1 1 1 1]
    r = 1
    %Wo = input('\n\ Pesos W:\ ')
    %r = input('\n\ Factor:\ ')
    
    % Ingresa el número de iteraciones que deseamos
    %fprintf('\n*** Ingrese el número máximo de iteraciones ***')     
    iter=10
    %iter = input('\n\ Iteraciones:\n')
    
    fprintf('*** Entradas ***') 
    P=[x b]
    % ***************    

    % Comenzamos el entrenamiento
       for epocas=1:iter        %repetir 10 veces el codigo
           ep=0;                       %almacena el numero de errores que comete
           fprintf('\n\nIteración número %d', epocas) 
           for i=1:length(P)    %repetir 1 hasta 8        
               clase = t(i,:);
               row = P(i,:);
               w = Wo';           
               fsal = row * w;  %genera la respuesta           
               if clase == 0 && fsal >= 0
                   Wo = Wo - r * P(i,:);
                   ep = ep + 1;
               elseif clase == 1 && fsal <= 0
                   Wo = Wo + r * P(i,:);
                   ep = ep + 1;
               end
           end
           fprintf('\nNúmero de errores: %d', ep) 
           if ep==0
               break;        
           end
       end   
       
    fprintf('\n')     
    %Wo
    
    figure(1)
    grid on
    hold on

    plot3(c1_c(1,:),c1_c(2,:),c1_c(3,:),'ro','MarkerSize',10,'MarkerFaceColor','r')
    plot3(c2_c(1,:),c2_c(2,:),c2_c(3,:),'bo','MarkerSize',10,'MarkerFaceColor','b')    
    
    syms x1 x2 x3 
    [x, y] = meshgrid(-0.2:0.05:1.2);
    z = (-Wo(1)*x - Wo(2)*y - Wo(4))/Wo(3);
    mesh(x, y, z)
    
    xlabel('Clase 1');
    ylabel('Clase 2');
    title('Perceptrón con un plano de separabilidad lineal de dos clases')

end