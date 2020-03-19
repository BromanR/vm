import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy

n=6 #кол-во узлов
xp=[-0.4, -0.2, -0.5, -0.6, 0, 0.1]
yp=[0 for i in  range(n)]
i=0 
while i<n:
    yp[i]=np.arcsin(xp[i])
    #print (yp[i])
    i+=1
q=-0.3 #question - искомый узел


for k in range(1,n):
    for i in range(n-1,k-1,-1):
        yp[i]=float(yp[i]-yp[i-1])/(xp[i]-xp[i-k]) #считаем р-р
temp=yp[n-1]
for i in range (0,n):
    temp=temp*(q-xp[n-i-1])+yp[n-i-1]  #считаем значение многочлена в нужной точке
print ("полученное значение: ", temp) #полученное значение
print ("разница с фактическим: ", temp-np.arcsin(q)) 


max_x = opt.fmin_l_bfgs_b(np.arcin(xp[i]), 1.0, bounds=[(-1,1)],approx_grad=True)



