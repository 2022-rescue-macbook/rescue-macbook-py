class printQ:
    def __init__(self):
        self.PQ = []
        self.size = 0
        self.target = 0
        self.count = 0
        
    def initialize(self, size, target):
        self.PQ = list(map(int, input().split(" ")))
        self.size = size
        self.target = target

    def printing(self):
        while True:
            if self.attemp(self.size): #print success
                self.count = self.count+1
                if self.target == 0:
                    return self.count
                else :
                    self.size = self.size-1
                    self.target = self.target-1
            else: #print fail
                self.target = (self.target - 1 + self.size) % self.size
            
            

        
    def attemp(self, size):
        for i in range(1,size):
            if self.PQ[0] < self.PQ[i]:
                self.PQ.append( self.PQ.pop(0) )
                return False
        self.PQ.pop(0)
        return True



N = int(input())

for i in range(N):
    printer = printQ()
    N,M = map(int, input().split(" "))
    printer.initialize(N,M)
    print(printer.printing())
