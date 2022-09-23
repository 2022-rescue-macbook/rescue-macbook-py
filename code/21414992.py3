import sys

def printer():
    n, m = sys.stdin.readline().split()
    n = int(n)
    m = int(m)

    q = []
    s = sys.stdin.readline().split()
    for i in range(n):
        q.append((int(s[i]), i))

    cnt = 1
    while len(q) > 0:
        k = max(q)
        #print(q)
        #print(k)
        if k[0] == q[0][0]:
            if q[0][1] == m:
                return cnt
            cnt += 1
            del(q[0])
        else:
            q.append(q.pop(0))


tc = int(sys.stdin.readline())

for i in range(tc):
    print(printer())
            
