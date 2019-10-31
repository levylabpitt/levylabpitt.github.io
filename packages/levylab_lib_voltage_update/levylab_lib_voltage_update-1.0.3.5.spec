[Package]
Name="levylab_lib_voltage_update"
Version="1.0.3.5"
Release=""
ID=e525ff3a4f9cd646d6a9f3f842644667
File Format="vip"
Format Version="2017"
Display Name="Voltage Update"


[Description]
Description="Instrument for updating static voltages (e.g. back gates). Can use any DAQ hardware such as USB-4431 or PXI-6120"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.3.5]\0A- Coerce voltage according to configured min/max\0A- Default min/max is now -/+ 10\0A- Return amplified voltage in addition to DAQ output"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


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
Requires=""
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
Num Files=4
File 0="user.lib/LevyLab/Voltage Update/LICENSE"
File 1="user.lib/LevyLab/Voltage Update/README.md"
File 2="user.lib/LevyLab/Voltage Update/Voltage Update.vi"
File 3="user.lib/LevyLab/Voltage Update/VoltageUpdate.lvproj"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Voltage_Update.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
