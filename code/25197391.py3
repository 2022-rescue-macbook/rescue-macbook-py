t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    check = [0] * n
    check[m] = 1
    count = 0
    while True:
        if n == 1:
            print(1)
            break
        if max(q) != q[0]:
            q.append(q[0])
            del(q[0])
            if check[0] != 1:
                check.append(check[0])
                del(check[0])
            else:
                check.append(check[0])
                del(check[0])
        elif max(q) == q[0]:
            del(q[0])
            if check[0] != 1:
                del(check[0])
                count += 1
            elif check[0] == 1:
                count += 1
                print(count)
                break