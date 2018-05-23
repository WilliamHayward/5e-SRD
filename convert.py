import sys
import os
import json
import collections
# Usage: `convert.py [input folder] [output folder]`
def main():
    inFolder = sys.argv[1]
    output = sys.argv[2]
    
    monsterNames = os.listdir(inFolder)

    if not os.path.exists(output):
        os.makedirs(output)

    for monsterFile in monsterNames:
        monster = json.load(
            open(inFolder + monsterFile)
        )

        info = []
        info.append('\\begin{monsterbox}{' + monster[u'name'] + '}')
        info.append('\\begin{hangingpar}')
        subtype = ""
        if monster[u'subtype'] != "":
            subtype = "(" + monster[u'subtype'] + ") "
        info.append('\\textit{' +
            monster[u'size'] + ' ' + monster[u'type'] + subtype +
            ', ' + monster[u'alignment'].replace("%", "\%") + '}')
        info.append('\\end{hangingpar}')
        info.append('\\dndline%')
        info.append('\\basics[%')
        info.append('armorclass = ' + str(monster[u'armor_class']) + ',')
        hitString = monster[u'hit_dice']
        base = monster[u'hit_points_base']
        if base > 0:
            hitString += ' + ' + str(base)
        elif base < 0:
            hitString += ' - ' + str(abs(base))
        info.append('hitpoints = ' + hitString + ',')
        info.append('speed = {' + monster[u'speed'] + '}')
        info.append(']')
        info.append('\\dndline%')

        info.append('\\stats[%')
        ability_scores = [u'strength', u'dexterity', u'constitution', u'intelligence', u'wisdom', u'charisma']
        for score in ability_scores:
            val = str(monster[score])
            abbreviation = score[0:3].upper()
            scoreString = abbreviation + ' = \\stat{' + val + '}'
            if abbreviation != 'CHA':
                scoreString += ','
            info.append(scoreString)

        info.append(']')
        info.append('\\dndline%')

        info.append('\\details[%')
        skills = "{"
        for skill in monster[u'skills']:
            skills += skill.title() + ' +' + str(monster[u'skills'][skill]) + ', '
        if skills[-2: -1] == ', ':
            skills = skills[0: -2]
        skills += '}'
        info.append('skills=' + skills + ',')
        info.append('damageimmunities={' + str(monster[u'damage_immunities']) + '},')
        saves = "{"
        for save in monster[u'saving_throws']:
            saves += save.title()[0:3] + ' +' + str(monster[u'saving_throws'][save]) + ', '
        if saves[-2: -1] == ', ':
            saves = saves[0: -2]
        saves += '}'
        info.append('savingthrows=' + saves + ',')
        info.append('conditionimmunities={' + str(monster[u'condition_immunities']) + '},')
        info.append('damageresistances={' + str(monster[u'damage_resistances']) + '},')
        info.append('damagevulnerabilities={' + str(monster[u'damage_vulnerabilities']) + '},')
        if str(monster[u'senses']) != "":
            info.append('senses={' + str(monster[u'senses']) + '},')
        if str(monster[u'languages']) != "":
            info.append('languages={' + str(monster[u'languages']) + '},')
        info.append('challenge=' + monster[u'challenge_rating'])

        info.append(']')
        info.append('\\dndline%')
        
        if u'special_abilities' in monster:
            for ability in monster[u'special_abilities']:
                info += buildAction(ability)

        if u'actions' in monster:
            info.append('\\monstersection{Actions}')
            for action in monster[u'actions']:
                info += buildAction(action)

        if u'legendary_actions' in monster:
            info.append('\\monstersection{Legendary Actions}')
            for legendary_action in monster[u'legendary_actions']:
                info += buildAction(legendary_action)

        info.append('\\end{monsterbox}')

        outFile = open(output + monsterFile.replace('.json', '.tex'), 'w+')
        outFile.write('\n'.join(info))

def buildAction(action):
    info = []
    info.append('\\begin{monsteraction}[' + action[u'name'] + ']')
    info.append(action[u'desc'])
    info.append('\\end{monsteraction}')
    return info
	

if __name__ == "__main__":
    main()