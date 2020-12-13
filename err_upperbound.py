#use secant method to calculate the min/max
def err_upperbound(x0,x1,f4,f5,prec):
   diff = prec + 1
   while abs(diff) >= prec and f5(x1) != 0:
        diff = (x1-x0)/(f5(x1)-f5(x0))*f5(x1)
        print('diff: '+ str(diff))
        x2 = x1-diff
        x0 = x1
        x1 = x2
   return x1
