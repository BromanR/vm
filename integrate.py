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
print ("(почти)точное значение", exact)
print()
simpson=integrate_simpson(0,1,4)
print ("Результат по формуле Симспона: ", simpson)    
print ("Погрешность: ", abs(exact-simpson))
print()
def p(x): 
    return math.sqrt(1 - x)
nodes = [0, 0.5, 1]
def f(x):
    return math.exp(x)
coeffs = [6 / 35, 16 / 35, 4 / 105]
weights_value = sum([coeffs[i] * f(nodes[i]) for i in range(len(nodes))])
print ("Результат используя интерполяционную формулу с весом: ",weights_value)
print ("Погрешность: ", abs(exact-weights_value))
print()

a=0
b=1
nodes = [-1 / math.sqrt(3), 1 / math.sqrt(3)]
coeffs = [1, 1]
gauss_value = sum([coeffs[i] * func((b-a)/2*nodes[i]+(b+a)/2) for i in range(len(nodes))]) * (b - a) / 2
print ("Результат используя формулу Гаусса с двумя узлами: ",gauss_value)
print ("Погрешность: ", abs(exact-gauss_value))
print()

nodes = [4/9+4*(math.sqrt(17/35))/9, 4/9-4*(math.sqrt(17/35))/9]
coeffs = [-1/30*math.sqrt(35/17)+1/3, 1/30*math.sqrt(35/17)+1/3]
gauss_like_value = sum([coeffs[i] * f(nodes[i]) for i in range(len(nodes))]) 
print ("Результат использу формулу типа Гаусса с двумя узлами    : ",gauss_like_value)
print ("Погрешность: ", abs(exact-gauss_like_value))