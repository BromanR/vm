import numpy as np
import math
n=3
yp=[1,2,3]
h=0.1
num1_d_yp=[]

for i in range (n-1):
    num1_d_yp.append((yp[i+1]-yp[i])/h)