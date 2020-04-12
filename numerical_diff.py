from math import exp
import numpy as np

def f(x): return exp(5*x)
def d_f(x): return 5*exp(5*x)
def d2_f(x): return 25*exp(5*x)

h=0.1
n=11
xp = [i*h for i in range(n)]
yp=[f(xp[i]) for i in range (n)]

d_yp=[d_f(xp[i]) for i in range (n)]
d2_yp=[d2_f(xp[i]) for i in range (n)]
print (xp)
print (yp)
print (d_yp)
print (d2_yp)

num1_d_yp=[]
err_num1=[]
for i in range (n-1):
    num1_d_yp.append((yp[i+1]-yp[i])/h)
num1_d_yp.append((yp[n-1]-yp[n-2])/h)
for i in range (n):
    err_num1.append(abs(d_yp[i]-num1_d_yp[i]))  
print(err_num1)
num2_d_yp=[]
err_num2=[]
for i in range (n-1):
    num2_d_yp.append((yp[i+1]-yp[i-1])/(2*h))
num2_d_yp.append((3*yp[n-1]-4*yp[n-2]+yp[n-3])/(2*h))
for i in range (n):
    err_num2.append(abs(d_yp[i]-num2_d_yp[i]))  
print(err_num2)
num2_d2_yp=[]
err_num2_d2=[]
for i in range (1,n-1):
    num2_d2_yp.append((yp[i+1]-2*yp[i]+yp[i-1])/h**2)
for i in range (1,n-1):
    err_num2_d2.append(abs(d2_yp[i]-num2_d2_yp[i-1]))  
print(err_num2_d2)