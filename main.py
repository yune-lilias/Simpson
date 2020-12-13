import math
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from scipy import special
from err_upperbound import err_upperbound
from c_simpson import c_simpson

def main():
    f = lambda x: 2/(math.pi)**0.5*math.exp(-x**2)
    f4 = lambda x: 8/(math.pi)**0.5*math.exp(-x**2) *(4*x**4-12*x**2+3)
    f5 = lambda x: 16/(math.pi)**0.5*x*math.exp(-x**2) *(-4*x**4+20*x**2-15)
    listn = [1,2,4,8]
    a = 0
    b = 1
    res = []
    f4_x0 = err_upperbound(0,0.5,f4,f5,0.0001)
    f4_x1 = err_upperbound(0.5,1,f4,f5,0.0001)
    maxroot = 5
    delt = (b-a)/maxroot
    actual_answer = special.erf(1)
    for k in listn:
         temp = c_simpson(f,a,b,k)
         res.append(temp)
         actual_error = -temp + actual_answer
         h = (b-a)/k
         error_bound1 = - (b-a)/180*h**4*f4(f4_x0)
         error_bound2 = - (b-a)/180*h**4*f4(f4_x1)
         print("n= "+str(k) + " \nresult " + str(temp))
         print("error: "+str(actual_error))
         print("error range: ["+str(error_bound1)+" , " + str(error_bound2) + "]")
         print("is error in range?: "+ str(actual_error>=error_bound1 and actual_error<=error_bound2) + "\n")
    
    #find minimum n needs to have error smaller than 10^(-13)
    t = f4(f4_x0)
    h_max = (180*10**(-13)/t)**0.25 
    n_min = math.ceil(1/h_max)

    #n must be even
    if(n_min%2 == 0):
         print("n is: "+ str(n_min))
    else:
         print("n is: "+ str(n_min+1))

main()