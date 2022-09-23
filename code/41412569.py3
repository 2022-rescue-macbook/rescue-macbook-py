import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    tmp = list(map(int,input().split()))
    priority = [(idx,val) for idx,val in enumerate(tmp)]
    ans = 0
    
    while True:
        res = priority.pop(0)
        if any(res[1]<q[1] for q in priority):
            priority.append(res)
        else:
            ans += 1
            if res[0] == m:
                print(ans)
                break