import sys
input = sys.stdin.readline
a,b = map(int,input().split())
d = {}

for i in range(b):
    student_id = input().strip()
    d[student_id] = i
sorted_list = sorted(d.items(), key = lambda x : x[1])
for i in range(min(a,len(sorted_list))):
    print(sorted_list[i][0])