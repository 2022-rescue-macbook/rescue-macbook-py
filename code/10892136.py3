for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [*map(int, input().split())]
    order = 1

    while l:
        first = l.index(max(l))
        if first == 0:
            if m == 0:
                print(order)
                break
            else:
                l.pop(0)
                order += 1
        else:
            l.append(l.pop(0))
        m = (m - 1) % len(l)
