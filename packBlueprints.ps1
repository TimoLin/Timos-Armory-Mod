# Collapse tmx files to binary
&'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\TmxTool\TmxTool.exe' -Collapse -TmxBin .\res\tiled\ -TmxXml .\bp-tmx\

# Create mod file
& 'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\PAKTool.exe' -creatediffpak -refpak "D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\res.pak" -indir "D:\Timo\Games\Timos-armory-mod\res\" -OutPak "D:\Timo\Games\Timos-armory-mod\workshop\Blueprints\res.pak"
