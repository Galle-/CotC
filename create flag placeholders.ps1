# 
# Get name of titles from folder and copy a gfx placeholder with that name to gfx\flags
#
#set path to mod folder
$ck2modfolder = "$env:HOMEPATH\Documents\Paradox Interactive\Crusader Kings II\mod"

#define mod name
$ck2modname = "Crisis of the Confederation"

#path and name of placeholder
$placeholderimage = ".\placeholder.tga"

#directories we need
$flagsdir = "$ck2modfolder\$ck2modname\gfx\flags"
$titlesdir = "$ck2modfolder\$ck2modname\history\titles"

#the magic happens here. get filename without extension from folder and then for each result copy the image
Get-ChildItem $titlesdir|% {$_.BaseName} | ForEach-Object { Copy-Item $placeholderimage "$flagsdir\$_.tga" }
