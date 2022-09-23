for i in range(int(input())):
    order = []
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = [0] * n
    idx[m] = 1
    count = 0

    while 1:
        if imp[0] == max(imp):
            count += 1
            if idx[0] == 1:
                print(count)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))