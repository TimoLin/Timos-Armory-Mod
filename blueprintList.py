import sys
import os

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

def xmlWrapperBP(id, x,y,item):
    line = '<object id="'+ str(id)+'" name="Timo" type="FixedBlueprint" x="'+str(x*24)+'" y="'+str(y*24)+'" width="24" height="24">\n'
    line +='  <properties>\n'
    line +='    <property name="item" value="'+str(item)+'"/>\n'
    line +='  </properties>\n'
    line +=' </object>\n'
    return (line)

def xmlWrapperLoot(id, x,y,item):
    line = '<object id="'+ str(id)+'" name="Timo" type="FixedLoot" x="'+str(x*24)+'" y="'+str(y*24)+'" width="24" height="24">\n'
    line +='  <properties>\n'
    line +='    <property name="item" value="'+str(item)+'"/>\n'
    line +='  </properties>\n'
    line +=' </object>\n'
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
    for item in os.listdir(itemDir+"/Skin"):
        skins.append(item[6:item.index(".")])
    
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
    
    
    # Read base room file
    f = open('src/PrisonFlaskRoom.tmx','r')
    lines = f.readlines()
    f.close()

    # Create new room file
    f = open("PrisonFlaskRoom-BP-Mod.tmx",'w')
    f.writelines(lines[:-2])

    # Get start id
    for line in lines:
        if "object id" in line:
            id = int(line.split('"')[1])+1
    
    print("Start id:", id)

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

    # Armory showcase at y direction
    yList = [33,36,39,42,45,48]

    # Weapons showcase
    xRange = [2,34]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            weaponIndex = j*nInLine+i
            if weaponIndex < sizeOfWeapons:
                x = xRange[0]+i*2+1
                y = yList[j]
                #f.writelines(jsonWrapper(x,y,weapons[weaponIndex]))
                f.writelines(xmlWrapperBP(id,x,y,weapons[weaponIndex]))
                id += 1

    # Skills showcase 1
    yList = [36,39,42,45,48]
    xRange = [36,64]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            skillIndex = j*nInLine+i
            if skillIndex < sizeOfSkills:
                x = xRange[0]+i*2+1
                y = yList[j]
                #f.writelines(jsonWrapper(x,y,skills[skillIndex]))
                f.writelines(xmlWrapperBP(id,x,y,skills[skillIndex]))
                id += 1

    # Skins showcase
    yList = [2,5,8]
    xRange = [2,64]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            skinIndex = j*nInLine+i
            if skinIndex < len(skins):
                x = xRange[0]+i*2+1
                y = yList[j]
                #f.writelines(jsonWrapper(x,y,skins[skinIndex]))
                f.writelines(xmlWrapperBP(id,x,y,skins[skinIndex]))
                id += 1

    # Metas and Mutation showcase
    comb = metas+mutations
    yList = [51,54,57]
    xRange = [2,64]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            combIndex = j*nInLine+i
            if combIndex < len(comb):
                x = xRange[0]+i*2+1
                y = yList[j]
                if comb[combIndex] in metas:
                    # Runes
                    #f.writelines(jsonWrapperLoot(x,y,comb[combIndex]))
                    f.writelines(xmlWrapperLoot(id,x,y,comb[combIndex]))
                    id += 1
                else:
                    # Mutations
                    #f.writelines(jsonWrapper(x,y,comb[combIndex]))
                    f.writelines(xmlWrapperBP(id,x,y,comb[combIndex]))
                    id += 1
   
    tail = lines[-2:]
    f.writelines(tail)

    f.close()

    # Copy file to ExtendedCDB
    os.system("cp PrisonFlaskRoom-BP-Mod.tmx ./res/tiled/tmx/Prison/PrisonFlaskRoom.tmx ")

    print("Done!")

if __name__  == "__main__":
    main()
    
