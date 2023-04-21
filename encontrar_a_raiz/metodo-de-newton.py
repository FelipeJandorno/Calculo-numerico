# Objetivo: Encontrar o zero de uma função utilizando o método de Newton
#
# DICIONÁRIO DE VARIÁVEIS
# x0 = chute inicial
# e = precisão do cálculo
# y = valor relacionado à função utilizada
# cnt = contador de loops
# check = o loop é repetido enquanto check = 0, caso contrário termina-se o loop
# def function = função necessária para aplicar o método de newton
# def delta_function = derivada da function

def function(x, y):
    f = pow(x, 2) - y
    return f
    
def delta_function(x):
    fd = 2*x
    return fd

def main(x0, e, y):
    
    cnt = 0
    check = 0
    x = x0
    
    while(cnt != 20):
        xd = x
        x = x - (function(x, y)/delta_function(x))
        print(cnt,' x: ', x)
        cnt = cnt + 1
        
        if((xd-x) < e):
            if(check == 1):
                break
            check = check + 1
        
main(1, 0.00000001, 2)


