TT = int(input())

for _ in range(TT):
    N, M = map(int, input().split())
    if N == 1:
        importance = [int(input())]
    else :
        importance = list(map(int, input().split()))
    documents = [i for i in range(N)]
    importance_dict = {}
    for key, value in enumerate(importance):
        importance_dict[key] = value

    print_list = []
    max_importance = max(importance)
    front = documents[0]

    while documents:
        front = documents[0]
        if max_importance == importance_dict[front]:
            documents.remove(front)
            print_list.append(front)
            importance.remove(max_importance)
            if len(importance):
                max_importance = max(importance)
            else:
                break
        else:
            documents.remove(front)
            documents.append(front)

    for idx, i in enumerate(print_list):
        if i == M:
            print(idx + 1)
