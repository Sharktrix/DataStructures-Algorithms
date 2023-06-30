// Two scenarios:
// One is if we only have one item in the queue.
// And the other is if we don't have any items in the queue.
// Last is with a longer list

def dequeue(self):
    if self.length == 0:
        return None
    temp = self.first
    if self.length == 1:
       self.first = None
       self.last = None
    else:
        self.first = self.first.next
        temp.next = None
    self.length -= 1
    return temp


my_queue = Queue(1)
my_queue.enqueue(2)


# (2) Items - Returns 2 Node
print(my_queue.dequeue())
# (1) Item - Returns 1 Node
print(my_queue.dequeue())
# (0) Items - Returns None
print(my_queue.dequeue())





