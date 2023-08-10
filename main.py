import cellmachine as cm
import sys
import relative
import ner
import time
start_time = time.time()

fileCode = sys.argv[1]
vault = cm.import_level(fileCode)

vaultNotation = sys.argv[2]
sections = vaultNotation.split(";")
if sections[0] != "V4":
    raise ValueError("Invalid notation version.")

ticks = sections[3].split(" ")
cells = [0 for i in range(len(ticks))]
for i in range(len(ticks)):
    cells[i] = ticks[i].split(".")

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
    raise Exception("\033[1;31mOne gaps only. One gap on top. No resistance to this policy allowed.\033[0m\n")
trashorpit = vault.cells.get(tuple(relative.move(facing, 2, tuple(corner2), 1, vault))).__class__ == cm.cells.trash.Trash
print("Trash Vault: " + str(trashorpit))
if trashorpit == False:
    print("Pit vaults not supported yet.. good luck?")
i = 0
for tick in cells:
    print(tick) 
    i += 1
thrust = length + 4
lengthFuse = thrust * i
endofFuse = ner.fuse(lengthFuse, relative.move(facing, 0, corner1, 1, vault), vault, facing)
boundaries = ner.base_ner(facing, thrust + 1, endofFuse, i, vault)
thrustValues = [0 for i in range(len(cells))]
count = 0
moverValues = [False for i in range(len(cells))]
for i in range(len(thrustValues)):
    for j in range(len(cells[i])):
        count += 1
        cell = cells[i][j]
        if cell[-1] == '+':
            moverValues[i] = True
            cells[i][j] = cell[:-1]
    thrustValues[i] = count
    count = 0
ner.customthrust(facing, thrustValues, moverValues, boundaries, vault)
ner.fill(facing, thrust, cells, [corner1, endofFuse], vault)

# ALWAYS LEAVE AT BOTTOM
endTime = time.time() - start_time
print("Solve took ", endTime ,"s to complete")
print(cm.levelstring.v2.export_level(vault))
print("Exporting took ", time.time() - start_time - endTime, "s to complete")