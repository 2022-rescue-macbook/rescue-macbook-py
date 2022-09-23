for tc in range(int(input())):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))
    mission = sorted(docs, reverse=True)
    cnt = 0
    while cnt < N:
        for i in range(N):
            if docs[i] == mission[cnt]:
                cnt += 1
                if i == M:
                    break
        else:
            continue
        break
    print(cnt)