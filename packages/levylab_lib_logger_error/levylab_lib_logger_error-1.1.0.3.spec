[Package]
Name="levylab_lib_logger_error"
Version="1.1.0.3"
Release=""
ID=36b8158643238ecc93a02a065753cae8
File Format="vip"
Format Version="2017"
Display Name="Logger.Error"


[Description]
Description="Error datalogger class."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2024, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.1.0]\0A- Issue #121 use debug attribute"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_lvdata>=5.0.0.27,oglib_string>=5.0.0.25,levylab_lib_build_support>=1.2.5.1"
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
Num Files=12
File 0="user.lib/Levylab/Logger.Error/Create Logger.vi"
File 1="user.lib/Levylab/Logger.Error/Destroy Logger.vi"
File 2="user.lib/Levylab/Logger.Error/Error Cluster to Array.vi"
File 3="user.lib/Levylab/Logger.Error/Get SMO Name from Error Event.vi"
File 4="user.lib/Levylab/Logger.Error/Initialize Error Log.vi"
File 5="user.lib/Levylab/Logger.Error/Logger.Error.lvclass"
File 6="user.lib/Levylab/Logger.Error/Logger.Error.lvproj"
File 7="user.lib/Levylab/Logger.Error/Logger.Error.TestLauncher.vi"
File 8="user.lib/Levylab/Logger.Error/Process.vi"
File 9="user.lib/Levylab/Logger.Error/Read Class from Error.vi"
File 10="user.lib/Levylab/Logger.Error/Write Class to Error.vi"
File 11="user.lib/Levylab/Logger.Error/Write Dependencies.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_logger_error.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
