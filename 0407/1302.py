import sys
input = sys.stdin.readline 

n = int(input())
counts = {}

for _ in range(n):
    book = input().strip()
    if book in counts:
        counts[book] += 1
    else:
        counts[book] = 1
sorted_books = sorted(counts.keys())
result = max(sorted_books, key=lambda x: counts[x])

print(result)