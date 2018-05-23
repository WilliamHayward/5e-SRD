import sys
import os
import json
import collections
# Usage: `explode.py [input file] [output folder]`
def main():
    spellsPath = sys.argv[1]
    output = sys.argv[2]
    spellsFile = open(spellsPath)
    spells = json.load(spellsFile, object_pairs_hook=collections.OrderedDict)

    if not os.path.exists(output):
        os.makedirs(output)
    
    for spell in spells:
        spellName = spell[u'name'].replace('/', '&2F')
        fileName = output + spellName + '.json'
        spellFile = open(fileName, 'w+')

        json.dump(spell, spellFile, indent=4)

if __name__ == "__main__":
    main()