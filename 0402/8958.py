import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    ox = input().rstrip()
    score = 0
    count = 0
    for i in ox:
        if i == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)