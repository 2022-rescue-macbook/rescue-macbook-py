import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, i = [*map(int,sys.stdin.readline().split())]
    priors = [*map(int,sys.stdin.readline().split())]
    tags = list(range(n))
    count = 0
    while 1:
        count += 1
        j = priors.index(max(priors))
        if tags[j]==i: print(count); break
        priors = priors[j:]+priors[:j]; del priors[0]
        tags = tags[j:]+tags[:j]; del tags[0]