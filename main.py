import cellmachine as cm
import sys

fileCode = sys.argv[1]
vault = cm.import_level(fileCode)
vaultArray = vault.cells.values()
print(vaultArray[0])

vaultNotation = sys.argv[2]
sections = vaultNotation.split(";")
if sections[0] != "V4":
    raise Exception("How dare you send a notation without the Holy V4.")
ticks = sections[3].split(" ")
for tick in ticks:
    cells = tick.split(".")

print("test")