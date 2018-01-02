
class Node:

    # initialize node with a key and value
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    # remap the previous and next node to each other
    # unmap the current node to none
    def remove(self):

        if self.next != None:
            self.next.prev = self.prev
        if self.prev != None:
            self.prev.next = self.next

        self.next = None
        self.prev = None

        return self