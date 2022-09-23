import sys
input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split(' '))
    c = list(map(int, input().split(' ')))
    d = [0 for j in range(a)]
    d[b] = 'e'

    count = 0
    while True:
        if c[0] == max(c):
            count += 1
            if d[0] == 'e':
                print(count)
                break
            else:
                c.pop(0)
                d.pop(0)
        else:
            c.append(c.pop(0))
            d.append(d.pop(0))