import sys
input = sys.stdin.readline
c = int(input())
for _ in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    m = data[1:]
    avg = sum(m) / n
    count = 0
    for i in m:
        if i > avg:
            count += 1
    print(f"{count/n*100:.3f}%")