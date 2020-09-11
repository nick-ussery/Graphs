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


def earliest_ancestor(ancestors, starting_node):
    visited = set()
    q = Queue()

    q.enqueue([starting_node])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            neighbors = []

            for f in ancestors:
                if f[1] == v:
                    neighbors.append(f[0])

            for neighbor in neighbors:
                q.enqueue(path + [neighbor])  # Makes a new list
                #path_copy = list(path)
                # path_copy.append(neighbor)
                # q.enqueue(path_copy)
