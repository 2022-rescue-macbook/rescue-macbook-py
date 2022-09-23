for i in range(int(input())):
    N, M = map(int,input().split())
    case = [i for i in range(N)]
    arr = list(map(int,input().split()))
    answer = []
    while len(arr) != 0:
        if arr[0] == max(arr):
            answer.append(case[0])
            del arr [0]
            del case [0]
        else:
            arr.append(arr[0])
            case.append(case[0])
            del arr[0]
            del case[0]
    print(answer.index(M)+1)
