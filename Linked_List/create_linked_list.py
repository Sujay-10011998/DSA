class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
        
        
    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        
    
    def insert_at_any_pos(self, data, position):
        new_node = Node(data)
        
        if position < 0:
            print("Invalid position")
            return
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        count = 0
        
        while temp is not None and count < position - 1:
            temp = temp.next
            count = count + 1
        
        if temp is None:
            print("Position out of range")
            return

        
        new_node.next = temp.next
        temp.next = new_node
        
        
        
    def delete_from_end(self):
        if self.head is None:
            print("List empty / doesn't exist")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp.next = None
            
            
    def delete_from_begin(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next
        
        
    def delete_from_any_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        
        temp1= self.head
        count = 0
        while temp1 is not None and count < pos-1:
            temp1 = temp1.next
            count = count + 1

            
        temp1.next = temp1.next.next
        