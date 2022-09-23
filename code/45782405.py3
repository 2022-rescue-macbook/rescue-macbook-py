from sys import stdin

t = int(stdin.readline())

for _ in range(t) :
    n,m = map(int,stdin.readline().split())
    priority = list(map(int,stdin.readline().rstrip().split()))

    box = []
    for i,j in enumerate(priority) :
        box.append((j,i))

    cnt = 0    
    while True :
        x = box.pop(0)

        for i in box :
            if x[0] < i[0] :
                box.append(x)
                break
        else :
            cnt +=1

            if x[1] == m :
                print(cnt)
                break