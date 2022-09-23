from sys import stdin

result = []
T = int(stdin.readline())
for i in range(T):
    N, Prior = map(int, stdin.readline().split())
    K = list(map(int, stdin.readline().split()))

    cnt = 0
    while True:
        while K[0] < max(K):
            K.append(K.pop(0))
            Prior = (N + Prior - 1) % N
        
        K.pop(0)
        cnt += 1
        N -= 1

        if Prior == 0:
            break

        Prior -= 1
    result.append(cnt)

for i in result:
    print(i)