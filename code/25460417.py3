K = int(input())
for _ in range(K):
    answer = 0
    length, location = map(int,input().split())
    priorities = list(map(int, input().split()))
    sorted_priorities = sorted(priorities, reverse=True)
    sorted_priorities.append(0)
    i_p = [(i,p) for i, p in enumerate(priorities)]
    maxV = sorted_priorities.pop(0)

    while i_p:
        temp = i_p.pop(0)
        if temp[1] != maxV:
            i_p.append(temp)
        else:
            maxV = sorted_priorities.pop(0)
            answer+=1
            if location == temp[0]:
                print(answer)
                break
    