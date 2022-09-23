class Queue:
    def __init__(self):
        self.queue = []
    def push(self, num):
        self.queue.append(num)
    def pop(self):
        return self.queue.pop(0) if len(self.queue) != 0 else -1
    def size(self):
        return len(self.queue)
    def empty(self):
        return 1 if self.size() == 0 else 0
    def front(self):
        return self.queue[0] if self.size() != 0 else -1
    def back(self):
        return self.queue[-1] if self.size() != 0 else -1
    def max(self):
        return max(self.queue)
numbers = int(input())

for _ in range(numbers):
    count = 0
    inp = list(map(int, input().split()))
    inp2 = list(map(int, input().split()))
    N = inp[0]
    index = inp[1]
    queue = Queue()
    queue_document = Queue()
    found = False
    for i in range(N):
        queue.push(inp2[i])
        queue_document.push(i)
    while(True):
        max_val = queue.max()
        current_priority = queue.pop()
        current_document = queue_document.pop()
        if (current_priority >= max_val):
            count += 1
            if(current_document == index):
                print(count)
                found = True
        else:
            queue.push(current_priority)
            queue_document.push(current_document)
        if found is True:
            break

