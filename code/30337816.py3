t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    while k > -1:
        if a[0] != max(a):
            a.append(a[0])
            a.remove(a[0])
            if k == 0:
                k = len(a) - 1
            else:
                k -= 1
        else:
            a.remove(a[0])
            s += 1
            k -= 1
    print(s)