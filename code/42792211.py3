class queue:

    class Full(Exception):
        pass

    class Empty(Exception):
        pass

    def __init__(self):

        self.start = 0
        self.end = 0
        self.stk = []

    def push(self, x):
        self.stk.append(x)
        self.end += 1

    def pop(self):
        if self.empty():
            raise queue.Empty
        self.start += 1
        return self.stk[self.start - 1]

    def size(self):
        return self.end - self.start

    def empty(self) -> bool:
        return self.size() <= 0

    def front(self):
        if self.empty():
            raise queue.Empty
        return self.stk[self.start]

    def back(self):
        if self.empty():
            raise queue.Empty
        return  self.stk[self.end - 1]

import sys
n = int(sys.stdin.readline())
for i in range(n):
    count = 1
    q = queue()
    N, M = map(int,sys.stdin.readline().split())
    l = list(map(int,sys.stdin.readline().split()))
    answer = (l[M],M)
    for i in range(len(l)):
        q.push((l[i],i))
    l.sort()
    while True:
        if l[-1] == q.front()[0]:
            if q.front() == answer:
                print(count)
                break
            l.pop()
            q.pop()
            count += 1
        else:
            q.push(q.pop())
