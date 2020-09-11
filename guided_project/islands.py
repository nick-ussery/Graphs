"""
Write a function that takes a 2D binary array and returns the number of islands
An island consists of 1s that are connected to the north, south, east, or west.
For Example:

connected components:
"""
islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]


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


def get_neighbors(row, col, islands):
    neighbors = []

    if col < len(islands[row]) - 1 and islands[row][col + 1] == 1:
        neighbors.append(islands[row][col + 1])

    if col > 0 and islands[row][col - 1] == 1:
        neighbors.append(islands[row][col - 1])

    if row < len(islands) - 1 and islands[row + 1][col] == 1:
        neighbors.append(islands[row + 1][col])

    if row > 0 and islands[row - 1][col] == 1:
        neighbors.append(islands[row - 1][col])
    return neighbors


def dft(row, col, islands, visited):
    s = Stack()
    s.push((row, col))
    while s.size() > 0:
        r, c = s.pop()
        if (r, c) not in visited:
            visited.add((r, c))
            for neighbor in get_neighbors(r, c, islands):
                s.push(neighbor)


def island_counter(islands):
    visited = set()
    island_count = 0
    # Walk through each cell in the islands matrix
    for row in range(len(islands)):
        for col in range(len(islands[0])):
            # if its not visited and its a 1:
            if (row, col) not in visited and islands[row][col] == 1:
                # DFT from that cell, marking each as visited
                dft(row, col, islands, visited)
    #         Increment island counter
                island_count += 1
    return island_count


print(island_counter(islands))
