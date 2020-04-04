import numpy as np
import sympy as sp
from scipy.misc import derivative
from interp1 import DivDiff #когда делается импорт из interp1, interp1 прогоняется и я не знаю как это убрать

def f(x): #считает значение функции по многочлену ньютона
    return yp[0]+yp[1]*(x-xp[0])+yp[2]*(x-xp[0])*(x-xp[1])+yp[3]*(x-xp[0])*(x-xp[1])*(x-xp[2])+yp[4]*(x-xp[0])*(x-xp[1])*(x-xp[2])*(x-xp[3])+yp[5]*(x-xp[0])*(x-xp[1])*(x-xp[2])*(x-xp[3])*(x-xp[4])

def df(abc): #производная функции, которая выше
    return derivative(f,abc,dx=1e-6)

def NewtonsMethod(f,df,x0,eps): #x0 - начальная точка поиска, eps - погрешность
    delta=abs(f(x0))
    while delta>eps:
        x0=x0-f(x0)/df(x0)
        delta=abs(f(x0))
    return(x0)    

xp=[-0.4, -0.2, -0.5, -0.6, 0, 0.1]
n=len(xp)
yp=[0 for i in  range(n)]
i=0
while i<n:
    yp[i]=np.arcsin(xp[i])
    i+=1
DivDiff(yp,xp) #считаем р-р     
yq=-0.8  #искомое значение
yp[0]-=yq #так как мы решаем уравнение Pn=yq -> решаем Pn-yq=0
print("искомая точка: ",NewtonsMethod(f,df,0,1e-6))





