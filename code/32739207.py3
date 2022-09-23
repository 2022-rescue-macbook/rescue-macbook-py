from sys import stdin, stdout

def IN():
    return stdin.readline().rstrip()
def OUT(d):
    stdout.write("%d\n" % d)

T = int(IN())

for i in range(T):
    N, M = map(int, IN().split())
    queue = list(map(int, IN().split()))
    maxlist = sorted(queue)
    ans = 0

    while True:
        if queue[0] == maxlist[-1]:
            ans += 1
            if M == 0:
                OUT(ans)
                break
            del(queue[0])
            del(maxlist[-1])
            N -= 1
            M -= 1
            continue

        queue.append(queue.pop(0))
        M -= 1

        if M < 0:
            M = N-1