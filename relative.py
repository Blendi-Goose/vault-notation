import sys
def move(facing, direction, position, magnitude, vault):
    # Facing starts at right, direction starts at forward. Both go clockwise.
    newDirection = facing + direction
    if newDirection >= 4:
        newDirection -= 4
    if newDirection % 2 == 0:
        if newDirection == 0:
            newposition = [position[0] + magnitude, position[1]]
        else:
            newposition = [position[0] - magnitude, position[1]]
    else:
        if newDirection == 3:
            newposition = [position[0], position[1] - magnitude]
        else:
            newposition = [position[0], position[1] + magnitude]
    if vault.outside_bounds(newposition):
        print("\033[1;31mArea too small for solve: Please center the vault and/or increase level size.\033[0m\n")
        sys.exit()
    return newposition

def rotate(facing, direction, position, vault):
    vector = facing + direction
    vault.cells.get(position).rotate(vector)
    return

def rotateval(facing, direction):
    newdir = facing + direction
    if newdir >= 4:
        newdir = newdir - 4
    return newdir