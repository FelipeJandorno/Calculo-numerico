%Descrição: Verifica se um número possui representação binária finita

% ===============================================================%
%Recebe o número a ser analisado
R = input("Informe o número na base decimal: ");
%Armazena o valor da casa inteira
d = ones(1, 20);
%Armazena o número no formato decimal
r = ones(1, 20);
%Contador de loops realizados
counter = 1;
% ===============================================================%

% Verifica se a casa inteira equivale a 1
for i = 1:20
    
    R = 2*R;
    r(1, i) = R;
    
    if r(1, i) < 1
        d(1, i) = 0;
    elseif r(1, i) > 1
        d(1, i) = 1;
        R = r(1, i) - 1;
    else
        break;
    end
    counter = counter + 1;
end

% Cria a matriz responsável por armazenar o resultado binário
%da parte decimal e exibe na tela
if d(1, counter) == 1 && r(1, counter) == 1
    A = zeros(1, counter);
    A(1,counter) = R;
    str = mat2str(A, counter);
    fprintf("Representação finita: 0.%s\n", str)
else 
    disp("Representação infinita");
end