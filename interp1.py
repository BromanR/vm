import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy
import sympy as sp
import math
from scipy.misc import derivative
import copy

def DivDiff(yp1,xp): #разделенные разности yp
    for k in range(1,n):
        for i in range(n-1,k-1,-1):
            yp1[i]=float(yp1[i]-yp1[i-1])/(xp[i]-xp[i-k]) 
def sortByDistance(a): #в идеале надо сделать автоматическую сортировку внутри входных данных
        return (abs(xq-a)) #но тогда надо делать не два массива, а одну матрицу
#задача уже сдана, а сейчас делать мне лень
            
def interp (xp,yp,xq,n):  #xp, yp - узлы и значение функции в этих узлах соответственно, xq - искомый узел, n - кол-во узлов
    yp1=copy.deepcopy(yp) #чтобы не изменять входные данные
    #xp1=copy.deepcopy(xp)
    #xp1.sort(key=sortByDistance)
    DivDiff(yp1,xp)
    temp=yp1[n-1]
    for i in range (0,n-1):
       temp=temp*(xq-xp[n-i-2])+yp1[n-i-2]  #считаем значение многочлена в нужной точке
    return(temp) #возвращаем получе нное значение

def fun(x):
    return sp.asin(x) 
        
xp=[-0.4, -0.2, -0.5, -0.6, 0, 0.1]
n=len(xp)
yp=[0 for i in  range(n)]
i=0
while i<n:
    yp[i]=np.arcsin(xp[i])
    i+=1
xq=-0.3 #xq - искомый узел       
ans=interp(xp,yp,xq,n) 
print ("полученное значение: ", ans) 
print ("фактическая погрешность: ", abs(ans-np.arcsin(xq))) 

#print(sp.diff(fun(x),x,6)) #6-ая производная от арксинуса
def fc(x): return 15*x*(63*x**4/(1 - x**2)**2 + 70*x**2/(1 - x**2) + 15)/(1 - x**2)**(7/2) #это 6-ая производная от арксинуса
#функция нечетная -> найдя максимум - найдем минимум

#поиск максимума производной
maximum=opt.minimize_scalar(fc,bounds=(-0.6,0.1),method='bounded') # по идее вместо fc должно стоять sp.diff(fun(x),x,6)), но я не знаю как это реализовать
print ("оценка модуля производной:", abs(maximum.fun))
err=-maximum.fun
for i in range (0,6):
    err=err*(xq-xp[i])
print ("оценка погрешности", (abs(err/math.factorial(n))))





