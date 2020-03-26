import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy
import sympy as sp
import math

xp=[5+i/10 for i in  range(11)]
#print (xp)

yp=[round(np.sin(xp[i]),5) for i in range (11)]
#print (yp)

xq=5.05 #xquestion - искомый узел
t=(xq-xp[0])/0.1
n=5 #степень полинома+1
for k in range(1,n):
    for i in range(n-1,k-1,-1):
        yp[i]=yp[i]-yp[i-1] #считаем к-р
#print (yp)        
temp=yp[n-1]
for i in range (1,n):
    temp=temp*(t-(n-i)+1)/(n-i)+yp[n-i-1]
print ("полученное значение: ", temp) 
print ("фактическая погрешность: ", temp-np.sin(xq))     
maximum=np.cos(5.4) #5-ая производная синуса=косинус, а он строго возрастает на [5,5.4]
#print (maximum)
err=t*maximum
for i in range (1,n):
    err=err*(t-i)/(i+1)
err=err*(0.1**n)
print ("оценка погрешности", err)