def fac(N):
    if N == 1:
        return 1
    else:
        return N * fac(N - 1)


print(fac(4)) 

def fac2(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac2(5)) 
