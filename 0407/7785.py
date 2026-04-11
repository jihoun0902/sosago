n = int(input())
m = set()
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        m.add(name)
    else :
        m.remove(name)
result = sorted(list(m), reverse=True)
for i in result:
    print(i)