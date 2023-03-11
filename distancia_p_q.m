p = input("Insira o vetor correspondente ao ponto p: ");
q = input("Insira o vetor correspondete ao ponto q: ");

temp = ((p(1) - q(1))^2 + (p(2) - q(2))^2 + (p(3) - q(3))^2);
distancia = sqrt(temp);
fprintf("Distancia: %f\n", distancia)