import cellmachine as cm
import sys

fileCode = sys.argv[1]
vault = cm.import_level(fileCode)

vaultNotation = sys.argv[2]
sections = vaultNotation.split(";")
if sections[0] != "V4":
    raise ValueError("Invalid notation version.")
ticks = sections[3].split(" ")
cells = {}
for i in range(len(ticks)):
    cells[i] = ticks[i].split(".")
print(cells)

size = vault.size
corner1S = sections[1].split(",")
corner1 = [int(corner1S[0]),int(corner1S[1])]
corner2S = sections[2].split(",")
corner2 = [int(corner2S[0]),int(corner2S[1])]
if vault.outside_bounds(corner1) or vault.outside_bounds(corner2):
    raise Exception("Vault Access Point is outside bounds.")

facing = 3
onegapontop = 0
if corner1[0] != corner2[0]:
    onegapontop += 1
    facing = 0
    if corner1[0] < corner2[0]:
        facing = 2
if corner1[1] != corner2[1]:
    onegapontop += 1
    if corner1[1] < corner2[1]:
        facing = 1
print("0 is right, goes counterclockwise: " + str(facing))
if onegapontop == 2:
    raise Exception("\033[1;31mNow hold your horses, buckaroo. Only one gaps allowed in this house.\033[0m\n")
fuse(20)
# FUSE FRAMEWORK
# Will write over cells in the way of the fuse! Manual fixing may be necessary.

def fuse(length, firstPush):
    pos = firstPush
    for i in range(length):
        cm.cells.Push(vault, pos)
        pos = relativeMove(2, pos, 1)
        cm.cells.Immobile(vault, pos)
        pos = relativeMove(0, pos, 2)
        cm.cells.Immobile(vault, pos)
        pos = relativeMove(3, pos, 1)
        pos = relativeMove(2, pos, 1)
        print(vault.export_level)
    return

def relativeMove(direction, position, magnitude):
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