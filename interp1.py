import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy
import sympy as sp
import math

def interp (xp,yp,xq,n):  #xp, yp - узлы и значение функции в этих узлах соответственно, qx - искомый узел, n - кол-во узлов
    for k in range(1,n):
        for i in range(n-1,k-1,-1):
            yp[i]=float(yp[i]-yp[i-1])/(xp[i]-xp[i-k]) #считаем р-р
    temp=yp[n-1]
    for i in range (0,n-1):
       temp=temp*(xq-xp[n-i-2])+yp[n-i-2]  #считаем значение многочлена в нужной точке
    return(temp) #возвращаем получе нное значение

xp=[-0.4, -0.2, -0.5, -0.6, 0, 0.1]
n=len(xp)
yp=[0 for i in  range(n)]
i=0
while i<n:
    yp[i]=np.arcsin(xp[i])
    i+=1
qx=-0.3 #qx - искомый узел       
ans=interp(xp,yp,qx,n) 
print ("полученное значение: ", ans) 
print ("фактическая погрешность: ", abs(ans-np.arcsin(qx))) 

x = sp.symbols('x')
def fun(x):
    return sp.asin(x)    
#print(sp.diff(fun(x),x,6)) #6-ая производная от арксинуса

def fc(x): return 15*x*(63*x**4/(1 - x**2)**2 + 70*x**2/(1 - x**2) + 15)/(1 - x**2)**(7/2) #это 6-ая производная от арксинуса
#функция нечетная -> найдя максимум - найдем минимум

#поиск максимума производной
maximum=opt.minimize_scalar(fc,bounds=(-0.6,0.1),method='bounded') # по идее вместо fc должно стоять sp.diff(fun(x),x,6)), но я не знаю как это реализовать
print ("оценка модуля производной:", abs(maximum.fun))
err=-maximum.fun
for i in range (0,6):
    err=err*(qx-xp[i])
print ("оценка погрешности", (abs(err/math.factorial(n))))





