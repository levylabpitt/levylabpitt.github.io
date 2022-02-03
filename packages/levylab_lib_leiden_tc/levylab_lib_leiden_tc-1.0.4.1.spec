[Package]
Name="levylab_lib_leiden_tc"
Version="1.0.4.1"
Release=""
ID=2e04d57effdfeeb23a465a7ba2d3bad7
File Format="vip"
Format Version="2017"
Display Name="LEIDEN TC"


[Description]
Description="Tools used by LevyLab to interact with Leiden Temperature Control (TC)\0A\0A[Instrument.TC.MNK.lvclass]\0A[Instrument.TC.CF.lvclass]\0A- APIs that overrides "Get Temperature.vi" method of Instrument.Cryostat.lvclass"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2022, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Update to Instrument Framework v1.11.2.1"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


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
Requires="levylab_lib_levylab_instruments>=1.11.2.1"
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
File 0="user.lib/LevyLab/Leiden TC/Instrument.TC.lvproj"
File 1="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Instrument.TC.MNK.lvclass"
File 2="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Instrument.TC.MNK.TestLauncher.vi"
File 3="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Process.vi"
File 4="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Private/Read_MNK_Temperature.vi"
File 5="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/API/Get Temperature.vi"
File 6="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Instrument.TC.CF.lvclass"
File 7="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Instrument.TC.CF.TestLauncher.vi"
File 8="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Process.vi"
File 9="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Private/Read_CF_Temperature.vi"
File 10="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/API/Get Temperature.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Leiden_TC.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
