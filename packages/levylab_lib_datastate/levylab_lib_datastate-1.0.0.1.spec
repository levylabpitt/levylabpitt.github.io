[Package]
Name="levylab_lib_datastate"
Version="1.0.0.1"
Release=""
ID=5c41a20d4d9221b98222b025e3cf114f
File Format="vip"
Format Version="2010"
Display Name="DataState"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2012, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Jeremy Levy"
Demo="FALSE"
Release Notes=""
System Package="FALSE"


[Platform]
Exclusive_LabVIEW_Version=">=11.0"
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
Num File Groups="2"
Sub-Packages=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=1
File 0="user.lib/LevyLab/DataState/DataStateArray.glb.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=1
File 0="functions_levylab_lib_datastate.mnu"
