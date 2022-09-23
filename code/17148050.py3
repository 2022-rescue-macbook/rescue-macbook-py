t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    cnt = 0
    answer_index = m
    while p:
        if(p[0]==max(p)):
            cnt += 1
            if(answer_index==0):
                print(cnt)
                break
            answer_index -= 1
            if(answer_index == -1):
                answer_index = len(p)-1
            p.pop(0)

        else:
            temp = p.pop(0)
            p.append(temp)
            answer_index -= 1
            if(answer_index == -1):
                answer_index = len(p)-1