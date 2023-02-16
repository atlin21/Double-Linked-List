class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def push(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None

    def peek(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
dllist = DLL()
dllist.push(12)
dllist.push(133)
dllist.append(17)
dllist.append(34)
dllist.append(2)
dllist.peek()
