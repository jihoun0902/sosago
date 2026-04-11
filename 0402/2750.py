import sys
input = sys.stdin.readline
n = int(input())
m = []
for _ in range(n):
    k = int(input())
    m.append(k)
m.sort()
for i in range(n):
    print(m[i])    