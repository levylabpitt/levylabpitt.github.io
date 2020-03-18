[Package]
Name="levylab_lib_fileutilities"
Version="1.2.4.11"
Release=""
ID=cd0cf1bebb32c1e76a58dc32defbf8fa
File Format="vip"
Format Version="2017"
Display Name="FileUtilities"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.4.11]\0A- Fix bugs in Increment Filename.vi"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=16.0"
Exclusive_LabVIEW_System="ALL"
Exclusive_OS="ALL"


[Script VIs]
PreInstall=""
PostInstall=""
PreUninstall=""
PostUninstall=""
Verify=""
PreBuild=""
PostBuild=""


[Dependencies]
AutoReqProv=FALSE
Requires=""
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="3"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=4
File 0="user.lib/LevyLab/FileUtilities/Ignore Hidden Files.vi"
File 1="user.lib/LevyLab/FileUtilities/Increment Filename.vi"
File 2="user.lib/LevyLab/FileUtilities/levylab_util_file.lvproj"
File 3="user.lib/LevyLab/FileUtilities/Number to String.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_FileUtilities.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
