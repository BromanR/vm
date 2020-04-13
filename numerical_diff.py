from math import exp
import numpy as np
from tabulate import tabulate

def f(x): return round(exp(5*x),d)
def d_f(x): return round(5*exp(5*x),d)
def d2_f(x): return round (25*exp(5*x),d)

d=5
h=0.1
n=11
xp = [round(i*h,d) for i in range(n)]
yp=[f(xp[i]) for i in range (n)]

d_yp=[d_f(xp[i]) for i in range (n)]
d2_yp=[round(d2_f(xp[i]),d) for i in range (n)]


calc_df_Oh=[]
err_calc_df_0h=[]
for i in range (n-1):
    calc_df_Oh.append(round(((yp[i+1]-yp[i])/h),d))
calc_df_Oh.append(round((yp[n-1]-yp[n-2])/h,d))
for i in range (n):
    err_calc_df_0h.append(round(abs(d_yp[i]-calc_df_Oh[i]),d))  

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

data=[[]]
data=np.column_stack((xp,yp,d_yp,calc_df_Oh,err_calc_df_0h,calc_df_0h2,err_calc_df_0h2,d2_yp,calc_d2f,err_calc_d2f))

print (" x       y          y'         ÿ'       err ÿ'       ÿ'       errÿ'       y''       ÿ''      errÿ''")
print(tabulate(data))    

xq=1
h=0.25
err0=1000
err1=999
while err1<err0:
    err0=err1
    err1=abs(d_f(xq)-(round((3*f(xq)-4*f(xq-h)+f(xq-2*h))/(2*h),d)))
    print (err1)
    h=h/2

print (round((3*f(xq)-4*f(xq-h)+f(xq-2*h))/(2*h),d))    
print (h)
        
print (round((-11*f(xq)+18*f(xq+h)-9*f(xq+2*h)+2*f(xq+3*h))/(6*h),d))    