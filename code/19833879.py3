import sys

num = input()
inputs = sys.stdin.readlines()
args = list(map(str.split, inputs))
args = [list(map(int, x)) for x in args]

for x in range(int(len(args) / 2)):
    count = 0
    idx = args[x * 2][1]
    i = 0
    while (True):
        if args[x * 2 + 1][0] >= max(args[x * 2 + 1]):
            count += 1
            if idx == 0:
                print(count)
                break
            args[x * 2 + 1].pop(0)
            idx -= 1
        else:
            if idx == 0:
                idx = len(args[x * 2 + 1]) - 1
            else:
                idx -= 1
            args[x * 2 + 1].append(args[x * 2 + 1].pop(0))
        i += 1
