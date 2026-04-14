import sys
input = sys.stdin.readline
while True:
    try:
        line = input()
        if not line:
            break
        
        a,b = map(int,line.split())
        print(a+b)

    except:
        break