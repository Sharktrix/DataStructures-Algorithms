// Now let's create our push method and we're going to push a new node onto the stack and we'll have top point to that new node.
// And just as we had in prepend, we have to code for when we don't have any items in the stack.

// Push Method
def push(self,value):
     new_node = Node(value)
     if self.height == 0:
        self.top = new_node
     else:
          new_node.next = self.top
           self.top = new_node
    self.height += 1


my_stack = Stack(2)   // This is where we create our new stack and we create it with a node with a value of 2.
my_stack.push(1)

my_stack.print_stack()
