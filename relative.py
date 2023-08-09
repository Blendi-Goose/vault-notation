def move(facing, direction, position, magnitude, vault):
    # Facing starts at right, direction starts at forward. Both go clockwise.
    newDirection = facing + direction
    if newDirection % 2 == 0:
        if newDirection == 0:
            newposition = [position[0] + magnitude, position[1]]
        else:
            newposition = [position[0] - magnitude, position[1]]
    else:
        if newDirection == 3:
            newposition = [position[0], position[1] + magnitude]
        else:
            newposition = [position[0], position[1] - magnitude]
    if vault.outside_bounds(newposition):
        raise Exception("Area too small for proper ner to be made, please expand.")
    return newposition

def rotate(facing, direction, position, vault):
    vector = facing + direction
    vault.cells.get(position).rotate(vector)
    return