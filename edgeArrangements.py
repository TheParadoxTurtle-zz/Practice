from fractions import Fraction
from math import ceil

c = {}

def answer(N, K):
    # your code here
    if K < N-1:
        return 0
    m = choose(N, 2)
    if K > m:
        return 0
    val = choose(m, K)
    for i in range(1, int(ceil(N/2)) + 1):
        up = choose(i , 2)
        tot = 0
        up2 = choose(N - i, 2)
        for j in range(0, up+1):
            temp = choose(up2, K-j)
            if temp == 0:
                continue
            tot += temp*choose(up, j)
        val -= tot*choose(N, i)
    
    return val


def choose(n,k):
    if n < k:
        return 0
    if (n,k) in c:
        return c[(n,k)]
    c[(n,k)] =  int( reduce(lambda x,y:x*y, (Fraction(n-i, i+1) for i in range(k)), 1) )
    c[(n, n-k)] = c[(n,k)]
    return c[(n,k)]
    
    
    
print answer(5, 4)
print c
