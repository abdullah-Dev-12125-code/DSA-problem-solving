class PriorityQueue:
    def __init__(self):
        # List to store elements as data, priority in tuples
        self.queue = []


    def enqueue(self, data, priority):
        # Add element with its priority into the queue
        self.queue.append((data, priority))
        return


    def dequeue(self):
        # If queue is empty nothing to remove
        if len(self.queue) == 0:
            print("Queue is empty")
            return

        # Assume first element has highest priority lowest number = highest priority so we will find it soon
        max_priority = 0

        # Find element with highest priority which is the smallest priority number
        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[max_priority][1]:
                max_priority = i

        # Remove and return the highest priority element
        removed = self.queue.pop(max_priority)
        return removed


    def peek(self):
        # Show highest priority element 
        if len(self.queue) == 0:
            print("Queue is empty")
            return

        # Start assuming first element has highest priority
        max_priority = 0

        # Find the element with smallest priority value
        for i in range(1, len(self.queue)):
            if self.queue[i][1] < self.queue[max_priority][1]:
                max_priority = i

        # Display the highest priority element
        peeked = self.queue[max_priority]
        print("Peeked:", peeked)


    def print_list(self):
        # Print queue 
        if len(self.queue) == 0:
            print("Priority Queue is empty")
            return

        # Display each element with its priority
        for data, priority in self.queue:
            print(f"{data}({priority})", end=" <- ")

        print(None)
        return



q = PriorityQueue()

# Insert elements with priorities
q.enqueue("Abdullah", 3)
q.enqueue("Hussain", 1)
q.enqueue("Shayan", 2)
q.enqueue("Ali", 0)

# Print current queue
q.print_list()

# Show highest priority element 
q.peek()

# Remove highest priority element
print("Removed:", q.dequeue())

# Print queue after removal
q.print_list()