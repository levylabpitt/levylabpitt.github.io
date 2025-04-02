[Package]
Name="levylab_lib_debug"
Version="1.0.0.1"
Release=""
ID=bf6141757e9c226d4a7857c369c0e44c
File Format="vip"
Format Version="2017"
Display Name="Debug"


[Description]
Description="Shared Debug SMO Attribute"
Summary="Shared Debug SMO Attribute"
License="BSD-3"
Copyright="Copyright (c) 2024, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes=""
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW x86>=19.0"
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
Num File Groups="5"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=10
File 0="user.lib/Levylab/Configuration/Debug.lvlib"
File 1="user.lib/Levylab/Configuration/Get Debug Mode.vi"
File 2="user.lib/Levylab/Configuration/Set Debug Mode.vi"
File 3="user.lib/Levylab/Configuration/subsystems/SMO.Mediator/Get Debug Attribute.vi"
File 4="user.lib/Levylab/Configuration/subsystems/SMO.Mediator/Set Debug Attribute.vi"
File 5="user.lib/Levylab/Configuration/subsystems/SMO.Mediator/SMO.Mediator.lvclass"
File 6="user.lib/Levylab/Configuration/subsystems/Attribute.Debug/Attribute.Debug.lvclass"
File 7="user.lib/Levylab/Configuration/subsystems/Attribute.Debug/DebugBehavior.ctl"
File 8="user.lib/Levylab/Configuration/subsystems/Attribute.Debug/Initialize Debug Attribute.vi"
File 9="user.lib/Levylab/Configuration/subsystems/Attribute.Debug/Read Debug Behavior.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_debug_1.mnu"
File 1="_functions_levylab_lib_debug_2.mnu"
File 2="_functions_levylab_lib_debug_3.mnu"
File 3="functions_Levylab_lib_debug.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"


[File Group 3]
Target Dir="<menus>/Controls/Levylab"
Replace Mode="Always"
Num Files=3
File 0="_controls_levylab_lib_debug_1.mnu"
File 1="_controls_levylab_lib_debug_2.mnu"
File 2="controls_Levylab_lib_debug.mnu"


[File Group 4]
Target Dir="<menus>/Controls/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
