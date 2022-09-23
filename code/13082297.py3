class ListNode:
    def __init__(self, data=0):
        self._data = data
        self._next = None
        self._prev = None

    def __repr__(self):
        return "ListNode (data: %s)" % str(self.data())

    def data(self):
        return self._data
    
    def next(self):
        return self._next

    def prev(self):
        return self._prev

    def setdata(self, data):
        self._data = data

    def setnext(self, next):
        self._next = next

    def setprev(self, prev):
        self._prev = prev
    

class Deque:
    def __init__(self):
        self._last = None
        self._count = 0

    def __repr__(self):
        if self.empty():
            return "[]"

        o="["
        o+="%s" % str(self.first().data())
        cur = self.first().next()
        while cur != self.first():
            o+=",%s" % cur.data()
            cur = cur.next()
        o+="]"
        return o

    def first(self):
        if self._last == None:
            return None
        return self.last().next()

    def last(self):
        return self._last
    
    def pushfront(self, data):
        self._count += 1
        if self._last == None:
            new = ListNode(data)
            new.setnext(new)
            new.setprev(new)
            self._last = new
            return

        new = ListNode(data)
        new.setnext(self.first())
        new.setprev(self.last())
        self.first().setprev(new)
        self.last().setnext(new)

        

    def pushback(self, data):
        self._count += 1
        if self._last == None:
            new = ListNode(data)
            new.setnext(new)
            new.setprev(new)
            self._last = new
            return

        new = ListNode(data)
        new.setnext(self.first())
        new.setprev(self.last())
        self.first().setprev(new)
        self.last().setnext(new)
        
        self._last = new
        

    def popfront(self):
        
        if self.size() == 1:
            old = self.last()
            self._last = None
            self._count -= 1
            return old.data()

        first = self.first()
        first.next().setprev(self.last())
        self.last().setnext(first.next())

        self._count -= 1
        
        return first.data()
        

    def popback(self):
        
        if self.size() == 1:
            old = self.last()
            self._last = None
            self._count -= 1
            return old.data()

        

        self._last = self.last().prev()
        
        return self.popfront()
        


    def size(self):
        return self._count

    def empty(self):
        return self.size() == 0

    def shiftleft(self, count=1):
        for _ in range(count):
            self._last = self.last().next()

    def shiftright(self, count=1):
        for _ in range(count):
            self._last = self.last().prev()

    def findtoright(self, target):
        cnt = 0
        cur = self.first()
        while cur.data()[1] != target:
            cnt+=1
            cur = cur.next()
        return (cnt, cur)


    def setfirst(self, first):
        self._last = first.prev()
    



t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    pri = [int(x) for x in input().split()]

    deque = Deque()
    for i in range(len(pri)):
        deque.pushback((i, pri[i]))
    
    pri.sort(reverse=True)
    cnt = 0
    for i in pri:
        cnt += 1
        s, node = deque.findtoright(i)
        if node.data()[0] == m:
            break
        deque.setfirst(node)
        deque.popfront()
    print(cnt)

