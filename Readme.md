Timo's Armory Mod
=================
## Motivation  
[Inky's Armory Mod](https://steamcommunity.com/sharedfiles/filedetails/?id=1506010908&searchtext=armory) is a great Armory mod which gives me much fun, yet it hasn't updated for some time and it has bugs in V2.2. Therefore, based on its idea, I create this new armory mod.   

## Improvement  
1. Fix bug in Inky's Armory Mod. Now it works under V2.2  
2. Update weapons. Now it provide weapons of all 3 DLCs (Rise of the Giant, Fatal Falls, The Bad Seed).    
3. Add a python script to get weapon list and create the room file automatically.  

## How to create your own Armory Mod  
### 1. Unpack "res.pak"    
```powershell
& 'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\PAKTool.exe' -Expand -OutDir Expanded -RefPak "D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\res.pak"
```
### 2. Unpack CDB  
```powershell
& 'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\CDBTool.exe' -Expand -Outdir .\ExpandedCDB -refcdb ".\Expanded\data.cdb"
```
### 3. Use "RoomEditor" to Modify "PrisonFlaskRoom"  
Follow the guide at "Steam\steamapps\common\Dead Cells\ModTools\ModsDoc.pdf".  

### 4. Use "itemList.py" to get weapons and skills names in the game.  
```shell
python3 itemList.py
```
This will generate starter room file named "0573---PrisonFlaskRoom.json" and copy it to "ExpandedCDB".

### 5. Collapse cdb file  
```powershell
& 'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\CDBTool.exe' -Collapse -Indir .\ExpandedCDB\ -OutCDB ".\Expanded\data.cdb"
```
### 6. Create mod file  
```powershell
 &  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\PAKTool.exe' -creatediffpak -refpak "D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\res.pak" -indir "D:\Timo\Games\Timos-armory-mod\Expanded\" -OutPak "D:\Timo\Games\Timos-armory-mod\workshop\res.pak"
```
