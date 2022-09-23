import sys
from sys import stdin


def print_que(importance, swi, ss):
    for a in range(len(importance)):
        if importance[a] > importance[0]:
            if swi != 0:
                swi-=1
            else:
                swi = len(importance)-1
            return print_que(importance[1:]+[importance[0]], swi, ss)
    if swi == 0:
        return ss+1
    else:
        return print_que(importance[1:], swi-1, ss+1) 



r = lambda: sys.stdin.readline()
fir = int(input())
q =[]
for a in range(fir):
    size, swi = map(int,r().split())
    arr = [0] * size
    importance = stdin.readline().split()
    ss = 0
    dab = print_que(importance, swi, ss)
    print(dab)


