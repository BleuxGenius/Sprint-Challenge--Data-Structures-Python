class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # 1. check if there is a node, if no node end the recursion.
        if not node:
            return
        # 2. check if next node exist , if no node , set current node as the head.node. it turns the tail of the old into the head of reversed list. 
        if node.get_next() == None:
            self.head = node
            return 
        # 3. set the next node to a variable to use it as a current node. when i recursively call the reverse_list() method. i also set current node as the previous node when reverse_list() is called 
        next_node = node.get_next()
        self.reverse_list(next_node, node)
        # 4. when list is traversed, change the pointers by preparing the next node of the new head [the previous tail] to current node and delete pointer of the current node. Do it for each node until entire list is reversed. 
        # traversed = Traversal is a process to visit all the nodes of a tree and may print their values too.
        node.get_next().set_next(node)
        node.set_next(None)

