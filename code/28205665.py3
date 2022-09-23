class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class PrintQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.target = None
        self.priorityArr = [0] * 10
        
    def addToTail(self, node, isTarget=False):
        if self.tail is not None:    
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
        
        self.priorityArr[node.data] += 1
        if isTarget:
            self.target = node
    
    def removeFromHead(self):
        node = self.head
        self.head = self.head.next
        self.priorityArr[node.data] -= 1
        return node
                
    def isLargePriorityExist(self, priority):
        for i in range(priority + 1, 10):
            if self.priorityArr[i] > 0:
                return True
        return False
    
    def rearrange(self):
        while self.isLargePriorityExist(self.head.data):
            self.addToTail(self.removeFromHead())
        
Cases = int(input())
answers = []
for TC in range(Cases):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))

    Queue = PrintQueue()
    for i in range(len(documents)):
        Queue.addToTail(Node(documents[i]), i == M)
    
    answer = 0
    while True:
        Queue.rearrange()
        printed = Queue.removeFromHead()
        answer += 1
        if printed == Queue.target:
            break

    answers.append(answer)

for ans in answers:
    print(ans)