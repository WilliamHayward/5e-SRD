import sys
import os
import json
import collections
# Usage: `explode.py [input file] [output folder]`
def main():
    spellsPath = sys.argv[1]
    output = sys.argv[2]
    spellsFile = open(spellsPath)
    items = json.load(spellsFile, object_pairs_hook=collections.OrderedDict)[u'Magic Items']

    if not os.path.exists(output):
        os.makedirs(output)
    names = items.keys()
    for name in names:
        new = collections.OrderedDict()
        new[u'name'] = name
        item = items[name]
        print(name)
        content = item[u'content']
        info = content[0].replace('*', '')
        divide = []
        if '),' in info:
            divide = info.split('),', 1)
            divide[0] += ')'
            divide[1] = divide[1][1:]
        else:
            divide = info.split(',', 1)
            divide[1] = divide[1][1:]

        attunement = False
        if 'requires attunement' in divide[1]:
            attunement = True
            divide[1] = divide[1].replace(' (requires attunement)', '')
        new[u'category'] = divide[0]
        new[u'rarity'] = divide[1]
        new[u'attunement'] = attunement
        new[u'desc'] = item[u'content'][1:]
        print(new)
        name = name.replace('/', '&2F')
        fileName = output + name + '.json'
        itemFile = open(fileName, 'w+')

        json.dump(new, itemFile, indent=4)

if __name__ == "__main__":
    main()