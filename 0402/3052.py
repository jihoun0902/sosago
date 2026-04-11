import sys
input = sys.stdin.readline
n = set()
for _ in range(10):
    n.add(int(input()))
    n = set(map(lambda x: x % 42, n))
print(len(n))