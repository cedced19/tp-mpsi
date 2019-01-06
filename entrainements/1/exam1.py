#!/usr/bin/python3

def somme(n):
    S=0
    sgn=-1
    for k in range(1,n+1):
       S+=sgn/(k*k)
       sgn=-sgn
    return(S)

def produit(n):
    P=1
    for k in range(1,n):
        P=P*((k-n)/(k+n))
    return(P)

def maxi_c(L):
    x=L[0]
    y=L[1]
    maxi=abs(x-y)
    for i in range(2,len(L)):
        x=y
        y=L[i]
        t=abs(x-y)
        if t>maxi:
            maxi=t
    return(maxi)

def median(L):
    medians=[]
    for k in L:
        up=0
        down=0
        for i in L:
            if i<=k:
                down+=1
            if i>=k:
                up+=1
        if (2*up >= len(L) & 2*down >= len(L)):
            medians.append(k)
    return(min(medians))

def dio2 (p):
    L=[]
    x=0
    z=2*p*p
    while x*x <= z:
        y=x
        while x*x+y*y <= z:
            if (x*x+y*y) == z:
                L.append([x,y])
            y+=1
        x+=1
    return(L)

def diovar(p):
    T=[]
    for i in range(p+1):
        r = dio2(i)
        for k in range(len(r)):
            r[k].append(i)
        T.append(r)
    return T

def nontriv(m):
    L=[]
    for k in range(m+1):
        if len(dio2(k))>1:
            L.append(k)
    return L

def valmax(m):
    maxi=0
    maxi_list=[]
    for k in range(m+1):
        t=len(dio2(k))
        if maxi<t:
            maxi=t
            maxi_list=[]
        if maxi==t:
            maxi_list.append(k)
    return maxi_list

def comp(l1,l2):
    if len(l1) != len(l2):
        return False
    i=0
    test = True
    while i<len(l1) and test:
        test=(l1[i]==l2[i])
        i+=1
    return test

def ana1(l1,l2):
    l1b = sorted(l1)
    l2b = sorted(l2)
    #print(l1b,l2b)
    return(comp(l1b,l2b))

def ana2(l1,l2):
    ll1 = l1.lower()
    ll2 = l2.lower()

    l1b=[x for x in ll1 if x != ' ']
    l2b=[x for x in ll2 if x != ' ']
    #print(l1b,l2b)
    return(comp(sorted(l1b),sorted(l2b)))

print(ana2('prin t', 'pirnt'))