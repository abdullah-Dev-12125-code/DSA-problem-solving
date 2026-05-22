class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


# making nodes 
new_node1 = Node(10)
new_node2 = Node(20)
new_node3 = Node(30)
new_node4 = Node(40)

# connecting them 
new_node1.next = new_node2
new_node2.next = new_node3
new_node3.next = new_node4

# head is first node
head = new_node1

# pointer to start moving in list
current = head

# we use this to store previous node for reversing
last = None

current = head

# go through whole list one by one
while current is not None:
    # save next node first so we dont lose rest of list
    next = current.next
    # reverse the link turn arrow backwards
    current.next = last
    # move last forward it becomes current node
    last = current
    # move current to next node
    current = next

# after loop last becomes new head
head = last

# now print reversed list
current = head

#Simply printed it
while current is not None:
    print(current.data, end="->")
    current = current.next

print(None)


