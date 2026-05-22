class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating nodes 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# connecting nodes altogether 
node1.next = node2
node2.next = node3
node3.next = node4

# head is starting point
head = node1

# pointer to move in list
current = head

# counting total nodes
count = 0
while current is not None:
    count += 1          # increase count
    current = current.next   # move forward

# finding middle index
middle = count // 2

# again start from head
current = head

# move to middle position
for i in range(middle):
    current = current.next

# print middle value
print(current.data)