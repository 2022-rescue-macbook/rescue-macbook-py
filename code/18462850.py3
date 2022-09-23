T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    cnt = 0

    while docs:
        if docs[0] == max(docs):
            docs.pop(0)
            cnt += 1
            if M == 0:
                break
            M -= 1
            continue
        docs.append(docs.pop(0))
        M -= 1
        if M < 0:
            M = len(docs)-1
    print(cnt)
