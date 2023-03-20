Timo's Armory Mod
=================
[![Timo's BluePrints Mod](https://img.shields.io/badge/Timo's%20BluePrints%20Mod-V3.3-blue)](https://steamcommunity.com/sharedfiles/filedetails/?id=2399579218)
[![Timo's Armory Mod](https://img.shields.io/badge/Timo's%20Armory%20Mod-V2.8-blue)](https://steamcommunity.com/sharedfiles/filedetails/?id=2389535625)

## Demo
![Screenshot](https://steamuserimages-a.akamaihd.net/ugc/1763693190280213490/B6F9216707B83D1890831D8A43331102D5A209B3/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false)

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
