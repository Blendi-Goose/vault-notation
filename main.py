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