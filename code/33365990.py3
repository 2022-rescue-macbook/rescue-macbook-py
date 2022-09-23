test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    document_list = list(map(int, input().split()))
    document_list = [(index, document_list[index]) for index in range(N)]
    sorted_list = sorted(document_list, key=lambda x: x[1], reverse=True)
    count, num = 0, 0

    while num < N+1:
        if document_list[0][1] != sorted_list[num][1]:
            document_list.append(document_list[0])
            del document_list[0]
        else:
            count += 1
            if document_list[0][0] == M:
                print(count)
                break
            document_list.pop(0)
            num += 1