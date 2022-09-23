import sys
import math

input = sys.stdin.readline
num = int(input())
for iii in range(num):
    n, m = map(int, input().split())
    key_index = m
    ans = 1
    arr = list(map(int, input().split()))
    while True:
        if arr[0] < max(arr):
            arr.append(arr[0])
            del arr[0]
            if key_index == 0:
                key_index = len(arr) - 1
            else:
                key_index -= 1
        elif arr[0] == max(arr):
            if key_index == 0:
                print(ans)
                break
            del arr[0]
            key_index -= 1
            ans += 1