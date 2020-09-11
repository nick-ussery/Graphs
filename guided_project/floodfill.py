image_str = [
    '############################',
    '#                          #',
    '#       ######             #',
    '#     ##      #            #',
    '#      ####   #            #',
    '#         ##  #            #',
    '#      ###    #            #',
    '#     ##      #            #',
    '#    #        #            #',
    '#     ########             #',
    '#                          #',
    '############################'
]

image = []

for s in image_str:
    image.append(list(s))


def print_image():
    for i in image:
        print("".join(i))


def floodfill(row, col, char):
    # depth first traversal
    # set the character at this "pixel" to char
    # for each neighbor:
    #      floodill(neighbor)
    # base case: if pixel at row, col is not a space, then return
    if image[row][col] != " ":
        return

    image[row][col] = char

    # flood fill neighbors
    floodfill(row-1, col, char)
    floodfill(row+1, col, char)
    floodfill(row, col - 1, char)
    floodfill(row, col-1, char)


print_image()
floodfill(6, 13, 'x')
print_image()
