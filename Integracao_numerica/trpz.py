#Integração numérica utilizando a regra do trapézio

import math as mt

def fnc(x):
    f = mt.exp(x)
    return f

def int_tpz(a, b, n):
    
    h = (b-a)/n
    x = a 
    f = 0
    
    for i in range(n):
        x = x + h
        f = f + fnc(x)
        #print('x: ', x, ' f: ', f)
        
    
    f = (h/2)*((2*f) + fnc(a) + fnc(b))
    print('Resultado f: ', f)

int_tpz(0, 1, 500)
