%% Práctica 2: Red de Hamming
clear all; clc;

%{
/******************/
    2 Clases
/*****************/
%}

p1=[0; 0;]
p2=[0; 1;]
p3=[1; 0;]
p4=[1; 1;]
P=[p1 p2 p3 p4]

t1=0
t2=0
t3=0
t4=1
t=[t1 t2 t3 t4]

w=[0 0]
b=0


%{
/******************/
    4 Clases
/*****************/
%}
%{
p1=[1; 1];
p2=[1; 2];
p3=[2; -1];
p4=[2; 0];
p5=[-1; 2];
p6=[-2; 1];
p7=[-1; -1];
p8=[-2; -2];
P=[p1 p2 p3 p4 p5 p6 p7 p8]

t1=[0; 0];
t2=[0; 0];
t3=[0; 1];
t4=[0; 1];
t5=[1; 0];
t6=[1; 0];
t7=[1; 1];
t8=[1; 1];
t=[t1 t2 t3 t4 t5 t6 t7 t8]

w=[-1 1; 2 -3]
b=[-1;2]
%}

%{
/******************/
   8 Clases
/*****************/
%}
%{
p1=[1; 1];
p2=[1; 2];
p3=[2; -1];
p4=[2; 0];
p5=[-1; 2];
p6=[-2; 1];
p7=[-1; -1];
p8=[-2; -2];
P=[p1 p2 p3 p4 p5 p6 p7 p8]

t1=[0; 0; 0];
t2=[0; 0; 0];
t3=[0; 1; 0];
t4=[0; 1; 0];
t5=[1; 0; 0];
t6=[1; 0; 1];
t7=[1; 1; 1];
t8=[1; 1; 1];
t=[t1 t2 t3 t4 t5 t6 t7 t8]

w=[-1 1; 2 -3; 2 1]
b=[-1;2;1]
%}

[m n] = size(P); 
maxEpocas=20; %Número máximo de épocas

%Algortimo de perceptron
for epoca=1:maxEpocas
    ep=0; %error acumulado por época 
    for i=1:n
        a = w*P(:,i)+b;
        for j=1:length(a) %función Hardlim
            if a(j) >= 0
                a(j)=1;
            else
                a(j)=0;
            end
        end
        e=t(:,i)-a; %error
        if nnz(e) ~= 0
            w=w+e*P(:,i)'; %regas de aprendizaje
            b=b+e;
            ep=ep+1;
        end
    end
    if ep==0 %si termina en cero finaliza entrenamiento
        break;        
    end
end 

%Graficar puntos del dataset
for i=1:n
    hold on; 
    punto = sprintf('p%d',i);
    text(P(1,i)+0.1,P(2,i),punto);
    plot(P(1,i), P(2,i), 'og', 'MarkerFaceColor', 'b'); 
end

axis([-3 3 -3 3]);

%Graficar fornteras de decisión
[m n] = size(w);
x=1:2;
for i=1:m
   for j=1:n
       if w(i,j)~= 0
           x(j) = -b(i)/w(i,j);
       else
           x(j)=0
       end
   end
   a = linspace(-10, 10, 100);
   y = (-x(2)/x(1))*a+x(2);
   ftra = sprintf('frontera %d',i);
   text(0.1,x(2),ftra);
   plot(a,y)
end

%Agregar origenes a la gráfica
ax = gca;
ax.XAxisLocation = 'origin';
ax.YAxisLocation = 'origin';
hold off; 

x = sprintf('Pesos y bias finales:');
disp(x);
b 
w


