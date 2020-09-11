"""
Word Ladders
-------------
Given 2 words(first_word, end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word. Note:
    return None if there is no such transformation sequence
    All words contain only lowercase alphabetic characters
    you may assume no duplicates in word list
    you may assume begin_word and end_word are non-empty and are not the same

For there to be a path, begin_word and end_word must be the same length
Ties for shortest path are dealers choice
"""

"""
Converting to graph terminology
-------------------------------
Nodes are words
so we know the first and last nodes

edges are letter change

nodes are only legal if in dictionary

option A: try every letter combination
option b: look through dictionary and find those words that are 1 letter different

so for each word, make a graph to find its neighbors
in this case, all the neighbors are every word with only 1 difference
"""
import string
words = set()

with open("words.txt") as f:
    for word in f:
        words.add(word.lower().strip())


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


def get_neighbors(word):
    neighbors = []

    for w in words:
        if len(w) != len(word):
            continue

        diffs = 0

        for i in range(len(w)):
            if w[i] != word[i]:
                diffs += 1

        if diffs == 1:
            neighbors.append(w)

    return neighbors


def get_neighbors_2(word):
    word_letters = list(word)
    neighbors = []
    for i in range(len(word)):
        for l in string.ascii_lowercase:
            candidate_letters = list(word_letters)
            candidate_letters[i] = l
            candidate = "".join(candidate_letters)

            if candidate != word and candidate in words:
                neighbors.append(candidate)
    return neighbors


def bfs(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                q.enqueue(path + [neighbor])  # Makes a new list
                #path_copy = list(path)
                # path_copy.append(neighbor)
                # q.enqueue(path_copy)


def bfs_2(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors_2(v):
                q.enqueue(path + [neighbor])  # Makes a new list
                #path_copy = list(path)
                # path_copy.append(neighbor)
                # q.enqueue(path_copy)


# print(bfs("sail", "boat"))
print(bfs_2("sail", "boat"))
