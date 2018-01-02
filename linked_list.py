from node import Node

class LinkedList:

    # initialize list with two nodes
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # add a node with key and value to list
    def append(self, key, value):
        append_node = Node(key, value)

        append_node.next = self.tail
        append_node.prev = self.tail.prev
        self.tail.prev.next = append_node
        self.tail.prev = append_node

        return append_node

    # loop through each node
    # remove the node with key provided
    def remove(self, key):
        loop_node = self.head.next

        while loop_node != self.tail:
            if loop_node.key == key:
                loop_node.remove()
                return loop_node.value
            loop_node = loop_node.next

        return None

    # loop through each node
    # update value of node with value provided
    def update(self, key, value):
        loop_node = self.head.next

        while loop_node != self.tail:
            if loop_node.key == key:
                loop_node.value = value
                return loop_node.value
            loop_node = loop_node.next

        return None

    # determine if the list is empty
    def isEmpty(self):
        return self.head.next == self.tail

    # loop through each node
    # return the value of the node matching the key
    def get(self, key):
        loop_node = self.head.next

        while loop_node != self.tail:
            if loop_node.key == key:
                return loop_node.value
            loop_node = loop_node.next

        return None

    # determine if the value is in the list
    def isIncluded(self, key):
        node_value = self.get(key)
        return node_value != None

    # loop through each node
    # helper function to get elements
    def get_fragmentSet(self, function = "keys"):
        contents = []
        loop_node = self.head.next

        while loop_node != self.tail:
            if function == "values":
                contents.append(loop_node.value)
            elif function == "elements":
                element = (loop_node.key, loop_node.value)
                contents.append(element)
            else:
                contents.append(loop_node.key)
            loop_node = loop_node.next
        return contents

    # return all values as a list
    def values(self):
        return self.get_fragmentSet("values")

    # return all keys as a list
    def keys(self):
        return self.get_fragmentSet()

    # return all key and value pairs as a list
    def elements(self):
        return self.get_fragmentSet("elements")