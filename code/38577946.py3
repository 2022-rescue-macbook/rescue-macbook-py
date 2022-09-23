import sys
 
case = int(sys.stdin.readline())
for i in range(case):
    table = []
    n, m = map(int,sys.stdin.readline().split())
    queue = list(map(int,sys.stdin.readline().split()))
    for i in queue:
        table.append(i)
    p = m
    count = 0
    while(True):
        if(max(table) == table[0]):
            table.pop(0)
            count += 1
            if(p == 0):
                print(count)
                break
            else:
                p -= 1
                if(p < 0):
                    p = len(table) - 1
        else:
            p -= 1
            if(p < 0):
                p = len(table) - 1
            table.append(table.pop(0))