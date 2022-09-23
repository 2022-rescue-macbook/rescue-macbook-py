tk = int(input())
result = []

for i in range(tk):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))

    impLoc = [0]*N
    impLoc[M] = 'x'
    count = 0

    while True:
        if imp[0] == max(imp):
            count += 1

            if impLoc[0] == 'x':
                result.append(count)
                break

            imp.pop(0)
            impLoc.pop(0)
        else:
            imp.append(imp.pop(0))
            impLoc.append(impLoc.pop(0))

print('\n'.join(map(str, result)))