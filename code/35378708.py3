import sys
n = int(input())

def f(x):
    X = int(x)
    s[X-1] += 1
    return X

for _ in range(n):
    n, m = map(int, sys.stdin.readline().rstrip('\n').split())
    s = [0] * 10
    l = list(map(f, sys.stdin.readline().rstrip('\n').split()))

    start = 0
    end = n

    res = 0
    t = m
    #print('s : ',s)
    while True:
        if sum(s[l[start]:]) > 0:
            l.append(l[start])

            if start == t:
                t = end

            start += 1
            end += 1
        else:
            s[l[start]-1] -= 1
            res += 1

            if t == start:
                break
            start += 1
        #print('s : ',s)
        #print('l : ',l)
        #print('start, end : ',start,end)
    #print('res : ', res)
    print(res)
