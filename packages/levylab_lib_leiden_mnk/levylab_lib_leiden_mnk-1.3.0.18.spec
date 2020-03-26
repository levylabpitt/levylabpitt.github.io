[Package]
Name="levylab_lib_leiden_mnk"
Version="1.3.0.18"
Release=""
ID=6e047643f22992364533e48529b3a6dd
File Format="vip"
Format Version="2017"
Display Name="Leiden MNK"


[Description]
Description="Tools used by LevyLab to interact with Leiden MNK Temperature Control (TC)\0A\0A[Instrument.MNK_TC.lvclass]\0A- API that overrides "Get Temperature.vi" method of Instrument.Cryostat.lvclass"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.3.0.187]\0A- build without Write to DSC functions"
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
Requires="levylab_lib_levylab_instruments>=1.5.11.73"
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
Num Files=6
File 0="user.lib/LevyLab/Leiden MNK/Instrument.MNK.lvproj"
File 1="user.lib/LevyLab/Leiden MNK/Instrument.MNK_TC/Instrument.MNK_TC.lvclass"
File 2="user.lib/LevyLab/Leiden MNK/Instrument.MNK_TC/Instrument.MNK_TC.TestLauncher.vi"
File 3="user.lib/LevyLab/Leiden MNK/Instrument.MNK_TC/Process.vi"
File 4="user.lib/LevyLab/Leiden MNK/Instrument.MNK_TC/Private/Read_MNK_Temp_from_DSC.vi"
File 5="user.lib/LevyLab/Leiden MNK/Instrument.MNK_TC/API/Get Temperature.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Leiden_MNK.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
