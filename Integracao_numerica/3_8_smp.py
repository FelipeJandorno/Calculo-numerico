#  Objetivo: Integrar uma determinada função utilizando a regra de 3/8 de Simpson
#
# DICIONÁRIO DE FUNÇÕES
# a = limite inferior de integração
# b = limite superior de integração
# n = quantidade de subintervalos utilizados (precisam ser pelo menos 3)
# h = tamanho de cada subintervalo de integração
# result_integral = resultado da integração
# cnt = contador de loops
# test = variável de controle de saída do loop
 

# A função fnc é responsável por retornar o resultado de um determinado valor x aplicado a uma determinada função
# Para integrar outra função, basta alterar o código definido nessa função
def fnc(x):
    f = 1/(1+pow(x, 2))
    f = 4*f
    return f

def smp_3_8_rep(a, b, n):
    h = (b-a)/n
    x = a   #y1
    cnt = 0
    test = True
    result_integral = 0
    
    while(test):
        if(cnt == 0):
            result_integral = result_integral + fnc(x)
        elif(cnt == n):
            result_integral = result_integral + fnc(x)
        elif(cnt%3 == 0):
            result_integral = result_integral + 2*fnc(x)
        else:
            result_integral = result_integral + 3*fnc(x)
        
        if(cnt >= (n)):
            test = False
            
        x = x + h
        cnt = cnt + 1 #end loop
    
    result_integral = result_integral * (3*h/8) 
    print('resultado: ', result_integral)
smp_3_8_rep(0, 1, 102)
    
