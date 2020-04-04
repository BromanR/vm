import numpy as np
import sympy as sp
from scipy.misc import derivative


def f(x): #считает значение функции по многочлену ньютона
    return yp[0]+yp[1]*(x-xp[0])+yp[2]*(x-xp[0])*(x-xp[1])+yp[3]*(x-xp[0])*(x-xp[1])*(x-xp[2])+yp[4]*(x-xp[0])*(x-xp[1])*(x-xp[2])*(x-xp[3])+yp[5]*(x-xp[0])*(x-xp[1])*(x-xp[2])*(x-xp[3])*(x-xp[4])

def df(abc): #производная функции, которая выше
    return derivative(f,abc,dx=1e-6)

xp=[-0.4, -0.2, -0.5, -0.6, 0, 0.1]
n=len(xp)
yp=[0 for i in  range(n)]
i=0
while i<n:
    yp[i]=np.arcsin(xp[i])
    i+=1
for k in range(1,n):
    for i in range(n-1,k-1,-1):
        yp[i]=float(yp[i]-yp[i-1])/(xp[i]-xp[i-k]) #считаем р-р       
yq=-0.8  
yp[0]=yp[0]-yq #так как мы решаем уравнение Pn=yq -> решаем Pn-yq=0
x0=0 #изначальная точка поиска
eps=1e-6
delta=abs(f(x0))
while delta>eps:
    x0=x0-f(x0)/df(x0)
    delta=abs(f(x0))
print (x0)
print (f(x0))




