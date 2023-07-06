// a method is Binary search tree class

def BFS(self):
    current_node = self.root
    queue = []
    results = []
    queue.append(current_node)   // entire node with value and left and right

    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)


