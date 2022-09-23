import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x, i = map(int, sys.stdin.readline().split()) # x는 큐의 길이, i는 인덱싱할 값의 위치
    a = list(map(int, sys.stdin.readline().split())) # a는 큐
    count = 0
    t = max(a)
    while True:
        if i == 0:
            if a[0] == t or a[0] == max(a):
                count += 1
                print(count)
                break
            else:
                a.append(a.pop(0))
                i = i+x-1
        elif a[0] == max(a):
            t = a.pop(0)
            i -= 1
            count += 1
            x -= 1
        else:
            a.append(a.pop(0))
            i -= 1