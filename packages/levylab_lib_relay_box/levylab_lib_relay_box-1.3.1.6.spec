[Package]
Name="levylab_lib_relay_box"
Version="1.3.1.6"
Release=""
ID=38e7cbbe46dc4f34a6a89f4d665fc435
File Format="vip"
Format Version="2017"
Display Name="Relay Box"


[Description]
Description="Software to control resistor relay box"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="John Maier / Patrick Irvin"
Demo="FALSE"
Release Notes="- fix instrument handle: U32 to U64\0A\0A(@nefrro)"
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
Requires="levylab_lib_d2xx_lv>=1.2.0.6"
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
File 0="user.lib/LevyLab/Relay Box/Relay-Box.lvclass"
File 1="user.lib/LevyLab/Relay Box/RelayBox.lvproj"
File 2="user.lib/LevyLab/Relay Box/Typedefs/Resistor--enum.ctl"
File 3="user.lib/LevyLab/Relay Box/subVIs/Close.vi"
File 4="user.lib/LevyLab/Relay Box/subVIs/Control Relay (256).vi"
File 5="user.lib/LevyLab/Relay Box/subVIs/Control Relay (boolean).vi"
File 6="user.lib/LevyLab/Relay Box/subVIs/Control Relay.vi"
File 7="user.lib/LevyLab/Relay Box/subVIs/Initialize.vi"
File 8="user.lib/LevyLab/Relay Box/subVIs/Read EEPROM.vi"
File 9="user.lib/LevyLab/Relay Box/subVIs/Read Relay.vi"
File 10="user.lib/LevyLab/Relay Box/API/Read Resistor.vi"
File 11="user.lib/LevyLab/Relay Box/API/Set Resistor.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Relay_Box.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
