class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        res = ''
        while node is not None:
            res += (' --> ' if res else '') + str(node)
            node = node.next
        return res

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)

    def create_cycle_list(self):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        if cur.next is None:
            cur.next = self.head

    def search(self, target):
        cur = self.head
        while cur.next:
            if cur.value == target:
                return True
            else:
                return False

    def remove(self, target):
        if self.head is None:
            return
        if self.head == target:
            self.head = self.head.next
            return
        cur = self.head
        prev = None
        while cur:
            if cur.value == target:
                prev.next = cur.next
            prev = cur
            cur = cur.next

    def reverse_list(self):
        cur = self.head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True and 'Yes cycle'
            except:
                return False, 'No cycle'


if __name__ == '__main__':

    a_list = LinkedList()
    a_list.append(1)
    a_list.append(2)
    a_list.append(3)
    a_list.append(5)
    print(a_list)
    a_list.remove(2)
    print(a_list)
    a_list.reverse_list()
    print(a_list)
    print(a_list.detect_cycle())
