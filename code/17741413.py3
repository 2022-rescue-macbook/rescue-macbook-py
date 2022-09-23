def docsCheck():
    global docs, cnt
    L = len(docs)
    for i in range(1, L):
        if docs[i][0] > docs[0][0]:
            temp = docs.pop(0)
            docs.append(temp)
            return False
    else:
        temp = docs.pop(0)
        cnt += 1
        return temp

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    docs = []

    for i in range(N):
        docs.append([importance[i], i])

    if N == 1:
        print(1)
    else:
        cnt = 0
        while True:
            result = docsCheck()
            if result != False:
                if result[1] == M:
                    print(cnt)
                    break