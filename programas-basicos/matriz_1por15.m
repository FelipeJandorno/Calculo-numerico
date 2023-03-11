%Exemplo: Faça um programa que crie uma matriz A 1por15 
%pedindo que o usuário insira cada um dos 15 valores.

%Criação da matriz 1 por 15
A = zeros(1,15);

%Inserindo os valores na matriz
for i = 1:15
    fprintf("\n\n--A(%i)--\n", i);
    var = input("Valor da casa: ", "s");
    A(1, i) = var;
end

%Exibe matriz
disp(A);