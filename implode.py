import sys
import os
import json
import collections
# Usage: `implode.py [input folder] [output file]`
def main():
    spellsPath = sys.argv[1]
    output = sys.argv[2]
    spellNames = os.listdir(spellsPath)
    spellNames.sort()
    spells = []
    for spellName in spellNames:
        name = spellName.replace('&2F', '/')
        spellFile = open(spellsPath + spellName)
        spells.append(json.load(spellFile, object_pairs_hook=collections.OrderedDict))

    compiled = open(output, 'w+')
    json.dump(spells, compiled, indent=4)

if __name__ == "__main__":
    main()