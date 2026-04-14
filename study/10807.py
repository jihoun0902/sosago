import sys
input = sys.stdin.readline
n = int(input())
m = list(map(int,input().split()))
v = int(input())
count = 0
for i in m:
    if i == v:
        count += 1
print(count)