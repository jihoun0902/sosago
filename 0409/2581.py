n = int(input())
m = int(input())
num = []
for i in range(n,m+1):
    if i == 1: continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:break
    else: num.append(i)
if len(num) == 0: print(-1)
else: print(sum(num)),print(min(num))