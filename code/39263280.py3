import sys


def solution():
    a = int(sys.stdin.readline())
    for i in range(a):
        m, n = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        answer = 0

        while True:
            if n == 0: #n이 제일 앞에 있을 때
                if arr[0] == max(arr): #우선순위가 짱일 때
                    answer += 1
                    break
                else: # 우선순위가 밀릴 때
                    n = len(arr)-1
                    arr.append(arr.pop(0))
            else: #제일 앞이 아닐 때
                if arr[0] == max(arr): # 제일 앞이 짱일 때
                    answer += 1
                    arr.pop(0)
                    n -= 1
                else: #제일 앞이 찐따일 때
                    arr.append(arr.pop(0))
                    n -= 1

        print(answer)




if __name__ == '__main__':
    solution()