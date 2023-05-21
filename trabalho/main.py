import part_1 as pt1
import part_2 as pt2

# Recebe a tabela de valores de x
x_list = pt2.input_coef()

# Calcula o valor dos coeficientes de LaGrange
L_coef = pt1.interpol_lagrange((len(x_list)-1), x_list)

# Calcula o valor do polinômio aplicado em x
p_x = pt2.pol_value(L_coef, x=2)

# Exibe o resultado na tela
print('resultado: ', p_x)