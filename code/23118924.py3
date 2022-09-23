import sys

sys.setrecursionlimit(2000)
# sys.stdin.readline().rstrip()
# map(int, sys.stdin.readline().rstrip().split())

def main(size, idx):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    visite = [0 for _ in range(size)]
    visite[idx] = 1
    # print(arr)
    cnt = 0
    while True:
        if arr.index(max(arr)) != 0:
            arr.append(arr.pop(0))
            visite.append(visite.pop(0))
        else:
            cnt += 1
            if visite[0] == 1:
                print(cnt)
                break
            else:
                del(arr[0])
                del(visite[0])

if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        size, index = map(int, sys.stdin.readline().rstrip().split())
        # index = input()
        main(size, index)