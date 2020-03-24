import scipy.optimize as opt
import scipy
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def f(x):
    return np.arcsin(x)
print (opt.minimize_scalar(f,bounds=(-1,1),method='bounded'))


x = sp.symbols('x')
def fun(x):
    return sp.asin(x)
    
print(sp.diff(fun(x),x,6))

def fc(x):
    return sp.diff(fun(x),x,6)

print (opt.minimize_scalar(fc(x),bounds=(-0.8,-0.1),method='bounded'))    
