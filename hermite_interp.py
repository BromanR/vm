import numpy as np
import math
from scipy.misc import derivative

def DivDefHermite(dd):      #dd - такая матрица, где нулевой столбец - столбец "иксов", первый столбец - столбец значений
    for k in range(1,n):    #второй столбец - столбец производных и т.д
        for i in range(n-1,k-1,-1):
            if (dd[i][0]==dd[i-k][0]):
                dd[i][1]=dd[i][k+1]/math.factorial(k)
            else:    
                dd[i][1]=float(dd[i][1]-dd[i-1][1])/(dd[i][0]-dd[i-k][0]) 

def f(x): #значение получившегося многочлена
    return coeff[0]+coeff[1]*x+coeff[2]*x*(x-1)+coeff[3]*x*(x-1)**2+coeff[4]*x*(x-1)**2*(x-2)+coeff[5]*x*(x-1)**2*(x-2)**2+coeff[6]*x*(x-1)**2*(x-2)**3

def df(x): #производная функции, которая выше
    return derivative(f,x,dx=1e-6)

def ddf(x): #вторая производная
    return derivative(df,x,dx=1e-6)                   

val=[[0,6],[1,-2,-2],[2,-14,-18,-24],[3,-30]]
height=len(val)
print ("Начальные данные:")
for i in range(height):
    for j in range(len(val[i])):
        print(val[i][j], end=' ')
    print()
print ()    
n=0
for i in range(height):
    n+=len(val[i])-1            #считаем кол-во узлов интерполирования 
repit=[]                        #далее некоторые строчки начальной матрицы будут специально дублированы
for i in range(height):         #сделано это для удобства подсчета разделенных разностей
    repit.append(len(val[i])-1) #строчка будет записана столько раз, сколько в этой точке есть производных -  
val[0]+=[0,0]                   #repit считает, сколько раз какую строку дублировать
val[1]+=[0]                     #дополняем нулями, чтобы получить матрицу, а не массив list'ов, иначе сложности
val[3]+=[0,0]    

dd=np.repeat(val, repit, axis=0) #здесь происходит создание дубликатов строк

DivDefHermite(dd)#считаем разделенные разности

coeff=[]  #в этом блоке кода, мы выводим получившийся многочлен
for i in range (n):
    coeff.append(dd[i][1])
polynoms = ['x','x*(x-1)','x*(x-1)^2','x*(x-1)^2*(x-2)','x*(x-1)^2*(x-2)^2','x*(x-1)^2*(x-2)^3','x*(x-1)^2*(x-2)^3*(x-3)']     
p = str(coeff[0])+"+"
for i in range(1,len(coeff)):
    p+=(str(coeff[i])+polynoms[i-1]+"+")
p = p[:-1]
print(p)
    
print ("Значение функции в точке x=0:",f(0))
print ("Значение функции в точке x=1:",f(1))
print ("Значение функции в точке x=2:",f(2))
print ("Значение функции в точке x=3:",f(3))
print ("Значение первой производной в точке x=1:",round(df(1)))
print ("Значение первой производной в точке x=2:",round (df(2)))
print ("Значение второй производной в точке x=2:",round (ddf(2)))
