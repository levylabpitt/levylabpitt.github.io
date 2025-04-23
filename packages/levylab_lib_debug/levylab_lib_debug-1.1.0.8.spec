[Package]
Name="levylab_lib_debug"
Version="1.1.0.8"
Release=""
ID=15052d9149e94d4b4ecaa56afa74bcc1
File Format="vip"
Format Version="2017"
Display Name="Debug"


[Description]
Description="Shared Debug SMO Attribute"
Summary="Shared Debug SMO Attribute"
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.1.0]\0A- Change to SMO v1.4"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=19.0"
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
Requires="jki_statemachineobjects>=1.4.0.69"
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
Num Files=10
File 0="user.lib/Levylab/Debug/Debug.lvlib"
File 1="user.lib/Levylab/Debug/SMO.Mediator/Get Debug Attribute.vi"
File 2="user.lib/Levylab/Debug/SMO.Mediator/Set Debug Attribute.vi"
File 3="user.lib/Levylab/Debug/SMO.Mediator/SMO.Mediator.lvclass"
File 4="user.lib/Levylab/Debug/Debug/Get Debug Mode.vi"
File 5="user.lib/Levylab/Debug/Debug/Set Debug Mode.vi"
File 6="user.lib/Levylab/Debug/Attribute.Debug/Attribute.Debug.lvclass"
File 7="user.lib/Levylab/Debug/Attribute.Debug/DebugBehavior.ctl"
File 8="user.lib/Levylab/Debug/Attribute.Debug/Initialize Debug Attribute.vi"
File 9="user.lib/Levylab/Debug/Attribute.Debug/Read Debug Behavior.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_debug.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
