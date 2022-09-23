import sys 

read = sys.stdin.readline

Case = int(read())

for _ in range(Case):
    count, index = list(map(int, read().split()))
    pr = list(map(int, read().split()))
    prcount = [pr.count(n) for n in range(10)]
    prmax = max(pr)
    turn = 1
    pos = 0
    
    while True:
        pos = pos if pos < count else 0
        if pr[pos] != prmax:
            pos += 1 
            continue
        
        if pos == index:
            print(turn)
            break
        
        pos += 1
        turn += 1
        prcount[prmax] -= 1
        if prcount[prmax] == 0:
            while prmax != 0:
                prmax -= 1
                if prcount[prmax] != 0:
                    break
