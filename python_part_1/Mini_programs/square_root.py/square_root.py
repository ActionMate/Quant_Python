import math
def is_square(n):
    if n>=0:
        if n%math.sqrt(n)==0:
            return True
        else:
           return False
    else:
        return False

def is_square_2nd_method(n):   
    if n<0:
        return False
    i=0
    while i*i<=n:
        if i*i==n:
            return True
        i+=1

def is_square_3rd_method(n):
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n

def is_square_4th_method(n):
    if n < 0:
        return False
    root=math.sqrt(n)
    return root.is_integer()
    if root.is_integer():
        return True
   