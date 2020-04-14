import numpy as np
import math
n=3
yp=[1,2,3]
xq=-0.3
xp=[-0.4, -0.2, -0.5, -0.6, 0, 0.1]

def sortByDistance(a):
        return (abs(xq-a))
xp.sort(key=sortByDistance)
print (xp)