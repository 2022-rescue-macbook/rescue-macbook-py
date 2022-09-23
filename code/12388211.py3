for _ in range(int(input())):
    N, M = map(int,input().split())
    docs = list(map(int, input().split()))

    cnt = 0

    while True:
        if M == 0:
            if docs[M] < max(docs):
                docs.append(docs[M])
                del docs[0]
                M = len(docs) - 1
            else : #docs[M] = max(docs)
                cnt+=1
                break
        else: #M != 0
            if docs[0] < max(docs):
                docs.append(docs[0])
                del docs[0]
                M -= 1
            else : #docs[0] = max(docs)
                del docs[0]
                cnt+=1
                M -= 1
    print(cnt)