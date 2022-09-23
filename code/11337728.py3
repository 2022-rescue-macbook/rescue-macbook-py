from sys import stdin

class Document:
    def __init__(self, data):
        self.data = data
        self.next = None

class PrinterQueue:
    def __init__(self):
        self.first = None
        self.target = None
        self.final = None

    def append(self, data):
        if self.first == None:
            self.first = Document(data)
            self.final = self.first
        else:
            self.final.next = Document(data)
            self.final = self.final.next

    def setTarget(self):
        self.target = self.final

    def link(self):
        self.final.next = self.first

    def print(self):
        current = self.first
        maxPriority = current
        prev = current
        current = current.next
        while(current != self.first):
            if current.data > maxPriority.data:
                maxPriority = current
                self.final = prev
            prev = current
            current = current.next
        if maxPriority == self.target:
            return 0
        else:
            #print(maxPriority)
            self.final.next = maxPriority.next
            self.first = maxPriority.next
            return maxPriority.data






iter = int(stdin.readline())
for i in range(iter):
    numDocs, numTarget = map(int, stdin.readline().split())
    priorities = list(map(int, stdin.readline().split()))
    pQueue = PrinterQueue()
    for j in range(numDocs):
        pQueue.append(priorities[j])
        if j == numTarget:
            pQueue.setTarget()
    pQueue.link()
    for j in range(numDocs):
        if pQueue.print() == 0:
            print(j+1)
            break



