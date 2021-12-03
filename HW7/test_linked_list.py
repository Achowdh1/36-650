from linked_list import * 
import pytest

def test_set_data():
    first_node = Node()
    first_node.set_data(11)
    assert first_node.data == 11, 'happy test set data'
    node2 = Node()
    node2.set_data('hello')
    assert node2.data == 'hello', 'happy test set data'
    node2.set_data(None)
    assert node2.data == None, 'edge test set data'
    #edge case, set_data throws error when not enough args are passed in
    with pytest.raises(TypeError):
        node3 = Node()
        node3.set_data()

def test_ll_size():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    l2 = LinkedList()
    assert l2.size() == 0, 'edge case size is empty'
    assert linked_list.size() == 1, 'happy case size is 1'
    linked_list.insert(3)
    linked_list.insert(6)
    assert linked_list.size() == 3, 'happy case size is 1'

def test_ll_print():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(3)
    l2 = LinkedList()
    assert l2.head == None, 'edge case, empty head init'
    with pytest.raises(ValueError):
        l2.print_list()
    assert linked_list.print_list() == None, 'happy path test print list'

def test_ll_remove_dups():
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    linked_list.insert(3)
    linked_list.insert(6)
    linked_list.insert(3)
    linked_list.remove_dups()
    assert linked_list.size() == 3, 'happy case remove dups  cut off one element'
    assert linked_list.head.next.next.next == None, 'happy case remove dups got rid of last node'
    linked_list.remove_dups()
    assert linked_list.size() == 3, 'edge case remove dups does nothing when all elements are unique'
    assert linked_list.head.next.data == 3, 'edge case remove dups does nothing when all elements are unique'
    assert linked_list.head.next.next.data == 6, 'edge case remove dups does nothing when all elements are unique'
    linked_list.insert(None)
    assert linked_list.head.next.next.next.data == None, 'edge case insert adding none-type'


def test_ll_insert():
    ll2 = LinkedList()
    ll2.insert(11)
    assert ll2.head.data == 11, 'edge case, insert node into empty list'
    first_node = Node()
    first_node.set_data(11)
    linked_list = LinkedList(first_node)
    assert linked_list.size() == 1, 'happy case size is 1'
    linked_list.insert(3)
    linked_list.insert(6)
    assert linked_list.size() == 3, 'happy case size is 1'
    assert linked_list.head.next.data == 3, 'happy case insert put right data'
    assert linked_list.head.next.next.data == 6, 'happy case insert put right data'