import collections
import os
import json
import sys
from math import ceil
skills = [u'athletics', u'acrobatics', u'sleight of hand', u'stealth', u'arcana', u'history', u'investigation', u'nature', u'religion', u'animal handling', u'insight', u'medicine', u'perception', u'survival', u'deception', u'intimidation', u'performance', u'persuasion']
ability_scores = [u'strength', u'dexterity', u'constitution', u'intelligence', u'wisdom', u'charisma']
def insertAtPosition(dictionary, key, value, position):
    new = collections.OrderedDict()
    for existing in dictionary:
        new[existing] = dictionary[existing]
        if existing == position:
            new[key] = value
    return new

def mergeSkills(dictionary):
    dictionary = insertAtPosition(dictionary, u'skills', collections.OrderedDict(), u'saving_throws')
    for skill in skills:
        if skill in dictionary:
            dictionary[u'skills'][skill] = dictionary[skill]
    new = collections.OrderedDict()
    for existing in dictionary:
        if existing not in skills:
            new[existing] = dictionary[existing]
    return new

def mergeSaves(dictionary):
    dictionary = insertAtPosition(dictionary, u'saving_throws', collections.OrderedDict(), u'charisma')
    for ability_score in ability_scores:
        save_string = ability_score + '_save'
        if save_string in dictionary:
            dictionary[u'saving_throws'][ability_score] = dictionary[save_string]
    new = collections.OrderedDict()
    for existing in dictionary:
        if '_save' not in existing:
            new[existing] = dictionary[existing]
    return new

def getBaseHealth(dice, hp):
    numDice = int(dice.split('d')[0])
    diceType = int(dice.split('d')[1])

    base = hp - (numDice * (diceType + 1) / 2.0)
    return ceil(base)


print(getBaseHealth('3d8', 22))
#sys.exit()
files = os.listdir(sys.argv[1])

for monsterFileName in files:
    path = sys.argv[1] + monsterFileName
    print(path)
    monsterFile = open(path)
    monster = json.load(monsterFile, object_pairs_hook=collections.OrderedDict)
    monster = mergeSaves(monster)
    monsterFile = open(path, 'w+')
    json.dump(monster, monsterFile, indent=4)
    