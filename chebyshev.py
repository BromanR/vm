import sympy as sp
import numpy as np
import copy

def f(x):
    return 1 / (x**2 + 1)
a, b = -1, 1
order = 6 #на самом деле это order + 1
exact=0.977995

# Compute Chebyshev xp
xp = [np.cos(np.pi * (2 * k - 1) / (2 * order)) for k in range(1,order)]
yp = [f(xp[i]) for i in range(len(xp))]
xq=0.15 #xq - искомый узел 

def DivDiff(yp1,xp): #разделенные разности yp
    for k in range(1,n):
        for i in range(n-1,k-1,-1):
            yp1[i]=float(yp1[i]-yp1[i-1])/(xp[i]-xp[i-k]) 


def interp (xp,yp,xq,n):  #xp, yp - узлы и значение функции в этих узлах соответственно, xq - искомый узел, n - кол-во узлов
    yp1=copy.deepcopy(yp) #чтобы не изменять входные данные
    #xp1=copy.deepcopy(xp)
    #xp1.sort(key=sortByDistance)
    DivDiff(yp1,xp)
    temp=yp1[n-1]
    for i in range (0,n-1):
       temp=temp*(xq-xp[n-i-2])+yp1[n-i-2]  #считаем значение многочлена в нужной точке
    return(temp) #возвращаем получе нное значение


n=len(xp)
xq=0.15 #xq - искомый узел       
ans=interp(xp,yp,xq,n) 
print ("полученное значение с помощью многочлена Чебышёва: ", ans) 
print ("погрешность: ", abs(ans-exact))


def interpEqDist (xp,yp,xq,n):#xp, yp - узлы и значение функции в этих узлах соответственно, qx - искомый узел, n - cтепень многочлена +1
    yp1=copy.deepcopy(yp)  #чтобы не изменять входные данные
    for k in range(1,n):
        for i in range(n-1,k-1,-1):
            yp1[i]=yp1[i]-yp1[i-1] #считаем к-р       
    temp=yp1[n-1]
    for i in range (1,n):
        temp=temp*(t-(n-i)+1)/(n-i)+yp1[n-i-1]  #считаем значение многочлена в нужной точке
    return(temp) #возвращаем поулученное значение
       
h= (b - a) / (order - 2) #шаг
xp=[-1+i*h for i in  range(order-1)]
yp=[f(xp[i]) for i in range (order-1)]
t=(xq-xp[0])/h
n=order-1 #степень полинома + 1
ans=interpEqDist(xp,yp,xq,n)
print ("полученное значение интерполированием по равностоящим узлам: ", ans) 
print ("погрешность: ", abs(ans-exact))





