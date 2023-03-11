%Exemplo: Faça um programa que verifique se o número dado
%pelo usuário é positivo, se sim determinar se o mesmo é par
%ou ímpar

numero = input("Informe um número inteiro: ");

if numero > 0
    if rem(numero, 2) == 0
        fprintf("O numero %i é positivo e par.\n", numero);
    else
        fprintf("O número %i é positivo e ímpar.\n", numero);
    end
else
    fprintf("O numero %i é negativo!\n", numero);
end