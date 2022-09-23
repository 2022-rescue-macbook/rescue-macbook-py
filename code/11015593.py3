testnum = int(input())

while testnum > 0:
    N, M = (int(i) for i in input().split())
    imp = [int(i) for i in input().split()]
    idx = [i for i in range(len(imp))]
    count = 1;

    while True:
        cur_idx = idx[0]
        del idx[0]
        cur_imp = imp[0]
        del imp[0]

        if len(imp) > 0 and max(imp) > cur_imp:
            imp.append(cur_imp)
            idx.append(cur_idx)
        else:
            if cur_idx == M:
                print(count)
                break
            count += 1

    testnum -= 1

