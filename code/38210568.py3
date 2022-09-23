import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, i = map(int, input().split())
    importance = list(map(int, input().split()))
    index_checking = [0 for i in range(n)]
    index_checking[i] = 1
    cnt = 0
    while 1:
        if importance[0] == max(importance):
            cnt += 1
            if index_checking[0] == 1:
                print(cnt)
                break
            else:
                del index_checking[0]
                del importance[0]
        else:
            index_checking.append(index_checking[0])
            del index_checking[0]
            importance.append(importance[0])
            del importance[0]