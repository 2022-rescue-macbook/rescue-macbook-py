import sys

a = int(sys.stdin.readline())

for _ in range(a) :

    count = 0
    n ,m = map(int, sys.stdin.readline().split())
    lst = [int(i) for i in sys.stdin.readline().split()]
    idx = [i for i in range(n)]

    idx[m] = 'target'

    while(True) :
        
        if(max(lst) == lst[0]) :
            count += 1
            if(idx[0] == 'target') :
                print(count)
                break
            else :
                idx.pop(0)
                lst.pop(0)
        else :
            lst.append(lst.pop(0))
            idx.append(idx.pop(0))