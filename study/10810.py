import sys
input = sys.stdin.readline
n,m = map(int,input().split())

buckets = [0] * (n+1)

for _ in range(m):
    i,j,k = map(int,input().split())

    for t in range(i,j+1):
        buckets[t] = k
print(*(buckets[1:]))