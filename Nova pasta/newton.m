y(x) = x^2;
yd(x) = 2*x;
eps = 0.01;
itmax = 20;

for i = 1:itmax
    x = x - (y(x)/yd(x));
    if(abs(y(x)) < eps)
        break
    end
end

fprintf("Raiz: %f\n", x);