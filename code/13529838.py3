from sys import stdin

class Queue(list):
    push = list.append

    def pop(self):
        if self:
            temp = self[0]
            del self[0]
            return temp
        else:
            return -1

    def front(self):
        return self[0] if self else -1

    def back(self):
        return self[-1] if self else -1

    def size(self):
        return len(self)

    def empty(self):
        return 0 if self else 1

case = int(stdin.readline())

for i in range(case):
    N, M = map(int, stdin.readline().split())
    arr = Queue(map(int, stdin.readline().split()))
    cnt = 0
    while True:
        max_ = max(arr)
        if arr[0] < max_:
            arr.push(arr.pop())
            if M == 0:
                M = len(arr)-1
            else:
                M -= 1
        else:
            arr.pop()
            cnt += 1
            if M == 0:
                break
            M -= 1
    print(cnt)