# Sub-modules 

def jsonWrapper(x,y,item):
    '''Wrap item line in json format
    '''
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
    '''Wrap item line in xml format
    '''
    line = '<object id="'+ str(id)+'" name="Timo" type="FixedLoot" x="'+str(x*24)+'" y="'+str(y*24)+'" width="24" height="24">\n'
    line +='  <properties>\n'
    line +='    <property name="item" value="'+str(item)+'"/>\n'
    line +='  </properties>\n'
    line +=' </object>\n'
    return (line)

def jsonWrapperLoot(x,y,item):
    '''Wrap item line in json format
    '''
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
    '''Wrap item line in xml format for blueprint items
    '''
    line = '<object id="'+ str(id)+'" name="Timo" type="FixedBlueprint" x="'+str(x*24)+'" y="'+str(y*24)+'" width="24" height="24">\n'
    line +='  <properties>\n'
    line +='    <property name="item" value="'+str(item)+'"/>\n'
    line +='  </properties>\n'
    line +=' </object>\n'
    return (line)

def xmlWrapperLoot(id, x,y,item):
    '''Wrap item line in xml format for Fixed loot items
    '''
    line = '<object id="'+ str(id)+'" name="Timo" type="FixedLoot" x="'+str(x*24)+'" y="'+str(y*24)+'" width="24" height="24">\n'
    line +='  <properties>\n'
    line +='    <property name="item" value="'+str(item)+'"/>\n'
    line +='  </properties>\n'
    line +=' </object>\n'
    return (line)

def itemsDLC():
    '''Read itemsDlc.list file and generate dict containing "item:dlc"
    '''
    fName = "itemsDlc.list"

    # RiseOfTheGiant is free dlc
    dlcs = ['TheBadSeed', 'FatalFalls', 'TheQueenAndTheSea']
    dlcDict = []
    tbs = []
    ff  = []
    tqats = []

    with open(fName,"r") as f:
        for line in f.readlines():
            if '"dlc"' in line:
                # Format line
                line = line.replace(",","")
                line = line[:-1].replace(" ","")
                line = line.replace('"',"")
                
                # Parse line
                cat  = line.split("/")[2]
                i1   = line.index("---")+3
                i2   = line.index(".json")
                item = line[i1:i2]
                dlc  = line.split(":")[2]
                if dlc == dlcs[0]:
                    tbs.append(item)
                elif dlc == dlcs[1]:
                    ff.append(item)
                elif dlc == dlcs[2]:
                    tqats.append(item)
                '''
                if cat in ["Melee","Ranged","Shield"]:
                    subDictWeapon[item] = dlc
                elif cat in ["Power","DeployedTrap"]:
                    subDictSkill[item] = dlc
                elif cat in ["Skin"]:
                    subDictSkin[item] = dlc
                elif cat in ["Meta"]:
                    subDictMeta[item] = dlc
                '''

    return dlcs, [tbs,ff, tqats]
