import sys
input = sys.stdin.readline
a,b = map(int,input().split())
h = set()
for _ in range(a):
    h.add(input().rstrip())
s = set()
for _ in range(b):
    s.add(input().rstrip())
result = sorted(h & s)
print(len(result))
for name in result:
    print(name)
