t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    printer = [[i, prior[i]] for i in range(n)]

    ans = 0
    while True:
        p = max(prior)
        cur = printer.pop(0)

        if p == cur[1]:
            prior.remove(p)
            ans += 1

            if m == cur[0]:
                print(ans)
                break
        
        else:
            printer.append(cur)