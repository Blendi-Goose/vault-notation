import cellmachine.cells as cm
import sys
def interpret(facing, shorthand, position, vault):
    notation = ["rm","dm","lm","um","rg","dg","lg","ug","cw","cc","0","s"]
    cell_list = [cm.CW,cm.CCW,cm.Push,cm.Slide]
    rotation = [0,1,2,3,0,1,2,3,4,4,4,4]
    if facing == 0 or 1:
        notfacing = facing + 2
    else:
        notfacing = facing - 2
    for i, name in enumerate(notation):
        if shorthand == name:
            if i <= 3:
                cm.Mover(vault, tuple(position), i)
            elif i <= 7:
                cm.Generator(vault, tuple(position), i-4)
            else:
                cell_list[i-8](vault, tuple(position))
            if rotation[i] == notfacing:
                if i < 3:
                    return [True, False]
                else:
                    return [True, True]
            else:
                return [False, False]
    if shorthand == "no":
        return [False, False]
    print("\033[1;31mInvalid cell name.\033[0m\n")
    sys.exit()