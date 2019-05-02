import numpy as np
import sys

def add_mat(A,B):
    (n,p)=np.shape(A)
    C=np.zeros([n,p])
    for i in range(n):
        for j in range(p):
            C[i,j]=A[i,j]+B[i,j]
    return C
            
#A=np.arange(1,12,2).reshape(3,2)
#print(add_mat(A,A))


def mult_scal_mat(A,x):
    (n,p)=np.shape(A)
    for i in range(n):
        for j in range(p):
            A[i,j]=x*A[i,j]
    return A

#A=np.arange(1,12,2).reshape(3,2)
#print(mult_scal_mat(A,2))

def mult_mat(A,B):
    (n,q)=np.shape(A)
    (q,p)=np.shape(B)
    C=np.zeros([n,p])
    for i in range(n):
        for j in range(p):
            s=0
            for k in range(q):
                s+=A[i,k]*B[k,j]
            C[i,j]=s
    return C

#A=np.arange(1,12,2).reshape(3,2)
#B=np.arange(1,12,2).reshape(2,3)
#print(mult_mat(A,B))
#print(np.dot(A,B))

def triangle_mat(A):
    B=np.copy(A)
    (n,n)=np.shape(A)
    for i in range(n-1):
        if B[i,i]==0:
            j=i+1
            while j<n-1 and B[j,i] == 0:
                j+=1
            if B[j,i]!=0:
                for k in range(i,n):
                    x=B[i,k]
                    B[i,k]=B[j,k]
                    B[j,k]=x
        if B[i,i]!=0:
            for j in range(i+1,n):
                p=B[j,i]/B[i,i]
                B[j,i]=0
                for k in range(i+1,n):
                    B[j,k]=B[j,k]-p*B[i,k]
    return B

#C=np.array([[0,1,0,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,1,0,0]])  
#print(triangle_mat(C))

def determinant_abs(A):
    B=triangle_mat(A)
    (n,n)=np.shape(B)
    p=1
    for i in range(n):
        p*=A[i,i]
    return abs(p)

#A=np.eye(3,3)
#print(determinant_abs(A))
#A=np.array([[1,0],[1,1]])
#print(determinant_abs(A))

def inv_mat(A):
    B=np.copy(A)
    (n,p)=np.shape(A)
    I=np.eye(n,p)
    for i in range(n-1):
        if B[i,i]==0:
            j=i+1
            while j<n-1 and B[j,i] == 0:
                j+=1
            if B[j,i]!=0:
                for k in range(i,n): # Pas besoin d'échanger des lignes déjà traité  
                    x=B[i,k]
                    B[i,k]=B[j,k]
                    B[j,k]=x
                for k in range(n): # Il faut faire échanger toutes les lignes   
                    x=I[i,k]
                    I[i,k]=I[j,k] 
                    I[j,k]=x
        if B[i,i]!=0:
            for j in range(i+1,n):
                p=B[j,i]/B[i,i]
                B[j,i]=0
                for k in range(i+1,n):
                    B[j,k]=B[j,k]-p*B[i,k]
                for k in range(n):
                    I[j,k]=I[j,k]-p*I[i,k] 

    # On vérifie si B inversible
    x=1
    for i in range(n):
        x=x*B[i,i]
    if x==0: return ()

    for i in range(n-1,-1,-1):
        for j in range(i-1,0,-1):
                p=B[j,i]/B[i,i]
                for k in range(n):
                    I[j,k]=I[j,k]-p*I[i,k]
    for i in range(n):
        for j in range(n):
            I[i,j]=I[i,j]/B[i,i]
    return I

#C=np.array([[0,1,0,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,1,0,0]])     
#print(inv_mat(C))
#print(np.linalg.inv(C))


def pivot(A,i,n):
    p=abs(A[i,i])
    indice=i
    j=i+1
    while j < n:
        x=abs(A[j,i])
        if x > p:
            p=x
            indice = j
        j+=1
    return(indice,p)

def triangle_pmax(A):
    B=np.copy(A)
    (n,n)=np.shape(A)
    eps=n*sys.float_info.epsilon
    for i in range(n-1):
        (j,pvt)=pivot(A,i,n)
        for k in range(i,n):
            x=B[i,k]
            B[i,k]=B[j,k]
            B[j,k]=x
        if pvt > eps:
            for j in range(i+1,n):
                p=B[j,i]/B[i,i]
                B[j,i]=0
                for k in range(i+1,n):
                    B[j,k]=B[j,k]-p*B[i,k]
    return B

#C=np.array([[0,1,0,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,1,0,0]])  
#print(triangle_mat(C))

def inv_pmax(A):
    B=np.copy(A)
    (n,p)=np.shape(A)
    eps=n*sys.float_info.epsilon
    I=np.eye(n,p)
    for i in range(n-1):
        (j,pvt)=pivot(A,i,n)
        for k in range(i,n): # Pas besoin d'échanger des lignes déjà traité  
            x=B[i,k]
            B[i,k]=B[j,k]
            B[j,k]=x
        for k in range(n): # Il faut faire échanger toutes les lignes   
            x=I[i,k]
            I[i,k]=I[j,k] 
            I[j,k]=x
        if p>eps:
            for j in range(i+1,n):
                p=B[j,i]/B[i,i]
                B[j,i]=0
                for k in range(i+1,n):
                    B[j,k]=B[j,k]-p*B[i,k]
                for k in range(n):
                    I[j,k]=I[j,k]-p*I[i,k] 

    # On vérifie si B inversible
    x=1
    for i in range(n):
        x=x*B[i,i]
    if x==0: return ()

    for i in range(n-1,-1,-1):
        for j in range(i-1,0,-1):
                p=B[j,i]/B[i,i]
                for k in range(n):
                    I[j,k]=I[j,k]-p*I[i,k]
    for i in range(n):
        for j in range(n):
            I[i,j]=I[i,j]/B[i,i]
    return I

C=np.array([[0,1,0,0,0],[0,0,0,1,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,1,0,0]])     
print(inv_mat(C))
print(np.linalg.inv(C))