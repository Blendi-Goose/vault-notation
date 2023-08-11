import cellmachine.cells as cm
import sys
def interpret(facing, shorthand, position, vault):
    notation = ["rm","dm","lm","um","rg","dg","lg","ug","cw","cc","0","s"]
    cell_list = [cm.CW,cm.CCW,cm.Push,cm.Slide]
    rotation = [0,1,2,3,0,1,2,3,4,4,4,4]
    if facing == 0 or facing == 1:
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
            if rotation[i] == notfacing or rotation[i] == facing:
                if rotation[i] == notfacing: # Facing the vault
                    if i > 3: # Generator facing the vault
                        print(i, shorthand, rotation[i], name)
                        return [True, True]
                    else: # Mover facing the vault
                        return [True, False]
                else: # Facing the ner
                    if i > 3: # Generator facing the ner
                        print(i, shorthand, rotation[i], name)
                        return [True, True]
                    else: # Mover facing the ner
                        return [False, True]
            else:
                return [False, False]
    if shorthand == "no":
        return [False, False]
    print("\033[1;31mInvalid cell name.\033[0m\n")
    sys.exit()