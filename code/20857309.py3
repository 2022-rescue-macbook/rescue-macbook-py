import sys
read = sys.stdin.readline


class queue:
    def __init__(self):
        self.arr = []
        self.count = 0
    
    def push(self, num):
        self.arr.append(num)
    
    def pop(self):
        if self.count < len(self.arr):
            self.count += 1
            return self.arr[self.count -1]
        else:
            return False
    
    def size(self):
        return len(self.arr) - self.count
    
    def reset(self):
        self.arr = []
        self.count = 0
    
    def maxq(self):
        return max(self.arr[self.count:])

num = int(read())    
que = queue()
for _ in range(num):
    n, pos = map(int, read().split())
    arr = list(map(int, read().split()))
    que.reset()
    for i in arr:
        que.push(i)
    count = 0
    while(1):
        if que.maxq() == que.arr[que.count]:
            count += 1
            if pos == que.count:
                print(count)
                break
            que.pop()
        else:
            if pos == que.count:
                pos = que.count + que.size()
            que.push(que.pop())