class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# creating nodes 
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# linking nodes
node1.next = node2
node2.next = node3
node3.next = node4

# creating a cycle 40 -> 20
node4.next = node2

# head 
head = node1


# function to detect & remove cycle
def remove_cycle(head):
    slow = head
    fast = head

    # detect cycle using slow & fast pointer
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return

    # move slow back to head
    slow = head

    # find start of cycle
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # break the cycle
    fast.next = None


# remove cycle from list
remove_cycle(head)


# print final linked list
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next

print(None)