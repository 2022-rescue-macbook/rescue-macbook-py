import sys
input = sys.stdin.readline
test = int(input())
for _  in range(test):
    a, b = map(int, input().split())
    imp = list(map(int, input().split()))
    interested = [0]*a
    interested[b] = 1
    ord = 0
    while True:
        if imp[0] == max(imp):
            ord += 1
            if interested[0]:
                print(ord)
                break
            else:
                del interested[0]
                del imp[0]
        else:
            interested.append(interested[0])
            imp.append(imp[0])
            del interested[0]
            del imp[0]
    