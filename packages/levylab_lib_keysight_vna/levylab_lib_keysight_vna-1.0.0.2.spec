[Package]
Name="levylab_lib_keysight_vna"
Version="1.0.0.2"
Release=""
ID=ba317e08bccb5bf2d3aceaa39ef9efa0
File Format="vip"
Format Version="2017"
Display Name="Keysight VNA"


[Description]
Description="Easy to use VIs for controlling the VNA"
Summary=""
License=""
Copyright="Copyright (c) 2018, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Dengyu"
Demo="FALSE"
Release Notes="update sweep DC to use lockin's API VI"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW>=16.0"
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
Requires="levylab_lib_lvtoitx>=2.6.4.19"
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
Num Files=3
File 0="user.lib/Levylab/Keysight VNA/P9374AEasilyUse_sweepDC.vi"
File 1="user.lib/Levylab/Keysight VNA/P9374AEasilyUse_v5.vi"
File 2="user.lib/Levylab/Keysight VNA/P9374AVNA.lvproj"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Keysight_VNA.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
