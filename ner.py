import cellmachine as cm
import relative
import list

def fuse(length, firstPush, vault, facing):
    pos = firstPush
    for i in range(length):
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(facing, 3, pos, 1, vault)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relative.move(facing, 1, pos, 2, vault)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relative.move(facing, 3, pos, 1, vault)
        pos = relative.move(facing, 0, pos, 1, vault)
    pos = relative.move(facing, 2, pos, 1, vault)
    pos = relative.move(facing, 1, pos, 2, vault)
    cm.cells.Immobile(vault, tuple(pos))
    pos = relative.move(facing, 3, pos, 2, vault)
    pos = relative.move(facing, 0, pos, 1, vault)
    return pos

def base_ner(facing, thrust, pos, length, vault):
    # Bottom part of ner, clears waste gens
    length = length + 1
    for i in range(thrust):
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(facing, 3, pos, 1, vault)
        cm.cells.Trash(vault, tuple(pos))
        pos = relative.move(facing, 1, pos, 2, vault)
        cm.cells.Generator(vault, tuple(pos), relative.rotateval(facing, 3))
        pos = relative.move(facing, 1, pos, 1, vault)
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(facing, 1, pos, 1, vault)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relative.move(facing, 3, pos, 3, vault)
        pos = relative.move(facing, 0, pos, 1, vault)
    # Bottom wall
    pos = relative.move(facing, 2, pos, 1, vault)
    pos = relative.move(facing, 1, pos, 2, vault)
    for i in range(length - 2):
        pos = relative.move(facing, 1, pos, 1, vault)
        cm.cells.Immobile(vault, tuple(pos))
    # Right push and gen
    pos = relative.move(facing, 1, pos, 1, vault)
    for i in range(thrust):
        pos = relative.move(facing, 0, pos, 1, vault)
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(facing, 3, pos, 1, vault)
        cm.cells.Generator(vault, tuple(pos), relative.rotateval(facing, 3))
        pos = relative.move(facing, 1, pos, 1, vault)
    #Final Array
    pos = relative.move(facing, 3, pos, 1, vault)
    for i in range(thrust):
        for j in range(length):
            pos = relative.move(facing, 3, pos, 1, vault)
            cm.cells.Push(vault, tuple(pos))
        pos = relative.move(facing, 1, pos, length, vault)
        pos = relative.move(facing, 2, pos, 1, vault)
    pos = relative.move(facing, 0, pos, 1, vault)
    pos = relative.move(facing, 3, pos, 1, vault)
    corner1 = pos
    pos = relative.move(facing, 0, pos, thrust, vault)
    pos = relative.move(facing, 3, pos, length, vault)
    pos = relative.move(facing, 1, pos, 1, vault)
    pos = relative.move(facing, 2, pos, 1, vault)
    corner2 = pos
    pos = relative.move(facing, 3, pos, 1, vault)
    pos = relative.move(facing, 0, pos, 1, vault)
    for i in range(thrust):
        pos = relative.move(facing, 2, pos, 1, vault)
        cm.cells.Trash(vault, tuple(pos))
    return [corner1, corner2]

def customthrust(facing, thrustValues, moverValues, corners, vault):
    corner1 = corners[0]
    corner2 = corners[1]
    pos = corner2
    for i in range(len(thrustValues)):
        for j in range(thrustValues[i] + 3):
            cm.cells.Generator(vault, tuple(pos), relative.rotateval(facing, 2))
            pos = relative.move(facing, 2, pos, 1, vault)
        pos = corner2
        pos = relative.move(facing, 1, pos, i+1, vault)
    pos = [corner2[0], corner1[1]]
    if facing == 0 or facing == 2:
        pos = [corner1[0], corner2[1]]
    notmyfirsttime = False
    for i in range(len(thrustValues)):
        if moverValues[i-1] and notmyfirsttime:
            cm.cells.Mover(vault, tuple(pos), relative.rotateval(facing, 2))
        notmyfirsttime = True
        pos = relative.move(facing, 1, pos, 1, vault)
    return

def fill(facing, thrust, cells, fusepos, vault):
    start = fusepos[0]
    pos = start
    pos = relative.move(facing, 0, pos, thrust - 2, vault)
    backtrack = False
    j = 0
    for tick in cells:
        for j, cell in enumerate(tick):
            backtrack = list.interpret(facing, cell, pos, vault)
            if backtrack[0] or backtrack[1]:
                J1 = j
                while True:
                    if j == 0:
                        pos = relative.move(facing, 2, pos, 1, vault)
                        if backtrack[0]: 
                            cm.cells.Mover(vault, tuple(pos), facing)
                        backtrack[0] = False
                        j = J1
                        if backtrack[1]:
                            pos = relative.move(facing, 0, pos, thrust - 2, vault)
                            cm.cells.Mover(vault,tuple(pos), relative.rotateval(facing, 2))
                            pos = relative.move(facing, 2, pos, thrust - 2, vault)
                            backtrack[1] = False
                        pos = relative.move(facing, 0, pos, j + 1, vault)
                        break
                    else:
                        j -= 1
                        pos = relative.move(facing, 2, pos, 1, vault)
            pos = relative.move(facing, 0, pos, 1, vault)
        pos = relative.move(facing, 0, pos, thrust - 3, vault)
    return