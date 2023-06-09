% Encontre o zero da função f(x) = x log(x-1) utilizando o método da Bisse
%cção com epsilon = 0,1 considerando o intervalo (2,3).

% a - limite inferior
% b - limite superior
% e - epsilon (precisão do intervalo)
%

function Bisseccao(a, b, e)

intervalo = [a b];

% Verifica se a diferença entre os limites superior e inferior do intervalo
%é menor do que a precisão estabelecida para o resultado obtido.
if (abs(func(intervalo(1)) - func(intervalo(2)))/2 < e)
    m = (intervalo(1) + intervalo(2))/2;
    fprintf("Raiz: %f\n", m);
else

    while(abs(func(intervalo(1)) - func(intervalo(2))) > e)
        m = intervalo(1) + intervalo(2);
        m = m/2;
    if( (func(m)*func(intervalo(1))) > 0)
        intervalo(2) = m;
    else
        intervalo(1) = m; 
    end

        fprintf("Valor de m: %f\n", m);
    end
end


end
