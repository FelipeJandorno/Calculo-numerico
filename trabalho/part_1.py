
# Identifica os numeradores dos coeficientes de lagrange
def num_prod(x, x_list):
    indice = len(x_list) - 1
    prod = (x_list[indice] - x)
    return prod

# Identifica quais valores pertencem ao denominador do coeficiente de lagrange
def den_prod(k, x_list):
    result_list, new_list = [], []
    cnt = 0
    for x in x_list:
        if x != x_list[k]:
            result = x_list[k] - x
            result_list.append(result)

            if len(result_list) == 2:
                new_list.append(result_list[0]*result_list[1])
                result_list = []
    return new_list[0]

def calc_coef(num_list, den_list):
    coef_list = []
    for num in enumerate(num_list):
        if num[1] != 0:
            coef = num[1]/den_list[num[0]]
            coef_list.append(coef)
    return coef_list

# Código responsável por calcular os coeficientes de lagrange
def interpol_lagrange(grau_pol, x_list):
    num_list = []
    den_list = []

    for x in x_list:
        num_list.append(num_prod(x, x_list))

    for k in range(grau_pol):
        den_list.append(den_prod(k, x_list))

    L_coef = calc_coef(num_list, den_list)
    return L_coef

    print("num: {}, den: {}, L_coef: {}".format(num_list, den_list, L_coef))


# Função que realiza o mapeamento dos pontos para a interpolação
def map_pontos(qnt_pnt=0):
    x_list = []
    for k in range(qnt_pnt):
        x = float(input('{} ponto: '.format(k + 1)))
        x_list.append(x)
    return x_list

# Código principal que realiza a interpolação
def main():
    # Input do grau do polinômio desejado
    grau_pol = int(input('Grau do polinômio: '))

    # Mapeamento dos pontos de interpolação
    x_list = map_pontos(grau_pol+1)

    # Cálculo dos coeficientes de lagrange
    interpol_lagrange(grau_pol+1, x_list)
