import part_1 as pt1
import part_2 as pt2

def print_polinomio(coef_list, result):
    pol = []
    for i in range(len(coef_list)):
        if coef_list[i] > 0:
            pol.append('+({}x^{})'.format(coef_list[i], i))
        else:
            pol.append('{}(x^{})'.format(coef_list[i], i))
    print(''.join(pol) + ' = ' + str(result))

# Realiza o produto entre os elementos de duas listas
def prod_list(a_list, b_list):
    result_list = []
    for i in range(len(a_list)):
        result_list.append(a_list[i] * b_list[i])
    return result_list

def main():
    # Recebe o valor do grau do polinomio
    grau_pol = int(input('Grau do polinômio: '))

    # Mapeia os pontos em x para interpolação
    x_list = pt1.map_pontos(qnt_pnt=grau_pol+1)

    # Mapeia os pontos em y para interpolação
    y_list = pt2.input_coef(qnt_coef=len(x_list))

    # Calcula os coeficientes de lagrange
    L_coef = pt1.interpol_lagrange(grau_pol, x_list)

    # Realiza o produto entre os coeficientes de lagrange e os valores de y(x)
    coef_list = prod_list(L_coef, y_list)

    # Calcula o valor do polinomio dado um valor x
    result = pt2.pol_value(coef_list=coef_list, x=3)

    # Exibe o polinomio de lagrange
    print_polinomio(coef_list, result)

main()