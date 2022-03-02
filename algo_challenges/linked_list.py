"""
Implement a linked list
"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """
        1. Create new Node with supplied data
        2. Set the new Node's next node to the current head of the linked list
        3. Set the current head of the linked list to the new Node
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """
        Starting at the head, travel down the line of nodes until you reach the end and keep track of the nodes.
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        """
        Check at each stop to see whether the current node has the requested data and if so, return the node holding that data.
        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        """
        When the delete method reaches the node it wants to delete, it resets the previous node’s pointer so that, rather than pointing to the soon-to-be-deleted node, it will point to the next node in line, effectively removing the node from the list!
        """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())