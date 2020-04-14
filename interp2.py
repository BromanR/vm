import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy
import sympy as sp
import math
import copy

def interpEqDist (xp,yp,xq,n):#xp, yp - узлы и значение функции в этих узлах соответственно, qx - искомый узел, n - cтепень многочлена +1
    yp1=copy.deepcopy(yp)  #чтобы не изменять входные данные
    for k in range(1,n):
        for i in range(n-1,k-1,-1):
            yp1[i]=yp1[i]-yp1[i-1] #считаем к-р       
    temp=yp1[n-1]
    for i in range (1,n):
        temp=temp*(t-(n-i)+1)/(n-i)+yp1[n-i-1]  #считаем значение многочлена в нужной точке
    return(temp) #возвращаем поулученное значение
       
h=0.1 #шаг
xp=[5+i*h for i in  range(11)]
yp=[round(np.sin(xp[i]),5) for i in range (11)]
xq=5.05 #xquestion - искомый узел
t=(xq-xp[0])/h
n=5 #степень полинома + 1
ans=interpEqDist(xp,yp,xq,n)
print ("полученное значение: ", ans) 
print ("фактическая погрешность: ", ans-np.sin(xq))  

maximum=np.cos(5.4) #5-ая производная синуса=косинус, а он строго возрастает на [5,5.4]
err=t*maximum
for i in range (1,n):
    err=err*(t-i)/(i+1)
err=err*(0.1**n)
print ("оценка погрешности", err) 
#теоретическая погрешность меньше фактической, тк мы округляли в начале