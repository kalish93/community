import math
n, m , a= list(map(int, input().split()))
def theatreSquare(n,m,a):
    return math.ceil(m/a) * math.ceil(n/a)
