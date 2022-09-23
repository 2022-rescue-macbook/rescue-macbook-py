n = int(input())
for i in range(n):
    elem, find = map(int,input().split())
    crit = list(map(int,input().split()))
    foll = [0 for x in crit]
    foll[find] = 1
    big = max(crit)
    count = 0
    while 1:
        if crit[0] == big:
            if foll[0] == 1:
                print(count + 1)
                break
            else:
                count += 1
                del(crit[0])
                del(foll[0])
                big = max(crit)
        else:
            crit.append(crit[0])
            del(crit[0])
            foll.append(foll[0])
            del(foll[0])