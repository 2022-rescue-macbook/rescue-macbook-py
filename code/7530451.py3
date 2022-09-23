class Queue:
    def __init__(self):
        self.queue = []

    def init(self, l):
        self.queue = l

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1

    def min(self):
        return min(self.queue)

    def max(self):
        max1 = -min(self.queue)
        max2 = max(self.queue)
        if max1 > max2:
            return max1
        else:
            return max2

    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return False
        else:
            return True

n = int(input())

for i in range(n):
    q = Queue()
    target = list(map(int, input().split()))[1]
    li = list(map(int, input().split()))
    li[target] = -li[target]

    q.init(li)
    order = 0
    maxval = q.max()
    if maxval < 0:
        maxval = -maxval

    while True:
        head = q.pop()
        if head < 0 and maxval == -head:
            order += 1
            break
        elif maxval == head:
            order += 1
            maxval = q.max()
        else:
            q.push(head)

    print(order)
