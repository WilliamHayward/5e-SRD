import sys
import os
import json
import collections
# Usage: `explode.py [input file] [output folder]`
def main():
    print(sys.argv)
    spellsPath = sys.argv[1]
    output = sys.argv[2]
    spellsFile = open(spellsPath)
    spells = json.load(spellsFile, object_pairs_hook=collections.OrderedDict)
    print(spells)

    if not os.path.exists(output):
        os.makedirs(output)
    
    for spell in spells:
        print(spell)
        spellName = spell[u'name'].replace('/', '%2F')
        spellFile = open(output + spellName + '.json', 'w+')
        json.dump(spell, spellFile)

if __name__ == "__main__":
    main()