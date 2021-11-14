class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.next = None
    def set_data(self, val):
        self.data = val


# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")

        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0

        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next

        return size

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.head:
            return

        temp = self.head

        # Check if head node is to be deleted
        if self.head.data == data:
            self.head = temp.next
            #print("Deleted node is " + str(self.head.data))
            return

        while temp.next:
            if temp.next.data == data:
                #print("Node deleted is " + str(temp.next.data))
                temp.next = temp.next.next
                return
            temp = temp.next
        #print("Node not found")
        return
    
    def length(self):
        c = 0
        temp = self.head
        while temp.next:
            c += 1 
            temp.next = temp.next.next
        return c + 1

    def get(self, index):
        if self.head == None:
            return None

        size = 0
        current = self.head
        while current:
            if size == index:
                return current.data
            size += 1
            current = current.next

        return size

    def mutate(self, index, value):
        if self.head == None:
            return None

        size = 0
        current = self.head
        while current:
            if size == index:
                current.data = value
            size += 1
            current = current.next

        return size
    
    def swap(self, ind1, ind2):
        val1 = self.get(ind1)
        val2 = self.get(ind2)
        self.mutate(ind1, val2)
        self.mutate(ind2, val1)

    def min_in_range(self, ind1, ind2):
        min_ind = ind1
        min_val = self.get(ind1)
        for i in range(ind1, ind2):
            val = self.get(i)
            if val < min_val:
                min_val = val
                min_ind = i 
        return min_ind, min_val

    def sort(self):
        l = self.size()
        for i in range(l):
            min_unseen = self.min_in_range(i,l)
            self.swap(i, min_unseen[0])

    def nodups(self):
        seen = set([self.head.data])
        if not self.head:
            return
        temp = self.head
        while temp.next:
            if temp.next.data in seen:
                temp.next = temp.next.next
            else:
                seen.add(temp.next.data)
                temp = temp.next
            


first_node = Node()
first_node.set_data(11)

ll = LinkedList(first_node)
ll.insert(3)
ll.insert(6)
ll.insert(3)
ll.insert(11)
ll.insert(6)
ll.insert(5)
ll.insert(7)
ll.insert(5)
print('before removing dups:')
ll.print_list()
ll.nodups()
print('after removing dups:')
ll.print_list()