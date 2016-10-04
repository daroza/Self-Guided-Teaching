"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head == None or head.next == None:
        return False

    cycle = 0
    node_a = head
    node_b = head.next

    while node_b.next != None:
        if node_a == node_b:
            return True
        if cycle % 4 == 0:
            node_a = node_a.next
            cycle += 1
            node_b = node_b.next

    return False
