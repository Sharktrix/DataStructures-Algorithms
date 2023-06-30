// Pop Method

// Pop is going to be the removal of that top node, and then you have the top pointer point at the next.
// And then, of course, we're going to return that node that we popped from the stack.
// And then we also have to code for this situation where we don't have any items in the stack.


def pop(self): 
      if self.height == 0:         //We'll code for this situation where we have an empty stack first.
      return None                 //We'll say if the height is zero.

    temp = self.top               //Otherwise, we do have items in the stack.
    self.top = self.top.next      //And we want to return that top node. Variable is "temp"
    temp.next = None
    self.height -=1               //Decrement the length by one.
    return temp                  //And then we'll return temp.



my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_Stack.pop(), '\n')

my_stack.print_stack()


