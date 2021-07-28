&  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\PAKTool.exe' -Expand -OutDir .\org-res -RefPak  "D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\res.pak"

&  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\TmxTool\TmxTool.exe' -Expand -TmxBin .\org-res\tiled  -TmxXml .\armory-tmx\

&  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\TmxTool\TmxTool.exe' -Expand -TmxBin .\org-res\tiled  -TmxXml .\bp-tmx\

&  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\PAKTool.exe' -Expand -OutDir .\res -RefPak  "D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\res.pak"
