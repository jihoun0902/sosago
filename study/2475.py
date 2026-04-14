n = list(map(int,input().split()))
sum = 0
total = 0
for i in n:
    sum += i**2
total = sum % 10
print(total)