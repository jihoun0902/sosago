total_price = int(input())
count = int(input())
price = 0
for _ in range(count):
    a,b = map(int,input().split())
    price += (a*b)
if price == total_price: print("Yes")
else: print("No")