import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int ,input().split())
    array = list(map(int, input().split()))
    count = 0
    if len(array) == 1:
        print(1)
    else:
        index = b
        while 1:
            if index == 0:
                if array[index] == max(array):
                    count += 1
                    print(count)
                    break
                else:
                    c = array.pop(0)
                    array.append(c)
                    index = len(array) - 1
            else:
                if array[0] == max(array):
                    array.pop(0)
                    index -= 1
                    count += 1
                else:
                    c = array.pop(0) 
                    array.append(c)
                    index -= 1