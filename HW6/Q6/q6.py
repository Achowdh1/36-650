
class ReverseNode(object):
    def __init__(self, data = None):
        self.data = data
        self.prev = None
    def set_data(self, val):
        self.data = val

class ReverseLinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")

        current = self.tail
        while current:
            print(current.data, end = " ")
            current = current.prev
        print()
    # Find length of Linked List
    def size(self):
        if self.tail == None:
            return 0

        size = 0
        current = self.tail
        while current:
            size += 1
            current = current.tail
        return size

    def insert(self, data):
        rn = ReverseNode(data)
        temp = self.tail
        self.tail = rn
        self.tail.prev = temp
    def delete(self, data):
        if not self.tail:
            return
        temp = self.tail
        # Check if head node is to be deleted
        if self.tail.data == data:
            self.tail = temp.prev
            #print("Deleted node is " + str(self.head.data))
            return
        while temp.prev:
            if temp.prev.data == data:
                #print("Node deleted is " + str(temp.next.data))
                temp.prev = temp.prev.prev
                return
            temp = temp.prev

    def search(self, data):
        current = self.tail
        while current: 
            if current.data == data:
                return True
            current = current.prev
        return False


first_node = ReverseNode()
first_node.set_data(11)

ll = ReverseLinkedList(first_node)
ll.insert(3)
ll.insert(6)
ll.insert(5)
print('reverse ll after insertion:')
ll.print_list()
ll.delete(6)

print('reverse ll after deleting 6:')
ll.print_list()
print('is 5 in the list?')
print(ll.search(5))
print('is 17 in the list?')
print(ll.search(17))