# Adjacency Lists have neighbors not a next node
# Can have many neighbors

"""
Graphs:
    Nodes connected by edges
    Vertexes
    Vertices
    Verts

Directed vs Undirected
    Directed has one-way edges

Cyclic vs Acyclic
    Cyclic has a way back to a node you have visited already

Weighed Edges
    "Cost" with traversing an edge

Traversals:
    Breadth First
    Depth first

LL:
cur = head
while cur is not None:
    print(cur)
    cur = cur.next

Binary Tree:
traverse(node):
if node is None: return
    traverse(node.left)
    print
    traverse(node.right)

Breath-First Adjacency List:
    visited = {}
    Queue front -> []

Depth-First Adjacency List:
    stack instead of queue



"""


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __repr__(self):
        return f'Node({repr(self.value)})'


def bft(node):
    # Create a queue to hold nodes to visit
    # Create a set to hold visited nodes
    to_visit = Queue()
    visited = set()
    # Initialize: add the starting node to the queue
    to_visit.enqueue(node)
    # while queue is NOT empty:
    while to_visit.size() > 0:
        v = to_visit.dequeue()
        # dequeue first entry
        # if not visitied, make it visited
        # Visit node( print it out )
        # Add it to the visited set
        if v not in visited:
            print(v)
            # Enqueue all its neighbors
            visited.add(v)

            for n in v.neighbors:
                to_visit.enqueue(n)


def dft(node):
    # Create a queue to hold nodes to visit
    # Create a set to hold visited nodes
    to_visit = Stack()
    visited = set()
    # Initialize: add the starting node to the queue
    to_visit.push(node)
    # while queue is NOT empty:
    while to_visit.size() > 0:
        v = to_visit.pop()
        # dequeue first entry
        # if not visitied, make it visited
        # Visit node( print it out )
        # Add it to the visited set
        if v not in visited:
            print(v)
            # Enqueue all its neighbors
            visited.add(v)

            for n in v.neighbors:
                to_visit.push(n)


def bfs(starting_vertex, target_vertex):
    # Create an empty queue and enqueue
    # Create a set to store visited vert
    # While the queue is not empty...
    # Dequeue the first Path
    # Grab the last vertex from the
    # If that vertex has not been visited...
    # Check if its the target
    # Mark it as visited...
    # Then add A PATH TO its neighbors
    # Copyu the path
    # Append the neighbor to the back


a = Node('A')
b = Node('B')
c = Node('C')

a.neighbors.append(b)
a.neighbors.append(c)

b.neighbors.append(b)
b.neighbors.append(c)

c.neighbors.append(b)


# how to traverse without being stuck in a loop
# Breath First Traversal

# Check Queue is it empty if no->done if yes->
# Visit next node in Queue, is it visited yet? No->
# Add neighbors to Queue
# Yes-> check queue

bft(a)

dft(a)
