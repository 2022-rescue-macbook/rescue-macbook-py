T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    Imp = input().split()
    Seq = list(range(N))

    count = 0

    while True:
        
        if Imp[0] == max(Imp):
            count += 1
            if Seq[0] == M:
                break
            else:
                del Imp[0]
                del Seq[0]
        else:
            Imp.append(Imp.pop(0))
            Seq.append(Seq.pop(0))

    print(count)         
