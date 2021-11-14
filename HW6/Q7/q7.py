
class TriTree(object):
    def __init__(self, data = None):
        self.data = data
        self.small = None
        self.big = None
        self.toobig = None
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.small: self.small.insert(data)
                else: self.small = TriTree(data)
            elif data - self.data <= 10:
                if self.big: self.big.insert(data)
                else: self.big = TriTree(data)
            else:
                if self.toobig: self.toobig.insert(data)
                else: self.toobig = TriTree(data)
        else: self.data = data

    def traversal(self, depth = 0):
        if self.small:
            self.small.traversal(depth + 1)
        if self.data:
            print(self.data)
        if self.big:
            self.big.traversal(depth + 1)
        if self.toobig:
            self.toobig.traversal(depth + 1)

    def fill_traversal(self, l, depth = 0):
        if self.small:
            self.small.fill_traversal(l, depth + 1)
        if self.data:
            l += [(self.data, depth)]
        if self.big:
            self.big.fill_traversal(l, depth + 1)
        if self.toobig:
            self.toobig.fill_traversal(l, depth + 1)

    def extract_traversal(self):
        l = []
        self.fill_traversal(l)
        return sorted(l, key = lambda x: x[1])

    def delete(self, key):
        trav = self.extract_traversal()
        self.__init__()
        for data in trav:
            val = data[0]
            if val != key:
                self.insert(val)



t = TriTree(20)
t.insert(40)
t.insert(45)
t.insert(32)
print('contents after insertion using traversal():')
t.traversal()
t.delete(45)
print('contents after deletion of 45 using traversal():')
t.traversal()





