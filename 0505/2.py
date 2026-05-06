import random

def printmat(n,m):
    for i in range(n):
        for j in range(n):
            print(f"{m[i][j]:0{len(str(n*n*10))}d}",end=' ')
        print()

def createmat(n):
    return [[random.randint(0,n*n*10) for _ in range(n)] for _ in range(n)]

n=int(input())
m=createmat(n)
printmat(n,m)
print()
for i in range(n):
    for j in range(i,n):
        tmp=m[i][j]
        m[i][j]=m[j][i]
        m[j][i]=tmp
printmat(n,m)