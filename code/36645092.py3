from sys import stdin

def prq(a, b):
    
    val = list(map(int, stdin.readline().split()))
    cnt = list(i for i in range(a))
    ans = 1

    for _ in range(n):
        while val[0] != max(val):
            val.append(val[0])
            del val[0]            
            cnt.append(cnt[0])
            del cnt[0]

        if cnt[0] == b:
            print(ans)
            break

        del val[0]
        del cnt[0]
        ans += 1

n = int(stdin.readline())

for _ in range(n):
    n, m = map(int, stdin.readline().split())
    prq(n, m)
