test_case = int(input())

for _ in range(test_case):
    # 문서 수, 궁금한 문서 위치
    n, m = list(map(int, input().split()))
    # 문서 중요도
    docs = list(map(int, input().split()))

    ##### 인덱스 리스트 만드는게 인상적
    idx = [0] * len(docs)

    idx[m] = 'target'
    answer = 0

    while True:
        if docs[0] == max(docs):
            docs.pop(0)
            answer += 1
            if idx.pop(0) == 'target':
                print(answer)
                break
        else:
            docs.append(docs.pop(0))
            idx.append(idx.pop(0))