def enqueue(self,value):                 // No items in the list 
    new_node = Node(value)
    if self.first is None:
        self.first = new_node
        self.last = new_node
    else:                                    // when there are items in the list
        self.last.next = new_node
        self.last = new_node
    self.length +=1


my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()

