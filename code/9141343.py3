t = int(input())
b = []
for i in range(0, t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    while True:
        if a[0] == max(a):
            if m == 0:
                b.append(i+1)
                break
            a.pop(0)
            i += 1
            m -= 1
        else:
            a.append(a.pop(0))
            m -= 1
            if m < 0:
                m += len(a)

for j in b:
    print(j)