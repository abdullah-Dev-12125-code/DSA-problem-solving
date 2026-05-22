class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        # node stores data next pointer prev pointer


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        # head points first node in list

    def append(self, data):
        new_node = Node(data)
        # create new node

        if self.head is None:
            self.head = new_node
            # if list empty new node becomes head
        else:
            current = self.head
            # start from head

            while current.next is not None:
                current = current.next
                # move to last node

            current.next = new_node
            # connect last node to new node
            new_node.prev = current
            # connect back pointer to previous node

    def find_node(self, value):
        count = 0
        current = self.head
        # start search from head

        while current is not None:
            if current.data == value:
                print(f"Index: {count}, Data: {current.data}")
                # value found print index and data
                return

            current = current.next
            count += 1
            # else move next node increase index

        print(-1)
        # if value not found

    def count_occurence_My_logic_enhanced(self):
        freq = {}
        current = self.head
        # dictionary for counting frequency

        while current:
            if current.data in freq:
                freq[current.data] += 1
                # increase count if already exists
            else:
                freq[current.data] = 1
                # first time seen value

            current = current.next
            # move next node

        return freq

    def count_occurrence_My_logic(self):
        new_array = []
        freq = {}
        current = self.head
        # list to track seen values and dict for counts

        while current:
            value = current.data

            if value in new_array:
                freq[value] += 1
                # already seen increase count
            else:
                new_array.append(value)
                freq[value] = 1
                # first time add to list and set count to 1

            current = current.next
            # move next node

        return freq

    def list_numbers(self):
        current = self.head
        # print full linked list

        while current is not None:
            print(current.data, end=" <- ")
            current = current.next
            # move next node

        print(None)
        # end of list




obb = DoublyLinkedList()

obb.append(10)
obb.append(20)
obb.append(20)
obb.append(20)
obb.append(30)
obb.append(40)
# create doubly linked list

obb.find_node(80)
obb.find_node(40)
# search values

print("\n--- Linked List ---")
obb.list_numbers()

print("\n--- Basic Frequency Count ---")

print(obb.count_occurrence_My_logic())

print("\n--- Enhanced Frequency Count ---")
print(obb.count_occurence_My_logic_enhanced())