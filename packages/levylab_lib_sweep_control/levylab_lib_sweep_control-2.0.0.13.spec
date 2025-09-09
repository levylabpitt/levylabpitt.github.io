[Package]
Name="levylab_lib_sweep_control"
Version="2.0.0.13"
Release=""
ID=b66d34f1705cbf770612edeb97996a93
File Format="vip"
Format Version="2017"
Display Name="Sweep Control"


[Description]
Description="[SweepControl.lvclass]\0A- Sweep Control.vi:\0A  - Sequencer for stepping multiple parameters. Calls VIs in Transport.lvclass\0A- Continuous B sweep.vi:\0A  - Sweep B continuously while asynchronously calling VIs in Transport.lvclass"
Summary=""
License=""
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.0.0]\0A#141 Update compatibility with Transport 2.0"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires="levylab_lib_transport>=2.0.1.30"
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
Num Files=34
File 0="user.lib/Levylab/Transport/Sweep Control/Continuous B sweep.vi"
File 1="user.lib/Levylab/Transport/Sweep Control/Process.vi"
File 2="user.lib/Levylab/Transport/Sweep Control/Sweep Control Cartesian.vi"
File 3="user.lib/Levylab/Transport/Sweep Control/Sweep Control.lvclass"
File 4="user.lib/Levylab/Transport/Sweep Control/Sweep Control.TestLauncher.vi"
File 5="user.lib/Levylab/Transport/Sweep Control/Sweep Control.vi"
File 6="user.lib/Levylab/Transport/Sweep Control/Typedefs/Cluster - ScanControl.ctl"
File 7="user.lib/Levylab/Transport/Sweep Control/Typedefs/Cluster - ScanParamters.ctl"
File 8="user.lib/Levylab/Transport/Sweep Control/Typedefs/Cluster - Sweep Control.ctl"
File 9="user.lib/Levylab/Transport/Sweep Control/Typedefs/Continuous B Sweep JSON--Cluster.ctl"
File 10="user.lib/Levylab/Transport/Sweep Control/Typedefs/Enum - Action.ctl"
File 11="user.lib/Levylab/Transport/Sweep Control/Typedefs/Enum - Experiments.ctl"
File 12="user.lib/Levylab/Transport/Sweep Control/Typedefs/Enum - PostAction.ctl"
File 13="user.lib/Levylab/Transport/Sweep Control/Typedefs/Enum - Priority.ctl"
File 14="user.lib/Levylab/Transport/Sweep Control/Typedefs/Lockin Sweep--Cluster.ctl"
File 15="user.lib/Levylab/Transport/Sweep Control/Typedefs/PostAction.ctl"
File 16="user.lib/Levylab/Transport/Sweep Control/Typedefs/ScanControl.ctl"
File 17="user.lib/Levylab/Transport/Sweep Control/Typedefs/ScanParamters.ctl"
File 18="user.lib/Levylab/Transport/Sweep Control/Typedefs/Sweep Control JSON--Cluster.ctl"
File 19="user.lib/Levylab/Transport/Sweep Control/Typedefs/Sweep Control.Dependencies--Cluster.ctl"
File 20="user.lib/Levylab/Transport/Sweep Control/Typedefs/XP Style VISA Control.ctl"
File 21="user.lib/Levylab/Transport/Sweep Control/subVIs/Create Scan.vi"
File 22="user.lib/Levylab/Transport/Sweep Control/subVIs/Post action.vi"
File 23="user.lib/Levylab/Transport/Sweep Control/subVIs/Scan action.vi"
File 24="user.lib/Levylab/Transport/Sweep Control/subVIs/Sort Scan Parameters.vi"
File 25="user.lib/Levylab/Transport/Sweep Control/subVIs/Sweep Control Inner Loop.vi"
File 26="user.lib/Levylab/Transport/Sweep Control/subVIs/Sweep Control Loop.vi"
File 27="user.lib/Levylab/Transport/Sweep Control/API (file)/Read Continuous B Sweep.json.vi"
File 28="user.lib/Levylab/Transport/Sweep Control/API (file)/Read Sweep Control.json.vi"
File 29="user.lib/Levylab/Transport/Sweep Control/API/Read Dependencies.vi"
File 30="user.lib/Levylab/Transport/Sweep Control/API/Read Sweep Configuration Example.vi"
File 31="user.lib/Levylab/Transport/Sweep Control/API/Read Sweep Configuration File.vi"
File 32="user.lib/Levylab/Transport/Sweep Control/API/Take Measurement.vi"
File 33="user.lib/Levylab/Transport/Sweep Control/API/Write Dependencies.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_sweep_control_1.mnu"
File 1="_functions_levylab_lib_sweep_control_2.mnu"
File 2="_functions_levylab_lib_sweep_control_3.mnu"
File 3="functions_Levylab_lib_sweep_control.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
