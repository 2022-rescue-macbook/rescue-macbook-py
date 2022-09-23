n= int(input())
for i in range(n):
    N, M = list(map(int, input().split()))
    Rank = list(map(int, input().split()))
    num, count, cycle = 0, 0, 0  #num은 검사한 횟수, count는 print한 횟수, cycle = 한바퀴 돌았을 때 추가해주는 것.
    while count < N:
        if max(Rank) == Rank[0]:
            Rank.pop(0)
            count += 1
            if num == M + cycle:
                cnt = count
                break
            num += 1
        else:
            Rank.append(Rank.pop(0))
            if num == M + cycle:
                cycle += len(Rank)
            num += 1
    print(cnt) 