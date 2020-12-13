import math
import numpy as np
from scipy import misc


def c_simpson(f,a,b,n):
   h = (b-a)/n
   sum = f(a)+f(b)
   for j in range(1,n):
      xj = a+h*j
      if (j%2 == 0):
            sum += 2*f(xj)
      else:
            sum += 4*f(xj)
   sum = h/3*sum 
   return sum