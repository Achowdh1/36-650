from myqueue import Queue
import pytest



def test_queue_functions():
    Q = Queue()
    Q.enqueue(5)
    assert Q.items == [5], 'check inner list'
    Q.enqueue(6)
    assert Q.dequeue() == 5, 'check fifo'
    assert Q.size() == 1, 'check size'
    Q.dequeue()
    assert Q.dequeue() == None, 'edge case, dequeue from empty queue'
    assert Q.size() == 0, 'edge case, Q is empty'
    Q.enqueue(None)
    Q.enqueue(None)
    assert Q.dequeue() == None, 'edge case, duplicates and string input'
    assert Q.dequeue() == None, 'edge case, duplicates and string input'
