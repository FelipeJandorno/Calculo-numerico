% Encontre o zero da função f(x) = x log(x-1) utilizando o método da Bisse
%cção com epsilon = 0,1 considerando o intervalo (2,3).

intervalo = [2 3];
epsilon = 0.1;

while((intervalo(2) - intervalo(1)) > epsilon)
    ponto_medio = (intervalo(2) - intervalo(1))/2;

    if(func(ponto_medio) < 0)
        intervalo(1) = ponto_medio;
    elseif(func(ponto_medio) > 0)
        intervalo(2) = ponto_medio;
    end
end

a = func(intervalo(2));
b = func(intervalo(1));

result = (a+b)/2;
disp(result);




