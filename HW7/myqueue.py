class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        try: return self.items.pop()
        except IndexError as i:
            print('index error, popping from empty queue:')
            print(str(i))
            return None
    
    def size(self):
        return len(self.items)