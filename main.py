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
corner1S = sections[1].split(",")
corner1 = [int(corner1S[0]),int(corner1S[1])]
corner2S = sections[2].split(",")
corner2 = [int(corner2S[0]),int(corner2S[1])]
if vault.outside_bounds(corner1) or vault.outside_bounds(corner2):
    raise Exception("Vault Access Point is outside bounds.")