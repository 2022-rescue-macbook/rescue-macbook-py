
test_case = int(input())

for i in range(test_case):
    q = list()
    q2 = list()
    N, M = map(int, input().split())

    NList = list(map(int, input().split()))
    temp = list()

    for j in range(9, 0, -1):
        temp.append(NList.count(j))

    for j in range(len(NList)):
        q.append([j, NList[j]])

    cnt = 1
    pr = 9
    for j in temp:
        cnt2 = j
        while cnt2 != 0:
            if q[0][1] == pr:
                if q[0][0] == M:
                    print(cnt)
                cnt2 -= 1
                cnt += 1
                q.pop(0)
            else:
                temp3 = q.pop(0)
                q.append(temp3)
        pr -= 1
