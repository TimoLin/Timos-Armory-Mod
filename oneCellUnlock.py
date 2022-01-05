import sys
import os
import glob
import re

def jsonWrapper(x,y,item):
    line =  '    {\n'+\
            '      "x": '+str(x)+',\n' + \
            '      "y": '+str(y)+',\n' + \
            '      "marker": "FixedBlueprint",\n' +\
            '      "width": 1,\n'+\
            '      "height": 1,\n'+\
            '      "item": "'+item+'"\n' + \
            '    },\n'
    return (line)

def jsonWrapperLoot(x,y,item):
    line =  '    {\n'+\
            '      "x": '+str(x)+',\n' + \
            '      "y": '+str(y)+',\n' + \
            '      "marker": "FixedLoot",\n' +\
            '      "width": 1,\n'+\
            '      "height": 1,\n'+\
            '      "item": "'+item+'"\n' + \
            '    },\n'
    return (line)


def main():
    itemDir = "./ExpandedCDB-BP/item/"
    # 1. Melee items
    melee = []
    for item in os.listdir(itemDir+"/Melee"):
        if "StartSword" not in item and "AdminWeapon" not in item:
            melee.append(item[6:item.index(".")])
    
    # 2. Ranged items
    ranged = []
    for item in os.listdir(itemDir+"/Ranged"):
        if "StartBow" not in item:
            ranged.append(item[6:item.index(".")])
    
    # 3. Shield items
    shield = []
    for item in os.listdir(itemDir+"/Shield"):
        if "StartShield" not in item:
            shield.append(item[6:item.index(".")])
    
    # 4. Trap items
    trap = []
    for item in os.listdir(itemDir+"/DeployedTrap"):
        trap.append(item[6:item.index(".")])

    # 5. Grenade items
    grenade = []
    for item in os.listdir(itemDir+"/Grenade"):
        grenade.append(item[6:item.index(".")])
    
    # 6. Power items
    power = []
    for item in os.listdir(itemDir+"/Power"):
        power.append(item[6:item.index(".")])
    
    # 7. Skins 
    skins = []
    # for item in os.listdir(itemDir+"/Skin"):
    for file in glob.glob(itemDir+"/Skin/*.json"):
        with open(file,'r') as f:
            lines = f.readlines()
            for n, line in enumerate(lines):
                if "cellCost" in line:
                    cost = int(line.split(":")[-1].split(",")[0])
                    if cost > 1:
                        lines[n] = '  "cellCost": 1,\n'
                        # Write to file
                        desFile = file.replace("CDB-BP","CDB-OCU")
                        with open(desFile,'w') as f2:
                            f2.writelines(lines)
                        # Jump out loop
                        break
    
    # 8. Meta stuff
    metas = []
    lastItem = ""
    for item in os.listdir(itemDir+"/Meta"):
        item = item[6:item.index(".")]
        if "BossRune" not in item:
            metas.append(item)
        # if item[0:-1] == lastItem[0:-1]:
            # metas[-1] = item
        # else:
            # metas.append(item)
            # lastItem=item

    # 9. Mutations/Perks
    mutations = []
    for item in os.listdir(itemDir+"/Perk"):
        item = item[6:item.index(".")]
        mutations.append(item)
    
    # Generate Armory list
    # Remove duplicates
    weapons = []
    for item in melee+ranged+shield:
        if "OffHand" not in item: # For some Bows
            if "theRight" not in item: # For some weapons with two hands
                if item not in weapons:
                    weapons.append(item)
    sizeOfWeapons = len(weapons)

    skills = []
    for item in trap+grenade+power:
        if "Up" not in item:
            skills.append(item)
    sizeOfSkills  = len(skills)

    sizeOfSkins  = len(skins)

    sizeOfMetas  = len(metas)

    print("Found Weapons: {0}".format(sizeOfWeapons))
    print("      Skills : {0}".format(sizeOfSkills))
    print("      Skins  : {0}".format(sizeOfSkins))
    print("      Metas  : {0}".format(sizeOfMetas))
    print("Done!")

if __name__  == "__main__":
    main()
    
