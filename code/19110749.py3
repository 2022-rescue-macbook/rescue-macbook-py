import sys
input = sys.stdin.readline

def isMax(q, Q):
    for i in range(0, len(Q)):
        if q < Q[i]:
            return False
    return True


def priority(Q, m):
    search = m
    cnt = 1
    while Q:
        if isMax(Q[0], Q):
            if search == 0: return cnt
            search -= 1
            cnt += 1
            del Q[0]
        else:
            if search == 0: search = len(Q) - 1
            else: search -= 1
            Q.append(Q[0])
            del Q[0]



def main():
    n, m = map(int, input().split())
    Q = list(map(int, input().split()))
    print(priority(Q, m))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        main()