case = int(input())
ans = list()

for i in range(case):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    score = 0
    pos = M

    if N == 1:
        ans.append(1)
    else:
        while True:
            #print(importance, pos)

            if importance[0] == max(importance):
                del(importance[0])
                score += 1
                
                if pos == 0:
                    break
                pos -= 1

            else:
                importance.append(importance[0])
                del(importance[0])
                if pos == 0:
                    pos = len(importance) - 1
                else:
                    pos -= 1

            if len(importance) == 0:
                break

        ans.append(score)

for _ in ans:
    print(_)
