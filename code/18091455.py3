import sys

class Queue:
    def __init__(self, arr):
        self.que = []
        for i in range(len(arr)) :
            self.que.append((i, arr[i]))

    def enque(self, data : list):
        self.que.append(data)

    def deque(self):
        ret = self.que[0]
        self.que = self.que[1:]
        return ret

    def isEmpty(self):
        return len(self.que) == 0

    def isFirstBiggest(self):
        if len(self.que) == 1 :
            return True
        else :
            for i in range(1, len(self.que)) :
                if self.que[0][1] < self.que[i][1] :
                    return False
            return True

T = int(sys.stdin.readline())
testCase = []
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    testCase.append([M] + list(map(int, sys.stdin.readline().split())))

for case in testCase:
    # each tuple has tuple pair : (documentID, importance)
    N, queue = case[0], Queue(case[1:])
    printed = []

    while not queue.isEmpty():
        if queue.isFirstBiggest() :
            printed.append(queue.deque())
        else :
            queue.enque(queue.deque())

        if len(printed) != 0 and printed[-1][0] == N:
            print(len(printed))
            break