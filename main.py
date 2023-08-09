import cellmachine as cm
import sys
import funky as funcs
import ner

fileCode = sys.argv[1]
vault = cm.import_level(fileCode)

vaultNotation = sys.argv[2]
sections = vaultNotation.split(";")
if sections[0] != "V4":
    raise ValueError("Invalid notation version.")
ticks = sections[3].split(" ")
cells = []
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
    length = corner1[0] - corner2[0]
    if corner1[0] < corner2[0]:
        facing = 2
        length = corner2[0] - corner1[0] 
if corner1[1] != corner2[1]:
    onegapontop += 1
    length = corner1[1] - corner2[1]
    if corner1[1] < corner2[1]:
        length = corner2[1] - corner1[1] 
        facing = 1
print("0 is right, goes counterclockwise: " + str(facing))
if onegapontop == 2:
    raise Exception("\033[1;31mNow hold your horses, buckaroo. Only one gaps allowed in this house.\033[0m\n")
trashorpit = vault.cells.get(tuple(funcs.relativeMove(facing, 2, tuple(corner2), 1, vault))).__class__ == cm.cells.trash.Trash
print("Trash Vault: " + str(trashorpit))

i = 0
j = 0
if trashorpit:
    for tick in cells:
        i += 1
        print(tick)
        for cell in tick:
            j += 1
    thrust = j/i + 2
    lengthFuse = thrust * i
else:
    raise Exception("Trash vaults are the only currently supported vault. Sorry!")
endofFuse = funcs.fuse(lengthFuse, funcs.relativeMove(facing, 0, corner1, 1, vault), vault, facing)
endofFuse = funcs.relativeMove(facing, 0, endofFuse, 1, vault)
ner.ner(facing, thrust, endofFuse, i, vault)