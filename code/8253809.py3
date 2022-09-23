import sys
read = sys.stdin.readline

class queue:
    def __init__(self):
        self.arr = []
        self.length = 0

    def push(self, x, y):
        self.arr += [[x, y]]
        self.length += 1

    def pop(self):
        if self.length == 0:
            return -1
        else:
            max1, mem, change = self.arr[0][0], 0, 0
            for i, j in enumerate(self.arr):
                if(j[0] > max1):
                    mem = i
                    max1 = j[0]
                    change = 1
            self.length -= 1 
            if change == 1:
                for _ in range(mem):
                    ack = self.arr.pop(0)
                    self.push(ack[0], ack[1])
                return self.arr.pop(0)
            return self.arr.pop(mem)


    def size(self):
        print(self.length)

    def empty(self):
        if self.length:
            print(0)

        else:
            print(1)

    def front(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.arr[0])

    def back(self):
        if self.length == 0:
            print(-1)
        else:
            print(self.arr[-1])

for _ in range(int(read())):
    queue1 = queue()
    a, b = map(int, read().split())
    lst = list(map(int, read().split()))
    for i, j in enumerate(lst):
        if i == b:
            queue1.push(j, 1)
        else:
            queue1.push(j, 0)
    cnt = 0
    while 1:
        if queue1.pop()[1] == 1:
            cnt += 1
            break
        else:
            cnt += 1
    print(cnt)