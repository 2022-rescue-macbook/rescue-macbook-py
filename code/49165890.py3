#1966 - 프린터 큐


n = int(input())
queue = [0 for k in range(n)]
for a in range(n):
    l,k = map(int, input().split())
    L = list(map(int, input().split()))
    i = 0
    M = max(L)
    found = False
    while L[k] != 0:
        while M in L:
            if L[i] == M:
                queue[a] += 1
                L[i] = 0
                if i == k:
                    break
            else:
                i += 1
            i %= l
        M -= 1

for i in queue:
    print(i)