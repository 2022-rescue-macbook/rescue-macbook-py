cases = []

class Doc:
    def __init__(self, i):
        self.important = i
        self.target = False

class Docs:
    def __init__(self):
        self.docs = []
        self.printCnt = 0

    def addDocs(self, doc):
        self.docs.append(doc)

    def setTarget(self, t):
        self.docs[t].target = True

    def print(self):
        t = self.docs.pop(0)
        if self.isMax(t):
            self.printCnt += 1
            if t.target:
                return True
            return False
        else:
            self.docs.append(t)

    def isMax(self, t):
        for i in self.docs:
            if i.important > t.important:
                return False
        return True

for _ in range(int(input())):
    N, M = map(int, input().split())
    d = list(map(int, input().split()))
    docs = Docs()
    for i in d:
        docs.addDocs(Doc(i))
    docs.setTarget(M)
    cases.append(docs)

for docs in cases:
    while True:
        if docs.print():
            print(docs.printCnt)
            break