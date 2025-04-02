[Package]
Name="levylab_lib_logger"
Version="2.0.0.6"
Release=""
ID=71ca528cd5219492aa8669487025c4b7
File Format="vip"
Format Version="2017"
Display Name="Logger"


[Description]
Description="Abstract datalogger class."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.0.0]\0A- #119 Debug Attribute\0A- #139 SMO 1.4 Error Handler\0A- #140 Macro: Exit\0A- #142 SMO v2.0 lvlib (not lvlibp)"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=2.0.0.73,levylab_lib_build_support>=1.2.5.1"
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
Num Files=9
File 0="user.lib/Levylab/Logger/Logger.lvlib"
File 1="user.lib/Levylab/Logger/Logger/Create Logger.vi"
File 2="user.lib/Levylab/Logger/Logger/Destroy Logger.vi"
File 3="user.lib/Levylab/Logger/Logger/Logger.lvclass"
File 4="user.lib/Levylab/Logger/Logger/Logger.TestLauncher.vi"
File 5="user.lib/Levylab/Logger/Logger/Process.vi"
File 6="user.lib/Levylab/Logger/Logger/Read path.vi"
File 7="user.lib/Levylab/Logger/Logger/State History.vi"
File 8="user.lib/Levylab/Logger/Logger/Write path.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_logger.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
