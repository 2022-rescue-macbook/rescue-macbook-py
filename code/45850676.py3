import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    number = [i for i in range(N)]
    temp = number[M]

    cnt = 0
    while(True) :
        if importance[0] == max(importance) :
            cnt += 1
            if number[0] == temp :
                print(cnt)
                break
            else :
                importance.pop(0)
                number.pop(0)
        
        else :
            importance.append(importance.pop(0))
            number.append(number.pop(0))