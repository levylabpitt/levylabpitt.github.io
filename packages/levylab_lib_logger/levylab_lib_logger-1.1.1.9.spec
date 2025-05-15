[Package]
Name="levylab_lib_logger"
Version="1.1.1.9"
Release=""
ID=1f78fe15f367dacf103af7eab81b8d9a
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
Release Notes="[1.1.1]\0A- #165 adjust package dependencies"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,oglib_string>=5.0.0.25"
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
