from fractions import Fraction

def rec (A, N):
    x2=A[-1]
    L=[]
    m=1
    for val in A:
        m+=val
    while (x2<=N*m): #TODO: trouver une meilleure majoration de x_i+1 
        L.append([*A, x2])
        x2+=1
    return L

def rec2 (x, N):
    L=[[x]]
    count=1
    while (count<N):
        Lt=[]
        for k in range (len(L)):
            for val in rec(L[k], N): #TODO: voir pour fusionner rec et rec2
                Lt.append(val)
        L=Lt
        count+=1
    return L


def check (r):
    s = 0
    for i in range(len(r)):
        s+=Fraction(1,r[i])
    return(s==1)

def solve (N):
    L=[[N]*N]
    for i in range(2, N):
        r = rec2(i, N)
        for i in r:
            if(check(i)):
                L.append(i)
    return L

# Tests
r1=solve(3)
print(r1, len(r1))
r2=solve(4)
print(r2, len(r2))
r3=solve(5)
print(r3, len(r3))