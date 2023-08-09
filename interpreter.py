import cellmachine as cm
def interpret(facing, shorthand, position, vault):
    if shorthand == "rg":
        cm.cells.Generator(vault, tuple(position), 0 + facing)
        return
    if shorthand == "dg":
        cm.cells.Generator(vault, tuple(position), 1 + facing)
        return
    if shorthand == "lg":
        cm.cells.Generator(vault, tuple(position), 2 + facing)
        return
    if shorthand == "ug":
        cm.cells.Generator(vault, tuple(position), 3 + facing)
        return
    if shorthand == "rm":
        cm.cells.Mover(vault, tuple(position), 0 + facing)
        return
    if shorthand == "dm":
        cm.cells.Mover(vault, tuple(position), 1 + facing)
        return
    if shorthand == "lm":
        cm.cells.Mover(vault, tuple(position), 2 + facing)
        return
    if shorthand == "um":
        cm.cells.Mover(vault, tuple(position), 3 + facing)
        return
    if shorthand == "cw":
        cm.cells.CW(vault, tuple(position))
        return
    if shorthand == "cc":
        cm.cells.CCW(vault, tuple(position))
        return
    if shorthand == "0":
        cm.cells.Push(vault, tuple(position))
        return
    if shorthand == "vs":
        cm.cells.Slide(vault, tuple(position), 1 + facing)
        return
    if shorthand == "hs":
        cm.cells.Slide(vault, tuple(position), 0 + facing)
        return
    raise Exception("Invalid data.")