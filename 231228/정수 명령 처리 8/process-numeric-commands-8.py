class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        else: 
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
        
        self.node_num += 1

    def push_back(self,new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

        else:
            self.head = new_node
            self.tail = new_node
            new_node.next = None

        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print("List is empty")

        elif self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.node_num = 0
            print(temp.data)

        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            print(temp.data)

    def pop_back(self):
        if self.tail == None:
            print("List is empty")

        elif self.tail.prev == None:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            print(temp.data)

        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            print(temp.data)

    def size(self):
       print(self.node_num)


    def empty(self):
        return self.node_num == 0

    def front(self):
        if self.head == None:
            print("List is empty")
        else:
            print(self.head.data)

    def back(self):
        if self.tail == None:
            print("List is empty")
        else:
            print(self.tail.data)


doubleLinkedList = DoublyLinkedList()

n = int(input())
for _ in range(n):
    arr = input().split()
    
    if arr[0] == "push_back":
        doubleLinkedList.push_back(int(arr[1]))
    elif arr[0] == "push_front":
        doubleLinkedList.push_front(int(arr[1]))
    elif arr[0] == "pop_front":
        doubleLinkedList.pop_front()
    elif arr[0] == "pop_back":
        doubleLinkedList.pop_back()
    elif arr[0] == "front":
        doubleLinkedList.front()
    elif arr[0] == "back":
        doubleLinkedList.back()
    elif arr[0] == "size":
        doubleLinkedList.size()
    elif arr[0] == "empty":
        if doubleLinkedList.empty() == True:
            print(0)
        else: 
            print(1)