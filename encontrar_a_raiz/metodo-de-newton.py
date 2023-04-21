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
    stop = True
    
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


