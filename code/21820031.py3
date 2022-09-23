case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    temp = [0 for _ in range(n)]
    temp[m] = 1
    cnt = 0

    while imp:
        if imp[0] == max(imp):
            cnt += 1
            if temp[0] == 1:
                print(cnt)
                break
            else:
                imp.pop(0)
                temp.pop(0)
        else:
            imp.append(imp[0])
            temp.append(temp[0])
            del(imp[0])
            del(temp[0])
