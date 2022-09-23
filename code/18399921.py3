import sys


def isHigher(arr):
    if len(arr) == 1:
        return False
    piv = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][1] > piv:
            return True
    return False


t = int(sys.stdin.readline())
for _ in range(t):

    n, m = map(int, sys.stdin.readline().split())
    papers = list(map(int, sys.stdin.readline().split()))
    enum = list(enumerate(papers))
    count = 0
    while True:
        if isHigher(enum):
            temp = enum[0]
            enum.pop(0)
            enum.append(temp)

        elif not isHigher(enum):
            if enum[0][0] == m:
                count += 1
                print(count)
                break
            enum.pop(0)
            count += 1
