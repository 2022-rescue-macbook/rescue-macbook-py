T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    ans = 1

    while len(li) != 0:
        ma = max(li)
        if ma == li[0]:
            if M == 0:
                break
            else:
                del li[0]
                ans += 1
        else:
            li.append(li.pop(0))
            if M == 0:
                M = len(li)
        M -= 1

    print(ans)
