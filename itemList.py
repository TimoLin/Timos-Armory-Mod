import sys
import os

def jsonWrapper(x,y,item):
    line =  '    {\n'+\
            '      "x": '+str(x)+',\n' + \
            '      "y": '+str(y)+',\n' + \
            '      "marker": "FixedLoot",\n' +\
            '      "width": 1,\n'+\
            '      "height": 1,\n'+\
            '      "item": "'+item+'"\n' + \
            '    },\n'
    return (line)

def xmlWrapper(id, x,y,item):
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
    
    # Read base room file
    f = open('src/PrisonFlaskRoom.tmx','r')
    lines = f.readlines()
    f.close()

    # Create new room file
    f = open('PrisonFlaskRoom-Armory.tmx','w')
    f.writelines(lines[:-2])

    # Get start id
    for line in lines:
        if "object id" in line:
            id = int(line.split('"')[1])+1
    
    print("Start id:", id)

    # Generate Armory list
    # Remove duplicates
    # Mostly it's the other status of the weapon
    weapons = []
    duplicates = ["OffHand", "theRight", "Broken"]
    for item in melee+ranged+shield:
        flag = any(key in item for key in duplicates)
        if (not flag):
            weapons.append(item)
    sizeOfWeapons = len(weapons)

    skills = []
    for item in trap+grenade+power:
        if item not in ["ExplodeFriendlyHardy","FlyingSwordCallback","OwlUp","BackDash"]:
            skills.append(item)

    sizeOfSkills  = len(skills)

    print("Found weapons: {0} and skills: {1}".format(sizeOfWeapons,sizeOfSkills))

    # Armory showcase at y direction
    yList = [41,44,47,50,53,56]

    # Weapons showcase
    xRange = [2,34]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            weaponIndex = j*nInLine+i
            if weaponIndex < sizeOfWeapons:
                x = xRange[0]+i*2+1
                y = yList[j]
                f.writelines(xmlWrapper(id,x,y,weapons[weaponIndex]))
                id += 1

    # Skills showcase 1
    yList = [41,44,47,50,53]
    xRange = [36,64]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            skillIndex = j*nInLine+i
            if skillIndex < sizeOfSkills:
                x = xRange[0]+i*2+1
                y = yList[j]
                f.writelines(xmlWrapper(id,x,y,skills[skillIndex]))
                id += 1

    f.writelines(lines[-2:])

    f.close()

    # Copy file to ExtendedCDB
    os.system("cp PrisonFlaskRoom-Armory.tmx ./armory-tmx/tmx/Prison/PrisonFlaskRoom.tmx")

    print("Done!")

if __name__  == "__main__":
    main()
    
