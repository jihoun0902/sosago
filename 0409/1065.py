def hansu(d):
    if d < 100: return True
    a,b,c = map(int,str(d))
    return (a-b) == (b-c)

n = int(input())
print(sum(1 for i in range(1, n+1) if hansu(i)))