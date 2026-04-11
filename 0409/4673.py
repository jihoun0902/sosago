def d(n):
    n += sum(map(int, str(n)))
    return n
an = set(d(i) for i in range(1, 10001))
self_num = set(i for i in range(1, 10001) if i not in an)
for i in sorted(self_num):
    print(i)