[Package]
Name="levylab_lib_logger"
Version="1.0.0.2"
Release=""
ID=0cebd94a7ee97f226a6f764f1fa80acf
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
Release Notes="[1.0.0]\0A- First build as stand-alone package (previously included in Instrument Framework)"
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
Num Files=10
File 0="user.lib/Levylab/Configuration/Create Logger.vi"
File 1="user.lib/Levylab/Configuration/Destroy Logger.vi"
File 2="user.lib/Levylab/Configuration/Logger.lvclass"
File 3="user.lib/Levylab/Configuration/Logger.lvproj"
File 4="user.lib/Levylab/Configuration/Logger.TestLauncher.vi"
File 5="user.lib/Levylab/Configuration/Process_DoNotRun.vi"
File 6="user.lib/Levylab/Configuration/Read Debug Mode.vi"
File 7="user.lib/Levylab/Configuration/Read path.vi"
File 8="user.lib/Levylab/Configuration/Write Debug Mode.vi"
File 9="user.lib/Levylab/Configuration/Write path.vi"


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
