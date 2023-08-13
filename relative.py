import sys
facing = 0
def orient(orient):
    global facing
    facing = orient
    return

def move(direction, position, magnitude):
    # Facing starts at right, direction starts at forward. Both go clockwise.
    newDirection = facing + direction
    if newDirection >= 4:
        newDirection -= 4
    if newDirection % 2:
        if newDirection == 3:
            newposition = [position[0], position[1] - magnitude]
        else:
            newposition = [position[0], position[1] + magnitude]
    else:
        if newDirection == 0:
            newposition = [position[0] + magnitude, position[1]]
        else:
            newposition = [position[0] - magnitude, position[1]]
    return newposition

def rotateval(direction):
    newdir = facing + direction
    if newdir >= 4:
        newdir = newdir - 4
    return newdir