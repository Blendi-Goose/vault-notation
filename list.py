import cellmachine as cm
import relative
def interpret(facing, shorthand, position, vault):
    if shorthand == "rg":
        cm.cells.Generator(vault, tuple(position), facing)
        return
    if shorthand == "dg":
        cm.cells.Generator(vault, tuple(position), relative.rotateval(facing, 1))
        return
    if shorthand == "lg":
        cm.cells.Generator(vault, tuple(position), relative.rotateval(facing, 2))
        return
    if shorthand == "ug":
        cm.cells.Generator(vault, tuple(position), relative.rotateval(facing, 3))
        return
    if shorthand == "rm":
        cm.cells.Mover(vault, tuple(position), facing)
        return
    if shorthand == "dm":
        cm.cells.Mover(vault, tuple(position), relative.rotateval(facing, 1))
        return
    if shorthand == "lm":
        cm.cells.Mover(vault, tuple(position), relative.rotateval(facing, 1))
        return
    if shorthand == "um":
        cm.cells.Mover(vault, tuple(position), relative.rotateval(facing, 1))
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
    if shorthand == "s":
        cm.cells.Slide(vault, tuple(position), facing)
        return
    raise Exception("Invalid data.")