import cellmachine as cm
import funky as funcs
def ner(facing, thrust, pos, length, vault):
    # Bottom part of ner, clears waste gens
    for i in range(thrust):
        cm.cells.Push(vault, tuple(pos))
        pos = funcs.relativeMove(facing, 3, pos, 1, vault)
        cm.cells.Trash(vault, tuple(pos))
        pos = funcs.relativeMove(facing, 1, pos, 2, vault)
        cm.cells.Generator(vault, tuple(pos), 1)
        pos = funcs.relativeMove(facing, 1, pos, 1, vault)
        cm.cells.Push(vault, tuple(pos))
        pos = funcs.relativeMove(facing, 1, pos, 1, vault)
        cm.cells.Immobile(vault, tuple(pos))
        pos = funcs.relativeMove(facing, 3, pos, 3, vault)
        pos = funcs.relativeMove(facing, 0, pos, 1, vault)
    # Bottom wall
    pos = funcs.relativeMove(facing, 2, pos, 1, vault)
    pos = funcs.relativeMove(facing, 1, pos, 2, vault)
    for i in range(length - 2):
        pos = funcs.relativeMove(facing, 1, pos, 1, vault)
        cm.cells.Immobile(vault, tuple(pos))
    # Right push and gen
    for i in range(thrust):
        pos = funcs.relativeMove(facing, 0, pos, 1, vault)
        cm.cells.Push(vault, tuple(pos))
        pos = funcs.relativeMove(facing, 3, pos, 1, vault)
        cm.cells.Generator(vault, tuple(pos), 1)
        pos = funcs.relativeMove(facing, 1, pos, 1, vault)
    # Main push array
    pos = funcs.relativeMove(facing, 1, pos, length+2, vault)
    for i in range(thrust):
        for i in range(length):
            cm.cells.Push(vault, tuple(pos))
            pos = funcs.relativeMove(facing, 3, pos, 1, vault)
        pos = funcs.relativeMove(facing, 2, pos, 1, vault)
        pos = funcs.relativeMove(facing, 1, pos, length, vault)
    pos = funcs.relativeMove(facing, 3, pos, length, vault)
    pos = funcs.relativeMove(facing, 0, pos, 1, vault)
    cm.cells.Generator(vault, tuple(pos), 1)
    corner1 = pos
    pos = funcs.relativeMove(facing, 0, pos, thrust, vault)
    pos = funcs.relativeMove(facing, 1, pos, length, vault)
    cm.cells.Generator(vault, tuple(pos), 1)
    corner2 = pos
    print(cm.levelstring.v3.export_level(vault))
    return [corner1, corner2]