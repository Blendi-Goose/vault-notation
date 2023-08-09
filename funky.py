import cellmachine as cm

def fuse(length, firstPush, vault, facing):
    pos = firstPush
    for i in range(length):
        cm.cells.Push(vault, tuple(pos))
        pos = relativeMove(facing, 3, pos, 1, vault)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relativeMove(facing, 1, pos, 2, vault)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relativeMove(facing, 3, pos, 1, vault)
        pos = relativeMove(facing, 0, pos, 1, vault)
    print(cm.levelstring.v3.export_level(vault))
    return pos


def relativeMove(facing, direction, position, magnitude, vault):
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

def relativeRotate(facing, direction, position, vault):
    vector = facing + direction
    vault.cells.get(position).rotate(vector)
    return