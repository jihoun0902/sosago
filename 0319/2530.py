h,m,s = map(int,input().split())
ct = int(input())

cts = (ct+s)//60
s = (ct+s)%60
ctm = (cts+m)//60
m = (cts+m)%60
h = ctm+h
h %=24

print(f'{h} {m} {s}')