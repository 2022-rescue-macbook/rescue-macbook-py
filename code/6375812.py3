class printer():
	def __init__(self, printing_queue, k):
		self.queue = printing_queue
		self.order = list(range(len(self.queue)))
		self.counter = 0
		self.search = k
	def print1(self):
		n = self.queue.index(max(self.queue))
		self.queue = self.queue[n:]+self.queue[:n]
		self.order = self.order[n:]+self.order[:n]
		self.counter += 1
		return self.queue.pop(0), self.order.pop(0)
	def finder(self):
		x = (-1, -1)
		while x[1] != self.search:
			x = self.print1()
		return self.counter

for i in range(int(input())):
	n, k = map(int, input().split())
	lst = list(map(int, input().split()))
	tmp = printer(lst, k)
	print(tmp.finder())