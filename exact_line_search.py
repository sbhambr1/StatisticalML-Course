import numpy as np
from scipy.optimize import line_search

def obj_func(x):
    return x[0]**2 + (5*x[1]**2)

def obj_grad(x): 
    return [2*x[0],10*x[1]]

x0 = np.array([5,1])
dx0 = np.array([-10,-10])

print(line_search(obj_func,obj_grad,x0,dx0))