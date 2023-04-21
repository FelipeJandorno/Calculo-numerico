# Objetivo: integrar uma determinada função utilizando a regra 1/3 de Simpson
#
# DICIONÁRIO DE VARIÁVEIS
#   a = limite inferior de integração
#   b = limite superior de integração
#   n = quantidade de repartições (precisa ser um número múltiplo de 3)
#   m = tamanho de cada subintervalo de integração
#   cnt = contador de loops
#   smp = resultado da integração
#   test = variável de controle de saída do loop

import math as mt

# A função fnc é responsável por retornar o resultado de um determinado valor x aplicado a uma determinada função
# Para integrar outra função, basta alterar o código definido nessa função
def fnc(x):
    f = mt.sqrt(x) + (1/x)
    return f

def int_spm(a, b, n):
    m = (b-a)/n
    cnt = 1
    smp = 0
    test = True
    
    while(test):
        
        x = a + (cnt*m)
        
        if(cnt%2 == 0):
            smp = smp + 2*fnc(x)
        else:
            smp = smp + 4*fnc(x)
            
        cnt = cnt + 1
        print('x: ', x)
        
        if(cnt == n):
            test = False
    
    smp = smp + fnc(a) + fnc(b)
    smp = smp*(m/3)
    
    print('smp: ', smp)
    
int_spm(1.4, 1.8, 4)
    
    
