# 
# Get name of title from file and copy a gfx placeholder with that name to gfx\flags
#
# commandline: scriptname.ps1 filename.txt placeholdername.tga
#
#set path to mod folder
[string]$ck2modfolder = "$env:HOMEPATH\Documents\Paradox Interactive\Crusader Kings II\mod"

#define mod name
[string]$ck2modname = "Crisis of the Confederation"

#directory we need
[string]$ck2flagsdir = "$ck2modfolder\$ck2modname\gfx\flags"

#pass filename as argument
[string]$ck2titles=$args[0]

#pass placeholder filename as argument
[string]$placeholderimage = $args[1]

#the magic happens here. get name from list and then for each result copy the image
Get-Content $ck2titles | ForEach-Object { Copy-Item $placeholderimage "$flagsdir\$_.tga" }
