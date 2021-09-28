function [] = AND(c1, c2, c3, Wo)

    % *** Copuertas OR y AND ***
    fprintf('\n*** Ingrese las clases en forma de vectores ***') 
    %c1 = [0; 0];
    %c2 = [0 1 1; 1 0 1];
    %c1 = [0 0 1; 0 1 0];
    %c2 = [1; 1];    
    c1 = input('\n\ Clase 1:\n')
    c2 = input('\n\ Clase 2:\ ')    
    x=[c1'; c2'];    
    
    fprintf('\n*** Ingrese el bias y los targets en forma de vectores ***') 
    %b=[1; 1; 1; 1];
    %t=[0; 0; 0; 1];        
    b = input('\n\ Bias:\ ')
    t = input('\n\ Targets:\ ')       

    fprintf('\n*** Ingrese los pesos en forma de vector y el factor de aprendizaje ***')     
    %Wo=[1 1 1]
    %r = 1       
    Wo = input('\n\ Pesos W:\ ')
    r = input('\n\ Factor:\ ')
    
    % Ingresa el número de iteraciones que deseamos
    fprintf('\n*** Ingrese el número máximo de iteraciones ***')     
    %iter=10
    iter = input('\n\ Iteraciones:\n')    
    
    fprintf('*** Entradas ***') 
    P=[x b]
    % ***************

    % Comenzamos el entrenamiento
       for epocas=1:iter        %repetir 10 veces el codigo
           ep=0;                       %almacena el numero de errores que comete
           fprintf('\n\nIteración número %d', epocas) 
           for i=1:length(P)    %repetir 1 hasta 4        
               row = P(i,:);
               w = Wo';
               fsal = row * w  %genera la respuesta
               clase = t(i,:);
               if clase == 0 && fsal >= 0
                   Wo = Wo - r * P(i,:)
                   ep = ep + 1;
               elseif clase == 1 && fsal <= 0
                   Wo = Wo + r * P(i,:)
                   ep = ep + 1;
               end
           end
           fprintf('Número de errores: %d', ep) 
           if ep==0
               break;        
           end
       end   

    fprintf('\n')     
    Wo

    figure(1)
    grid on
    hold on

    plot(c1(1,:),c1(2,:),'ro','MarkerSize',10,'MarkerFaceColor','r')
    plot(c2(1,:),c2(2,:),'bo','MarkerSize',10,'MarkerFaceColor','b')
    
    syms x1 x2
    eq1 = Wo(1)*x1 + Wo(3);
    eq2 = Wo(2)*x2 + Wo(3);
    x1 = solve(eq1)
    x2 = solve(eq2)
    x = linspace(0, x1);
    y = linspace(x2, 0);
    plot(x,y, 'k-','LineWidth',4);

    xlabel('Clase 1');
    ylabel('Clase 2');
    title('Perceptrón con un plano de separabilidad lineal de dos clases')

end
