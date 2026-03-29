a, b = map(int, input().split())
results = []

for i in range(1, b + 1):
    c = a * i
    results.append(int(str(c)[::-1]))

print(max(results))