n = int(input())
m = list(map(int,input().split()))
result = 0
m.sort()
for i in range(n):
        result += (m[i]*(i-(n-1-i)))*2
print(result)