import random

def printmat(n,m):
    for i in range(n):
        for j in range(n):
            print(f"{m[i][j]:0{len(str(n*n*10))}d}",end=' ')
        print()

def createmat(n):
    return [[random.randint(0,n*n*10) for _ in range(n)] for _ in range(n)]

n=int(input())
a=createmat(n)
b=createmat(n)
c=createmat(n)
sum = createmat(n)

for i in range(n):
    for j in range(n):
        sum[i][j]=0
        for k in range(n):
            sum[i][j]+=a[i][k]*b[k][j]

for i in range(n):
    for j in range(n):
        sum[i][j]+=c[i][j]
printmat(n,a)
printmat(n,b)
printmat(n,c)
printmat(n,sum)