%'Exercício: Represente os seguintes números (que estão em 
%'base 10) em ponto flutuante de base binária, sendo t o 
%tamanho da mantissa, e expoente e E[emin, emax]. Use
%truncamento
x1 = 0;
x2 = 0;

for i = 1:3000 
    x1 = x1 + 0.5;
    x2 = x2 + 0.11;
end

fprintf("A: %f, B: %f\n", x1, x2)