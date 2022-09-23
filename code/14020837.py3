# 1966.py
# 2019.07.19

##################### 

class Queue:

    # make data
    def __init__(self):
        self.data = []
        
    # push_list
    def push_list(self, lst):
        for element in lst:
            self.data.append(int(element))

    # push
    def push(self, value):
        self.data.append(value)
            
    # pop
    def pop(self):
        if len(self.data) > 0:
            del self.data[0]
            
    # max
    def max(self):
        return max(self.data)

    # size
    def size(self):
        return len(self.data)


    # empty
    def empty(self):
        if len(self.data) > 0:
            return False
            
        else:
            return True

    # front
    def front(self):
        if len(self.data) > 0:
            return self.data[0]
            
        else:
            return "-1"

#####################

# Get number
num = int(input())

# Queue
que = Queue()

for i in range(num):

    # 첫번째 인자는 size 두번째 인자는 index
    answer1 = input().split(' ')

    # 중요도 list
    answer2 = input().split(' ')

    # 청소
    while(not que.empty()):
        que.pop()
    
    # 중요도 push
    que.push_list(answer2)

    # 인덱스
    index = int(answer1[1])
    number = 1
                      
    while not que.empty():

        if que.front() < que.max():
            que.push(que.front())
            que.pop()

            if index == 0:
                index = que.size()-1
            else:
                index -= 1

        else:
            que.pop()
            
            if index == 0:
                print(number)
                break
            else:
                number += 1
                index -= 1
        
