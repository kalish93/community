# class Solution:
def myPow( x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    # elif n == 0:
    #     return 1
    elif n < 0:
        return float(1.0/( x * myPow(x , n+1)))
    
    else:
        return x * myPow(x,n-1)
        

x = 2
n = -4
print(myPow(x,n))