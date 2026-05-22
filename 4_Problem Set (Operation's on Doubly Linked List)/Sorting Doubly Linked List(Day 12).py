class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data,end=" <- ")
            current = current.next
        print(None)

    def insert_at_head(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = new_node
            new_node.prev = current

    def insert_at_position(self,data,position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_head(data) 
            return
        current = self.head
        count = 0 

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("position is out of reach")
            return
        
        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node

    
    def bubble_sort_list(self):
        if self.head is None:
            return  # If list is empty there is nothing to sort

        swap = True  # Flag to control whether another pass is needed

        while swap:  # Keep looping until no swaps happen in a full pass
            swap = False  # Assume list is sorted at start of each pass
            current = self.head  # Start from head for each pass

            while current.next is not None:  # Traverse until second last node
                if current.data > current.next.data:
                    # If current node value is greater than next node value
                    # then swap their data not nodes 
                    current.data, current.next.data = current.next.data, current.data
                    swap = True  # A swap happened so list is not fully sorted yet

                current = current.next  # Move to next node in list


dll = DoublyLinkedList()
dll.append(50)
dll.append(10)
dll.append(70)
dll.append(20)
dll.append(60)
dll.append(40)
dll.bubble_sort_list()
dll.print_list()