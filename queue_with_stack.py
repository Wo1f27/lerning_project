class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, elem):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        self.s1.append(elem)
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            raise Exception('Cannot pop from empty queue')
        return self.s1.pop()

    def size(self):
        return len(self.s1)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    print(queue.size())
    for i in range(queue.size()):
        print(queue.dequeue())
