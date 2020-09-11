from room import Room
from player import Player
from world import World

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
visited = {}

inverse_directions = {"n": "s", "s": "n",
                      "e": "w", "w": "e"}  # easier to code backpath

reverse_path = [None]  # backtrack path

visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph):  # loop until all rooms visited
    if player.current_room.id not in visited:  # is room new
        visited[player.current_room.id] = player.current_room.get_exits()

        reverse_direction = reverse_path[-1]  # save backpath
        visited[player.current_room.id].remove(reverse_direction)

    # reverse up tree to go down new path
    while len(visited[player.current_room.id]) < 1:
        reverse_direction = reverse_path.pop()
        traversal_path.append(reverse_direction)
        player.travel(reverse_direction)

    exit_direction = visited[player.current_room.id].pop(0)
    traversal_path.append(exit_direction)
    reverse_path.append(inverse_directions[exit_direction])

    player.travel(exit_direction)

    if len(room_graph) - len(visited) == 1:  # an error is thrown if there is 1 room left. idk why
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
