[Package]
Name="levylab_lib_fileutilities"
Version="1.2.5.12"
Release=""
ID=d47eb15b70dfca9671e29564e49539d3
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
Release Notes="[1.2.5.12]\0D\0A- Issue #2: Improve Increment Filename.vi to better handle special cases such as Filemame.YYYMMDD.txt\0A- Add VI documentation"
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
Num Files=5
File 0="user.lib/LevyLab/FileUtilities/Ignore Hidden Files.vi"
File 1="user.lib/LevyLab/FileUtilities/Increment Filename.vi"
File 2="user.lib/LevyLab/FileUtilities/levylab_util_file.lvproj"
File 3="user.lib/LevyLab/FileUtilities/Number to String.vi"
File 4="user.lib/LevyLab/FileUtilities/Support/Is String Number.vi"


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
