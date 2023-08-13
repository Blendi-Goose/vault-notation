import cellmachine.cells as cm
import sys
notation = {"rm": [cm.Mover, 0],"dm": [cm.Mover, 1],"lm": [cm.Mover, 2],"um": [cm.Mover, 3],
             "rg": [cm.Generator, 0],"dg": [cm.Generator, 1],"lg": [cm.Generator, 2],"ug": [cm.Generator, 3],
             "cw": [cm.CW, 0],"cc": [cm.CCW, 0],"0": [cm.Push, 0]}
notfacing = 0
def slideallow(facing):
    notation.update({"s": [cm.Slide, facing]})
    global notfacing
    if facing == 0 or facing == 1:
        notfacing = facing + 2
    else:
        notfacing = facing - 2
def interpret(facing, shorthand, position, vault):
    cell = notation[shorthand][0]
    rot = notation[shorthand][1]
    if cell != cm.Push:
        cell(vault, tuple(position), rot)
    if rot == facing:
        if cell == cm.Mover:
            return [False, True]
        if cell == cm.Generator:
            return [True, True]
    if rot == notfacing:
        if cell == cm.Mover:
            return [True, False]
        if cell == cm.Generator:
            return [True, True]
    return [False, False]