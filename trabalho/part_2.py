# ============ FUNÇÕES AUXILIARES =============== #

# 01. Recebe a lista de coeficientes do polinômio
def input_coef(qnt_coef=0):
    coef_list = []

    if qnt_coef == 0:
        qnt_coef = int(input('Quantidade de coef: '))
    else:
        for k in range(qnt_coef):
            coef_list.append(float(input('y(x{}) - Coef: '.format(k))))
    return coef_list

# 02. Calcula o valor do polinômio com base na lista de input e o valor de x dado pelo usuário
def pol_value(coef_list, x=0, p_x=0):
    for coef in enumerate(coef_list):
        p_x = p_x + (coef[1]*pow(x, coef[0]))
    return p_x

# ============ CÓDIGO PRINCIPAL ============ #

def main():
    x = float(input('x: '))
    p_x = pol_value(input_coef(), x)
    print('resultado p_x: ', p_x)

