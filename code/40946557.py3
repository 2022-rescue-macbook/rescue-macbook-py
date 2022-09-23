for _ in range(int(input())):
    N, M = map(int, input().split())
    t = list(map(int, input().split()))

    st = sorted(t)
    t = [(v, i) for i, v in enumerate(t)]
    p = ans = 0
    mod = len(t)

    while 1:
        v, i = t[p]

        if v == st[-1]:
            ans += 1
            st.pop()

            if i == M:
                print(ans)
                break

        p = (p+1)%mod