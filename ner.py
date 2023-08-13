import cellmachine as cm
import relative
import list

def fuse(length, firstPush, vault, facing):
    pos = firstPush
    for i in range(length):
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(3, pos, 1)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relative.move(1, pos, 2)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relative.move(3, pos, 1)
        pos = relative.move(0, pos, 1)
    pos = relative.move(2, pos, 1)
    pos = relative.move(1, pos, 2)
    cm.cells.Immobile(vault, tuple(pos))
    pos = relative.move(3, pos, 2)
    pos = relative.move(0, pos, 1)
    return pos

def base_ner(facing, thrust, pos, length, vault):
    # Bottom part of ner, clears waste gens
    length = length + 1
    for i in range(thrust):
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(3, pos, 1)
        cm.cells.Trash(vault, tuple(pos))
        pos = relative.move(1, pos, 2)
        cm.cells.Generator(vault, tuple(pos), relative.rotateval(3))
        pos = relative.move(1, pos, 1)
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(1, pos, 1)
        cm.cells.Immobile(vault, tuple(pos))
        pos = relative.move(3, pos, 3)
        pos = relative.move(0, pos, 1)
    # Bottom wall
    pos = relative.move(2, pos, 1)
    pos = relative.move(1, pos, 2)
    for i in range(length - 2):
        pos = relative.move(1, pos, 1)
        cm.cells.Immobile(vault, tuple(pos))
    # Right push and gen
    pos = relative.move(1, pos, 1)
    for i in range(thrust):
        pos = relative.move(0, pos, 1)
        cm.cells.Push(vault, tuple(pos))
        pos = relative.move(3, pos, 1)
        cm.cells.Generator(vault, tuple(pos), relative.rotateval(3))
        pos = relative.move(1, pos, 1)
    #Final Array
    pos = relative.move(3, pos, 1)
    for i in range(thrust):
        for j in range(length):
            pos = relative.move(3, pos, 1)
            cm.cells.Push(vault, tuple(pos))
        pos = relative.move(1, pos, length)
        pos = relative.move(2, pos, 1)
    pos = relative.move(0, pos, 1)
    pos = relative.move(3, pos, 1)
    corner1 = pos
    pos = relative.move(0, pos, thrust)
    pos = relative.move(3, pos, length)
    pos = relative.move(1, pos, 1)
    pos = relative.move(2, pos, 1)
    corner2 = pos
    pos = relative.move(3, pos, 1)
    pos = relative.move(0, pos, 1)
    for i in range(thrust):
        pos = relative.move(2, pos, 1)
        cm.cells.Trash(vault, tuple(pos))
    return [corner1, corner2]

def customthrust(facing, thrustValues, moverValues, corners, vault):
    corner1 = corners[0]
    corner2 = corners[1]
    vertical = True
    if facing == 0 or facing == 2:
        vertical = False
    pos = corner2
    if vertical: pos = relative.move(1, pos, 1)
    for i in range(len(thrustValues)):
        for j in range(thrustValues[i] + 3):
            cm.cells.Generator(vault, tuple(pos), relative.rotateval(2))
            pos = relative.move(2, pos, 1)
        pos = corner2
        if vertical: pos = relative.move(1, pos, 1)
        pos = relative.move(1, pos, i+1)
    if facing == 0 or facing == 2:
        pos = [corner1[0], corner2[1]]
    else:
        pos = [corner2[0], corner1[1]]
    notmyfirsttime = False
    for i in range(len(thrustValues)):
        if moverValues[i-1] and notmyfirsttime:
            cm.cells.Mover(vault, tuple(pos), relative.rotateval(2))
            if vertical and i != len(thrustValues):
                pos1 = pos
                pos = relative.move(1, pos, 1)
                pos = relative.move(0, pos, thrustValues[i] + 2)
                cm.cells.Push(vault, tuple(pos))
                pos = pos1
        notmyfirsttime = True
        pos = relative.move(1, pos, 1)
    list.slideallow(facing)
    return

def fill(facing, thrust, cells, fusepos, vault):
    start = fusepos[0]
    pos = start
    pos = relative.move(0, pos, thrust - 2)
    backtrack = False
    j = 0
    for tick in cells:
        for j, cell in enumerate(tick):
            backtrack = list.interpret(facing, cell, pos, vault)
            if backtrack[0] or backtrack[1]:
                J1 = j
                while True:
                    if j == 0:
                        pos = relative.move(2, pos, 1 + J1)
                        if backtrack[0]: 
                            cm.cells.Mover(vault, tuple(pos), facing)
                        backtrack[0] = False
                        j = J1
                        if backtrack[1]:
                            pos = relative.move(0, pos, thrust - 2)
                            cm.cells.Mover(vault,tuple(pos), relative.rotateval(2))
                            pos = relative.move(2, pos, thrust - 2)
                            backtrack[1] = False
                        pos = relative.move(0, pos, j + 1)
                        break
                    else:
                        j -= 1
            pos = relative.move(0, pos, 1)
        pos = relative.move(0, pos, thrust - 3)
    return