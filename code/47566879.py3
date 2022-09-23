from sys import stdin

def run(q, ind):
    ans = 0
    while len(q) > 0:
        if q[0] == max(q):
            ans += 1
            if ind == 0:
                break
            del q[0]
        else:
            tmp = q[0]
            del q[0]
            q.append(tmp)
        
        ind -= 1
        if ind < 0:
            ind = len(q)-1

    print(ans)

for _ in range(int(stdin.readline())):
    queueLen, queueInd = map(int, stdin.readline().split())
    queue = list(map(int, stdin.readline().split()))

    run(queue, queueInd)