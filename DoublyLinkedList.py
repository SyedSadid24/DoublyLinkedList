class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node 
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def __remove_node(self,node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1

    def remove_all(self,value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.__remove_node(node)
            node = node.next

    def remove(self,value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.__remove_node(node)
                break
            node = node.next

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def count(self,value):
        c = 0
        tmp = self.head
        while tmp is not None:
            if tmp.value == value:
                c += 1
            tmp = tmp.next
        return c

    def extend(self,value):
        for val in value:
            node = Node(val)
            if self.tail is None:
                self.head = node
                self.tail = node
                self.size += 1
            else:
                self.tail.next = node 
                node.prev = self.tail
                self.tail = node
                self.size += 1

    def index(self,value):
        indx = 0
        tmp = self.head
        while tmp is not None:
            if tmp.value == value:
                break
            tmp = tmp.next
            indx += 1
        return indx

    def insert(self,pos,value):
        node = Node(value)
        tmp = self.head
        p = 0
        while tmp is not None:
            if p+1 == pos:
                node.prev = tmp
                node.next = tmp.next
                tmp.next.prev = node
                tmp.next = node
                self.size += 1
            tmp = tmp.next
            p += 1

    def pop(self):
        self.tail = self.tail.prev
        self.tail.next = None

    def reverse(self):
        vals = []
        node = self.tail
        while node is not None:
            vals.append(node.value)
            node = node.prev
        array = [x for x in vals]
        DoubleLinkedList.clear(self)
        for arr in array:
            DoubleLinkedList.append(self,arr)

    def sort(self):
        vals = []
        node = self.tail
        while node is not None:
            vals.append(node.value)
            node = node.prev
        array = [x for x in vals]
        DoubleLinkedList.clear(self)
        array = sorted(array)
        for a in array:
            DoubleLinkedList.append(self,a)

    def len(self):
        return self.size
        
    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.value)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"