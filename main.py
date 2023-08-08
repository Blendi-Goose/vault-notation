import cellmachine as cm
import sys

fileCode = sys.argv[1]
print(fileCode)
vault = cm.import_level(fileCode)
vaultArray = vault.cells.values()
print(list(vaultArray))

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
positionS = [sections[1], sections[2]]
position = [int(positionS[0].split(",")),int(positionS[1].split(","))]
if vault.outside_bounds(position[0]) or vault.outside_bounds(position[1]):
    raise Exception("Vault Access Point is outside bounds.")
cell = vault.level.cells.get(position[1])