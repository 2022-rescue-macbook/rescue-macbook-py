from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    priorities = list(map(int, stdin.readline().split()))
    isPrinted = [False for _ in range(n)]
    maxPriorities = sorted(priorities.copy())[::-1]
    i = 0
    rank = 0
    while rank < n:
        if isPrinted[i % n] == False and priorities[i % n] == maxPriorities[rank]:
            rank += 1
            if i % n == k:
                print(rank)
                break
            else:
                isPrinted[i % n] = True
        i += 1