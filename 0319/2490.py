for i in range(3):
    t = list(map(int,input().split()))
    x = t.count(0)
    y = t.count(1)

    if x==1 and y==3:
        print('A')
    elif x==2 and y==2:
        print('B')
    elif x==3 and y==1:
        print('C')
    elif x==4 and y==0:
        print('D')
    else :
        print('E')