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

def main():
    itemDir = "./ExpandedCDB/item/"
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
    f = open('src/PrisonFlaskRoom.json','r')
    lines = f.readlines()
    f.close()

    # Create new room file
    f = open("0573---PrisonFlaskRoom.json",'w')
    for n, line in enumerate(lines):
        if "]," in line:
            lines[n-1] = "    },\n"
            header = lines[0:n]
            tail = lines[n:]
            break
    f.writelines(header)

    # Generate Armory list
    sizeOfWeapons = len(melee)+len(ranged)+len(shield)
    weapons = melee+ranged+shield
    sizeOfSkills  = len(trap)+len(grenade)+len(power)
    skills = trap+grenade+power
    print("Found weapons: {0} and skills: {1}".format(sizeOfWeapons,sizeOfSkills))

    # Armory showcase at y direction
    yList = [32,35,38,41,44,47]

    # Weapons showcase
    xRange = [2,34]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            weaponIndex = j*nInLine+i
            if weaponIndex < sizeOfWeapons:
                x = xRange[0]+i*2+1
                y = yList[j]
                f.writelines(jsonWrapper(x,y,weapons[weaponIndex]))

    # Skills showcase 1
    yList = [35,38,41,44,47]
    xRange = [36,62]
    nInLine = int((xRange[-1]-xRange[0])/2)
    for j in range(len(yList)):
        for i in range(nInLine):
            skillIndex = j*nInLine+i
            if skillIndex < sizeOfSkills:
                x = xRange[0]+i*2+1
                y = yList[j]
                f.writelines(jsonWrapper(x,y,skills[skillIndex]))

    f.writelines(tail)

    f.close()

    # Copy file to ExtendedCDB
    os.system("cp 0573---PrisonFlaskRoom.json ./ExpandedCDB/room/Prison/0573---PrisonFlaskRoom.json")

    print("Done!")

if __name__  == "__main__":
    main()
    
