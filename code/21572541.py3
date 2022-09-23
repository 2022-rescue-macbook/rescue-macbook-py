import sys


class Node:
    def __init__(self, idx, val, prev_node=None, next_node=None):
        self.idx = idx
        self.val = val
        self.prev = prev_node
        if prev_node is not None:
            prev_node.set_next(self)
        self.next = next_node
        if next_node is not None:
            next_node.set_prev(self)

    def set_prev(self, prev_node):
        if self.prev is not None:
            self.prev.next = None
        if prev_node.next is not None:
            prev_node.next.prev = None

        self.prev = prev_node
        prev_node.next = self

    def set_next(self, next_node):
        if self.next is not None:
            self.next.prev = None
        if next_node.prev is not None:
            next_node.prev.next = None

        self.next = next_node
        next_node.prev = self


for test in range(int(sys.stdin.readline())):
    n, m = list(map(int, sys.stdin.readline().split()))
    priority = list(map(int, sys.stdin.readline().split()))

    nodes = [Node(i, priority[i]) for i in range(n)]
    for i in range(1, n):
        nodes[i].set_prev(nodes[i-1])

    start = Node(-1, 0, None, nodes[0])
    end = Node(-1, 0, nodes[n-1], None)

    print_num = 0
    while True:
        # Find first node with maximum value
        max_node = start
        cur_node = start.next
        while cur_node != end:
            if cur_node.val > max_node.val:
                max_node = cur_node

            cur_node = cur_node.next

        # Print max_node, while ignoring other nodes that were before that
        start.next.set_prev(end.prev)
        max_node.next.set_prev(start)
        max_node.prev.set_next(end)

        print_num += 1

        if max_node.idx == m:
            break

    print(print_num)
