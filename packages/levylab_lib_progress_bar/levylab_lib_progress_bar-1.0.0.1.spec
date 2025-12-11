[Package]
Name="levylab_lib_progress_bar"
Version="1.0.0.1"
Release=""
ID=7f92bad500770d82beb7443be53dc7ba
File Format="vip"
Format Version="2017"
Display Name="Progress Bar"


[Description]
Description="Simple progress bar using JKI SMOs."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.0]\0D\0A- This is the first stand-alone build of 'Progress Bar.' It was previously included as part of the 'build-support' package."
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
Requires="jki_statemachineobjects>=1.4.0.69,oglib_appcontrol>=4.1.0.7"
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
File 0="user.lib/Levylab/Progress Bar/ProgressBar/Process.vi"
File 1="user.lib/Levylab/Progress Bar/ProgressBar/ProgressBar.lvclass"
File 2="user.lib/Levylab/Progress Bar/ProgressBar/ProgressBar.TestLauncher.vi"
File 3="user.lib/Levylab/Progress Bar/ProgressBar/Typedefs/PrivateEvents--Cluster.ctl"
File 4="user.lib/Levylab/Progress Bar/ProgressBar/Private/ProgressBar.GetPrivateEvents.vi"
File 5="user.lib/Levylab/Progress Bar/ProgressBar/Overrides/CreatePrivateEvents.vi"
File 6="user.lib/Levylab/Progress Bar/ProgressBar/Overrides/DestroyPrivateEvents.vi"
File 7="user.lib/Levylab/Progress Bar/ProgressBar/API/Destroy ProgressBar.vi"
File 8="user.lib/Levylab/Progress Bar/ProgressBar/API/Initialize ProgressBar.vi"
File 9="user.lib/Levylab/Progress Bar/ProgressBar/API/Send Message.vi"
File 10="user.lib/Levylab/Progress Bar/ProgressBar/API/Send Progress and Message.vi"
File 11="user.lib/Levylab/Progress Bar/ProgressBar/API/Send Progress.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_progress_bar_1.mnu"
File 1="_functions_levylab_lib_progress_bar_2.mnu"
File 2="_functions_levylab_lib_progress_bar_3.mnu"
File 3="functions_Levylab_lib_progress_bar.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
