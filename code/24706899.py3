a = int(input())
for i in range(a) :
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    ll = [False] * n
    ll[m] = True
    p = 1
    while True :
        k = l.index(max(l))
        if k != 0 :
            l = l[k:]+l[:k]
            ll = ll[k:] + ll[:k]
        l.pop(0)
        if ll.pop(0) :
            print(p)
            break
        p += 1