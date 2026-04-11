import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    vps = input().strip()
    count = 0
    for i in vps:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print('YES')
    else:
        print('NO')