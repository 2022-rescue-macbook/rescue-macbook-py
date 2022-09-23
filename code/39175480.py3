import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    dic = {}
    dic[1] = 0
    dic[2] = 0
    dic[3] = 0
    dic[4] = 0
    dic[5] = 0
    dic[6] = 0
    dic[7] = 0
    dic[8] = 0
    dic[9] = 0
    for n in li:
        dic[n] += 1
    myP = li[M]
    count = 0
    idx = 0
    for j in range(10-myP):
        while (dic[9-j] > 0):
            if (li[idx] == 9-j):
                count += 1
                dic[9-j] -= 1
                if (idx == M):
                    break
            idx += 1
            if (idx == N):
                idx = 0
    print(count)