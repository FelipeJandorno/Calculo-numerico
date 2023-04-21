import math as mt

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
    
    
