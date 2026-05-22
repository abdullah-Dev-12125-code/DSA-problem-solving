class Queue:
    def __init__(self):
        # queue as array
        self.queue = []

    def enqueue(self, data):
        # Add element at the rear of the queue 
        self.queue.append(data)

    def dequeue(self):
        # Remove element from the front of the queue 

        # Check whether queue is empty or not 
        if len(self.queue) == 0:
            print("The queue is empty")
            return

        # pop(0) removes first element 
        removed = self.queue.pop(0)
        return removed

    def recursive_reversal(self):
        # Reverses queue using recursion only

        # stop when queue becomes empty
        if len(self.queue) == 0:
            return

        # Remove front element
        first = self.dequeue()

        # Recursive call on remaining queue
        self.recursive_reversal()

        # Add removed element at rear 
        self.enqueue(first)

    def list_values(self):
        # Display all queue elements with index positions

        # empty queue
        if len(self.queue) == 0:
            print("Queue is empty")
            return

        # Print all elements in order
        for value, data in enumerate(self.queue):
            print(f"{value}. {data}")

        print(None)



obb = Queue()

obb.enqueue(10)
obb.enqueue(20)
obb.enqueue(30)
obb.enqueue(40)
obb.enqueue(50)

obb.list_values()          # original queue
obb.recursive_reversal()   # reverse using recursion
obb.list_values()          # reversed queue