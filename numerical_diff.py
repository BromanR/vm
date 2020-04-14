from math import exp
import numpy as np
from tabulate import tabulate
from interp2 import interpEqDist
from interp1 import interp
from interp1 import DivDiff

def f(x): return round(exp(5*x),d)
def d_f(x): return round(5*exp(5*x),d)               #первая производная
def d2_f(x): return round (25*exp(5*x),d)            #вторая 

d=6                                                  #точность с которой округляем (кол-во знаков после запятой)
h=0.1                                                #шаг
n=11                                                 #кол-во точек
start = 0.5                                          #первая точка
xp = [start+round(i*h,d) for i in range(n)]
yp=[f(xp[i]) for i in range (n)]

d_yp=[d_f(xp[i]) for i in range (n)]                 #точные значения первой производной
d2_yp=[round(d2_f(xp[i]),d) for i in range (n)]      #второй

# calc_*** - посчитанные что-либо
# err_*** - погрешность чего-либо
# ***_df_*** - первая производная
# ***_d2f_*** - вторая производная   err_calc_df_Oh
# ***_0h - погрешность O(h)
# ***_0h2 - погрешность O(h^2)
calc_df_Oh=[] 
err_calc_df_Oh=[] 
for i in range (n-1):
    calc_df_Oh.append(round(((yp[i+1]-yp[i])/h),d))  
calc_df_Oh.append(round((yp[n-1]-yp[n-2])/h,d))
for i in range (n):
    err_calc_df_Oh.append(round(abs(d_yp[i]-calc_df_Oh[i]),d))  

calc_df_0h2=[round((-3*yp[0]+4*yp[1]-yp[2])/(2*h),d)]
err_calc_df_0h2=[]
for i in range (1,n-1):
    calc_df_0h2.append(round((yp[i+1]-yp[i-1])/(2*h),d))
calc_df_0h2.append(round((3*yp[n-1]-4*yp[n-2]+yp[n-3])/(2*h),d))
for i in range (n):
    err_calc_df_0h2.append(round(abs(d_yp[i]-calc_df_0h2[i]),d))  

calc_d2f=[0]
err_calc_d2f=[0]
for i in range (1,n-1):
    calc_d2f.append((yp[i+1]-2*yp[i]+yp[i-1])/h**2)
calc_d2f.append(0)
for i in range (1,n-1):
    err_calc_d2f.append(round((abs(d2_yp[i]-calc_d2f[i])),d)) 
err_calc_d2f.append(0) 

data=[[]] #создаем таблицу как двумерную матрицу, чтобы аккуратно вывести
data=np.column_stack((xp,yp,d_yp,calc_df_Oh,err_calc_df_Oh,calc_df_0h2,err_calc_df_0h2,d2_yp,calc_d2f,err_calc_d2f))

print (" x       y          y'      ÿ'O(h)     err ÿ      ÿ'O(h^2)    errÿ        y''        ÿ''       errÿ''")
print(tabulate(data))    

xq=1 #точка в которой будем искать производную
h=0.25 #начнем с этого значения h
err0=abs(d_f(xq)-(round((3*f(xq)-4*f(xq-h)+f(xq-2*h))/(2*h),d)))
h=h/2
err1=abs(d_f(xq)-(round((3*f(xq)-4*f(xq-h)+f(xq-2*h))/(2*h),d)))
while err1<err0: #ищем ~оптимальное h
    h=h/2
    err0=err1
    err1=abs(d_f(xq)-(round((3*f(xq)-4*f(xq-h)+f(xq-2*h))/(2*h),d)))
h*=2    

print ("погрешность", round(err0,d))    
print ("шаг подобранный эксперементально:", h)
        
#считаем дифференцированием интерполяционного многочлена в форме Ньютона        
f1=interp(xp,yp,xq,n)
f2=interp(xp,yp,xq-h,n)
f3=interp(xp,yp,xq-2*h,n)
print ("погрешность", round(d_f(xq)-(3*f1-4*f2+f3)/(2*h),d)) 
