import math
import numpy as np

def integrate_simpson(a, b, n):
    h = ( b - a )/n 
    x = list() 
    fx = list() 
    i = 0
    while i<= n: 
        x.append(a + i * h) 
        fx.append(func(x[i])) 
        i += 1
    res = 0
    i = 0
    while i<= n: 
        if i == 0 or i == n: 
            res+= fx[i] 
        elif i % 2 != 0: 
            res+= 4 * fx[i] 
        else: 
            res+= 2 * fx[i] 
        i+= 1
    res = res * (h / 3) 
    return res 

def func(x):
    return math.exp(x)*math.sqrt(1-x)

exact=1.030078469278705
simpson=integrate_simpson(0,1,4)
print ("Результат по формуле Симспона: ", simpson)    
print ("Погрешность: ", abs(exact-simpson))