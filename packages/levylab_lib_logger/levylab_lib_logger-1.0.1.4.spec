[Package]
Name="levylab_lib_logger"
Version="1.0.1.4"
Release=""
ID=c3edd7e276b784884323c7657695c59f
File Format="vip"
Format Version="2017"
Display Name="Logger"


[Description]
Description="Abstract datalogger class."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.1]\0A- Add State History VI"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,levylab_lib_build_support>=1.2.5.1"
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
Num Files=11
File 0="user.lib/Levylab/Logger/Create Logger.vi"
File 1="user.lib/Levylab/Logger/Destroy Logger.vi"
File 2="user.lib/Levylab/Logger/Logger.lvclass"
File 3="user.lib/Levylab/Logger/Logger.lvproj"
File 4="user.lib/Levylab/Logger/Logger.TestLauncher.vi"
File 5="user.lib/Levylab/Logger/Process_DoNotRun.vi"
File 6="user.lib/Levylab/Logger/Read Debug Mode.vi"
File 7="user.lib/Levylab/Logger/Read path.vi"
File 8="user.lib/Levylab/Logger/State History.vi"
File 9="user.lib/Levylab/Logger/Write Debug Mode.vi"
File 10="user.lib/Levylab/Logger/Write path.vi"


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
