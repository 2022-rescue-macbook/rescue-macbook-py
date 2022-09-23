import sys
test_n = int(sys.stdin.readline())
out = []
for _ in range(test_n):
    N , M = map(int, input().split())
    prior = [int(x) for x in input().split()]
    idx = [0 for _ in range(N)]
    idx[M] = 'q'
    cnt = 0
    while prior:
        if prior[0] == max(prior):
            cnt += 1
            if idx[0] == 'q':
                out.append(str(cnt))
                break
            else:
                prior.pop(0)
                idx.pop(0)
        else:
            prior.append(prior.pop(0))
            idx.append(idx.pop(0))
print('\n'.join(out))