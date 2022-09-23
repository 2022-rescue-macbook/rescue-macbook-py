T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    docs = list(map(int, input().split()))

    docs_idx = [ _ for _ in range(N)]
    maxV = max(docs)
    cnt = 1

    while docs:
        doc = docs.pop(0)
        idx = docs_idx.pop(0)
        if doc == maxV and idx == M:
            print(cnt)
            break

        if maxV == doc:
            cnt += 1
            maxV = max(docs)
        else:
            docs.append(doc)
            docs_idx.append(idx)