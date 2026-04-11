m = []
for i in range(9):
    m.append(int(input()))
print(max(m))
print(m.index(max(m)) + 1)