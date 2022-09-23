import sys

input = sys.stdin.readline

def main() :
    testNum = int(input())
    for _ in range(testNum):
        N, M = map(int, input().split())
        inputs = list(map(int, input().split()))
        Queue = [(inputs[n], n) for n in range(N)]
        target = Queue[M]
        print(Printer(Queue, target))

def Printer(Queue, target):
    def QCheck(Queue):
        for doc in Queue:
            if Queue[0][0] < doc[0]:
                return False
        return True

    cnt = 1
    while(Queue):
        if QCheck(Queue) == True:
            if Queue[0] == target:
                return cnt
            Queue.pop(0)
            cnt += 1
        else:
            Queue.append(Queue.pop(0))

if __name__ == '__main__':
    main()