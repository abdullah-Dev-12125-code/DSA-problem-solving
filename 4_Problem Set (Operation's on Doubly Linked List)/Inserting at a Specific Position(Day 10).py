class Node:
    def __init__(self, data):
        # Each node stores data
        self.data = data

        # Pointer to next node in the list
        self.next = None
        
        # Pointer to previous node in the list
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        # Head points to the first node of the list
        self.head = None

    def append(self, data):
        # Create a new node
        new_node = Node(data)

        # If list is empty new node becomes head
        if self.head is None:
            self.head = new_node
        else:
            # Traverse to the last node
            current = self.head
            while current.next is not None:
                current = current.next

            # Link last node to new node
            current.next = new_node
            
            # Link new node back to last node
            new_node.prev = current

    def insert_at_specific_position(self, data, position):
        # Create new node to insert
        new_node = Node(data)

        # Case 1 insert at beginnining
        if position == 0:
            new_node.next = self.head  # new node points to old head

            # If list is not empty update old head's prev pointer
            if self.head:
                self.head.prev = new_node

            # Move head to new node
            self.head = new_node
            return

        # Case 2 insert at middle or end
        count = 0
        current = self.head

        # Move to node just before target position
        while current and count < position - 1:
            current = current.next
            count += 1

        # If position is out of range
        if current is None:
            return

        # Connect new node to next node
        new_node.next = current.next

        # Link new node's prev back to current
        new_node.prev = current

        # If not inserting at end fix backward link of next node
        if current.next:
            current.next.prev = new_node

        # Connect current node to new node
        current.next = new_node

    def list_values(self):
        # Traverse and print list 
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(None)



obb = doubly_linked_list()

obb.append(10)
obb.append(20)
obb.append(30)

# Inserting 80 at position 1 
obb.insert_at_specific_position(80, 1)

obb.list_values()