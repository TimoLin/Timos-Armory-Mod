Timo's Armory Mod
=================
## Motivation  
[Inky's Armory Mod](https://steamcommunity.com/sharedfiles/filedetails/?id=1506010908&searchtext=armory) is a great Armory mod which gives me much fun, yet it hasn't updated for some time and it has bugs in V2.2. Therefore, based on its idea, I create this new armory mod.   

## Improvement  
1. Fix bug in Inky's Armory Mod. Now it works under V2.2  
2. Update weapons. Now it provide weapons of all 3 DLCs (Rise of the Giant, Fatal Falls, The Bad Seed).    
3. Add a python script to get weapon list and create the room file automatically.  

## File Description
|File|Language|Description|
|:-|:-:|:-|
|preStep.ps1|Powershell|Pre-steps that unpack Dead Cells resource packages|
|itemList.py|Python|Extract items to create armory mod files|
|packArmory.ps1|Powershell|Pack Timo's armory mod|
|blueprintList.py|Python|Extract blueprints to create bp mod files|
|packBlueprints.ps1|Powershell|Pack Timo's blueprints mod|

## How to create your own Armory Mod  
Say `Dead Cells` is installed under `D:\Program Files (x86)\Steam\steamapps\common\Dead Cells`.

### 1. Prepare game resource files
```powershell
.\preStep.ps1
```

### 2. Use `Tiled` to customize `PrisonFlaskRoom` 
Follow the guide at "Steam\steamapps\common\Dead Cells\ModTools\ModsDoc.pdf".  

Save as the `PrisonFlaskRoom.tmx` to `src\PrisonFlaskRoom.tmx`

### 3. Use "itemList.py" to get weapons and skills names in the game.  
```shell
python3 itemList.py
```
This will generate starter room file named "PrisonFlaskRoom.tmx" and copy it back to `armory-tmx`.  

### 4. Collapse tmx files to binary and Create Mod file.
```powershell
.\packArmory.ps1
```
The mod file is under `workshop\Armory` folder.
