%Realiza a coleta de dados
a = input("Insira o valor de a: ");
b = input("Insira o valor de b: ");
c = input("Insira o valor de c: ");

%Cálculo do valor de delta
delta = sqrt((b^2)-(4*a*c));

%Cálculo das raízes
x1 = (-b + delta)/(2*a);
x2 = (-b - delta)/(2*a);

%Saída de dados
fprintf("Valor de X1: %f e Valor de X2: %f\n", x1, x2);