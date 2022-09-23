import sys

class Queue:
    def __init__(self):
        self.items = []
        self.front_Index = 0
    def push(self, val, i):
        x = []
        x.append(val); x.append(i)
        self.items.append(x)
    def pop(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            return -1
        else:
            x = self.items[self.front_Index][0]
            self.front_Index += 1
            return x
    def front(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            return -1
        else:
            x, y = self.items[self.front_Index][0], self.items[self.front_Index][1] 
            return x, y
    def size(self):
        return len(self.items) - self.front_Index
    def empty(self):
        return self.size() == 0


n = int(input())

for i in range(n):
    N, M = map(int,sys.stdin.readline().split())
    input_list = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    imp_list = []
    my_Queue = Queue()
    
    for i in range(len(input_list)):
        my_Queue.push(input_list[i], i)
        val = my_Queue.items[i][0]
        imp_list.append(val)
    
    imp_list.sort()

    while not(my_Queue.empty()): #my_Queue.size() == False -> 이렇게 되면 틀림 !
        x, y = my_Queue.items[M]
        val, index = my_Queue.front()
        last = len(imp_list) - 1
        most_imp = imp_list[last]
        # val <= most_impt
        if val < most_imp:
            my_Queue.push(my_Queue.pop(), index)
        else:
            if val == x and index == y:
                my_Queue.pop()
                cnt += 1
                print(cnt)
                break
            else:
                my_Queue.pop()
                cnt += 1
                imp_list.pop()