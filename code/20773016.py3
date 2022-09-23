from sys import stdin
nCase = int(input())
for _ in range(nCase):
    nFile, curIdx = map(int, stdin.readline().split())
    files = list(map(int, stdin.readline().split()))
    priors = [prior for prior in files]
    priors.sort(reverse=True)
    i = 0
    j = 0
    cnt = 0
    while 1:
        if files[i] != priors[j]:
            files.append(files[i])
            if i == curIdx:
                curIdx = len(files) - 1
            i += 1
        elif files[i] == priors[j]:
            cnt += 1
            if i == curIdx:
                break
            i += 1
            j += 1
    print(cnt)
