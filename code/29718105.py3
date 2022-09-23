import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PrintQue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_first_priority(self):
        front_data = self.front.data
        temp = self.front.next
        while temp:
            if front_data < temp.data:
                return False
            temp = temp.next
        return True

    def enqueue(self, data):
        new_node = Node(data)
        if self.front:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = new_node
            self.rear = new_node

    def node_to_dequeue(self):
        if self.front:
            while not self.is_first_priority():
                node = self.front
                self.front = self.front.next
                node.next = None

                self.rear.next = node
                self.rear = self.rear.next

            node_to_delete = self.front
            self.front = self.front.next
            return node_to_delete

    def search_mth_node(self, m):
        node_pointer = self.front
        count = 0
        while count < m:
            node_pointer = node_pointer.next
            count = count + 1
        return node_pointer

    def dequeue_counter(self, m):
        count = 0
        mth_node = self.search_mth_node(m)
        while self.front is not None:
            node_to_delete = self.node_to_dequeue()
            count += 1
            if node_to_delete is mth_node:
                break

        return count


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    print_queue =PrintQue()

    N, M = map(int, sys.stdin.readline().split())
    documents = list(map(int, sys.stdin.readline().split()))
    for x in documents:
        print_queue.enqueue(x)

    print(print_queue.dequeue_counter(M))