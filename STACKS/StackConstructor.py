// Node Class
class Node:
    def__init__(self,value):
        self.value = value
        self.next = None

// Stack Class
class Stack:
    def __init__(self, value):     //Constructor for the stack 
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(4)

my_stack.print_stack()