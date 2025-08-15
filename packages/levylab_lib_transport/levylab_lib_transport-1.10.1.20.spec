[Package]
Name="levylab_lib_transport"
Version="1.10.1.20"
Release=""
ID=7165043cca586cefd03837c4ce68285c
File Format="vip"
Format Version="2017"
Display Name="Transport"


[Description]
Description="VIs for scripting and performing transport measurments.\0A\0A[Transport.lvclass]\0ABasic transport measurments:\0A- Lockin vs time (Lockin_time.vi)\0A- Lockin Sweep Mode (Lockin_sweep.vi)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.10.1]\0A#130 Fix LockinTime saving multiple TDMS files upon startup (@pgwijesinghe)"
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
Requires="levylab_lib_control_experiment>=1.3.2.18"
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
Num Files=23
File 0="user.lib/Levylab/Transport/Transport/Lockin_AIWFM_time.vi"
File 1="user.lib/Levylab/Transport/Transport/Lockin_sweep.vi"
File 2="user.lib/Levylab/Transport/Transport/Lockin_time.vi"
File 3="user.lib/Levylab/Transport/Transport/Sweep_AIWFM_time.vi"
File 4="user.lib/Levylab/Transport/Transport/THz_TimeDelay.vi"
File 5="user.lib/Levylab/Transport/Transport/Transport.lvclass"
File 6="user.lib/Levylab/Transport/Transport/Typedefs/Lockin_Sweep JSON--Cluster.ctl"
File 7="user.lib/Levylab/Transport/Transport/Typedefs/Transport.Dependencies--Cluster.ctl"
File 8="user.lib/Levylab/Transport/Transport/Private/Calculate R and G (Four Terminal).vi"
File 9="user.lib/Levylab/Transport/Transport/Private/Calculate R and G (Two Terminal).vi"
File 10="user.lib/Levylab/Transport/Transport/Private/Calculate R and G 2.vi"
File 11="user.lib/Levylab/Transport/Transport/Private/Exec State to Append.vi"
File 12="user.lib/Levylab/Transport/Transport/Private/Graph Lockin vs Parameter.vi"
File 13="user.lib/Levylab/Transport/Transport/Private/Graph R and G vs Parameter.vi"
File 14="user.lib/Levylab/Transport/Transport/Private/Results (2D) to X and Y Arrays.vi"
File 15="user.lib/Levylab/Transport/Transport/Private/Results (Dictionary) to X and Y Arrays.vi"
File 16="user.lib/Levylab/Transport/Transport/Private/State History.vi"
File 17="user.lib/Levylab/Transport/Transport/API (file)/Read Lockin_Sweep.json.vi"
File 18="user.lib/Levylab/Transport/Transport/API (class)/Read Dependencies.vi"
File 19="user.lib/Levylab/Transport/Transport/API (class)/Write Configure Sweep.vi"
File 20="user.lib/Levylab/Transport/Transport/API (class)/Write Dependencies.vi"
File 21="user.lib/Levylab/Transport/Transport/API (class)/Write notifier.vi"
File 22="user.lib/Levylab/Transport/Transport/API (class)/Write Sweep Table.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_transport_1.mnu"
File 1="_functions_levylab_lib_transport_2.mnu"
File 2="_functions_levylab_lib_transport_3.mnu"
File 3="functions_Levylab_lib_Transport.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
