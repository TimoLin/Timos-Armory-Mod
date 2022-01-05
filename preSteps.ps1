# Clean old folders
Remove-Item '.\org-res', '.\res', '.\armory-tmx', '.\bp-tmx', '.\ExpandedCDB-BP' -Recurse

# Expand res package
&  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\PAKTool.exe' -Expand -OutDir .\org-res -RefPak  "D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\res.pak"

# Copy folder
copy-item -path ".\org-res" -destination ".\res" -Recurse

# Extract tmx files from binary
&  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\TmxTool\TmxTool.exe' -Expand -TmxBin .\org-res\tiled  -TmxXml .\armory-tmx\

&  'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\TmxTool\TmxTool.exe' -Expand -TmxBin .\org-res\tiled  -TmxXml .\bp-tmx\

# Expand data cdb
& 'D:\Program Files (x86)\Steam\steamapps\common\Dead Cells\ModTools\CDBTool.exe' -Expand -Outdir .\ExpandedCDB-BP -refcdb ".\res\data.cdb"
