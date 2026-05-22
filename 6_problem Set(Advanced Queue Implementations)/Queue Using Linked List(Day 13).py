class Node:
    def __init__(self, data):
        # Each node stores data and a pointer to next node
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        # Queue uses two pointers
        # front points to first element
        # rear points to last element
        self.rear = None
        self.front = None

    def queue_status(self):
        # Check if queue is empty
        if self.front is None:
            print("Queue is empty")
        else:
            print("Queue contains elements")

    def enqueue(self, data):
        # Insert element at the rear
        new_node = Node(data)

        # If queue is empty both front and rear point to new node
        if self.rear is None:
            self.front = self.rear = new_node
            return

        # Link new node at end and update rear
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        # Remove element from front
        if self.front is None:
            self.queue_status()
            return

        # Store value to display
        element = self.front.data

        # Move front ahead
        self.front = self.front.next

        # If queue becomes empty reset rear too
        if self.front is None:
            self.rear = None

        print("Removed", element)

    def peek(self):
        # Show front element
        if self.front is None:
            self.queue_status()
            return

        print(self.front.data)

    def list_values(self):
        # Display all queue elements
        current = self.front

        if self.front is None:
            self.queue_status()
            return

        while current:
            print(current.data, end=" <- ")
            current = current.next

        print(None)


obb = Queue()

obb.enqueue(10)
obb.enqueue(20)
obb.enqueue(30)
obb.enqueue(40)

obb.dequeue()        # removes 10 
obb.list_values()    # prints remaining queue 