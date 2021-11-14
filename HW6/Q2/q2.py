
class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list += [value]
        return None
        
    def dequeue(self):
        return self.inner_list.pop(0)

    def delete(self, value):
        l = []
        while len(self.inner_list) > 0:
            val = self.dequeue()
            if val != value:
                l += [val]
        for elem in l:
            self.enqueue(elem)
        pass



print('Test 1')     
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.delete(7)
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())




print('Test 2')     
obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(8)
obj.enqueue(9)
obj.delete(5)
print(obj.inner_list)



