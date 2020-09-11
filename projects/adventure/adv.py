from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# DFS fewer moves if go all the way down and back track once deadends are hit

turn_counter = 0

backup_directions = {"n": "s", "s": "n",
                     "e": "w", "w": "e"}  # easier to code backpath

reverse_path = [None]  # backtrack path
visited = {}
visited[player.current_room.id] = player.current_room.get_exits()


while len(visited) < len(room_graph):  # loop until all rooms visited
    print(f"entered room: {player.current_room.id}")
    if player.current_room.id not in visited:  # is room new
        visited[player.current_room.id] = player.current_room.get_exits()
        visited[player.current_room.id].remove(reverse_path[-1])

    # dead end hit when 0 exits. go back up
    if len(visited[player.current_room.id]) == 0:
        while len(visited[player.current_room.id]) < 1:
            reverse_direction = reverse_path.pop()
            traversal_path.append(reverse_direction)
            player.travel(reverse_direction)
    if "e" in visited[player.current_room.id]:
        direction = visited[player.current_room.id].index("e")
        explore = visited[player.current_room.id].pop(direction)
    else:
        explore = visited[player.current_room.id].pop(0)
    print(f"taking exit {explore}")
    traversal_path.append(explore)
    reverse_path.append(backup_directions[explore])

    player.travel(explore)

    if len(room_graph) - len(visited) == 1:
        visited[player.current_room.id] = player.current_room.get_exits()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######

# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
