import sys

def printerque(n, m, arr):
    count = 0
    while len(arr)!=0:
        if(max(arr)>arr[0]):
            arr.append(arr[0])
            del arr[0]
            m = (m+len(arr)-1)%len(arr)
        elif(max(arr)==arr[0]):
            n -= 1
            count += 1
            if(m==0):
                return count
            else:
                m = (m + len(arr) - 1) % len(arr)
            del arr[0]

    return count




if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    for i in range(n):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        y = printerque(n, m, arr)
        print(y)