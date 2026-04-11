n = int(input("n을 입력하세요: "))
numbers = list(range(1, n + 1))
numbers[0] = 0

for i in range(2, n + 1):
    if numbers[i - 1] != 0:
        for j in range(i * 2, n + 1, i):
            numbers[j - 1] = 0

print([x for x in numbers if x != 0])