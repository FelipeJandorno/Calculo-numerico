% Exemplo: Faça um programa que permita calcular os valores
% para a função: f(x) = 1, se x < -1 | x², se -1 <= x <= 1 |
% -x+2, se x > 1.

% Input do valor de x
x = input("Informe o valor de x: ");

if(x < -1)
    fprintf("Resultado: %i", 1);
elseif((x >= -1) / x<= 1)
    fprintf("Resultado: %f", x^2);
else
    fprintf("Resultado: %f", -x+2);
end