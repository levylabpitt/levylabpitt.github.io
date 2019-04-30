[Package]
Name="levylab_lib_fileutilities"
Version="1.2.3.9"
Release=""
ID=494ec19bff7e4856070449ec556586fa
File Format="vip"
Format Version="2017"
Display Name="FileUtilities"


[Description]
Description="Utilities for working with files and folders\0A\0A* DirExists-NoThenCreate.vi\0A  * Checks if a directory exists, if not one is created\0A* Format number_123.vi\0A  * takes a number and appends zeros to make 3 digits long (1 becomes 001, 25 becomes 025, 531 remains 531.)\0A* Format number_123456.vi\0A  * takes a number and appends zeros to make 6 digits long (1 becomes 000001, 25 becomes 000025, 531 becomes 000531, etc)\0A* Format number_1234567890.vi\0A  * same idea as previous but has a control for how many digits to add\0A* Ignore Hidden Files.vi\0A  * Removes hidden files (.hidden) from an array of files names\0A* increment filename.vi\0A  * If file.0.txt already exists change the path to file.1.txt, etc."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.2.3.9]\0A- update icons\0A- add LICENSE\0A- add README"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


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
Num Files=8
File 0="user.lib/LevyLab/FileUtilities/DirExists-NoThenCreate.vi"
File 1="user.lib/LevyLab/FileUtilities/FilePath.glb.vi"
File 2="user.lib/LevyLab/FileUtilities/Format number_123.vi"
File 3="user.lib/LevyLab/FileUtilities/Format number_123456.vi"
File 4="user.lib/LevyLab/FileUtilities/Format number_1234567890.vi"
File 5="user.lib/LevyLab/FileUtilities/Ignore Hidden Files.vi"
File 6="user.lib/LevyLab/FileUtilities/increment filename.vi"
File 7="user.lib/LevyLab/FileUtilities/levylab_util_file.lvproj"


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
