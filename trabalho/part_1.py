def main():
    # Input do grau do polinômio desejado
    grau_pol = int(input('Grau do polinômio: '))

    # Mapeamento dos pontos de interpolação
    x_list = map_pontos(grau_pol+1)

    # Cálculo dos coeficientes de lagrange
    interpol_lagrange(grau_pol+1, x_list)

main()

# ============ FUNÇÕES AUXILIARES =============== #

# 01. Função que realiza o mapeamento dos pontos para a interpolação
def map_pontos(qnt_pnt=0):
    # Inicializa lista que armazenará os pontos de interpolação
    x_list = []

    # Cria a lista com os pontos de interpolação (a quantidade de pontos é igual ao grau do polinômio + 1)
    for k in range(qnt_pnt):
        x = float(input('{} ponto: '.format(k + 1)))
        x_list.append(x)

    # Retorna a lista de pontos de interpolação
    return x_list

# 02. Código responsável por calcular os coeficientes de lagrange (utiliza 03, 04 e 05 em sua execução)
def interpol_lagrange(grau_pol, x_list):
    # Inicializa a lista com os valores presentes no numerador dos coeficientes de lagrange
    num_list = []

    # Inicializa a lista com os valores presentes no denominador dos coeficientes de lagrange
    den_list = []

    for x in x_list:
        # Adiciona o valor do numerador do coeficiente de lagrange à lista de numeradores
        num_list.append(num_lagrange(x, x_list))

    for k in range(grau_pol):
        # Adiciona o valor do denominador do coeficiente de lagrange à lista de denominadores
        den_list.append(den_lagrange(k, x_list))

    L_coef = calc_coef(num_list, den_list)

    print(f"num: {num_list}, den: {den_list}, L_coef: {L_coef}")
    return L_coef

# 03. Identifica os numeradores dos coeficientes de lagrange
def num_lagrange(x, x_list):
    indice = len(x_list) - 1
    num = (x_list[indice] - x)
    return num

# 04. Identifica quais valores pertencem ao denominador do coeficiente de lagrange
def den_lagrange(k, x_list):
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

# 05. Calcula o coeficiente de lagrange com base na lista dos valores do numerador e denominador
def calc_coef(num_list, den_list):
    coef_list = []
    for num in enumerate(num_list):
        if num[1] != 0:
            coef = num[1]/den_list[num[0]]
            coef_list.append(coef)
    return coef_list