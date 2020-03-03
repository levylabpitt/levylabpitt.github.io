[Package]
Name="levylab_lib_krohn_hite_7008"
Version="1.5.0.26"
Release=""
ID=4f87b0cb5b1b9c7227312cebfd4b71e2
File Format="vip"
Format Version="2017"
Display Name="Krohn-Hite 7008 Drivers"


[Description]
Description="Drivers and control interface for Krohn-Hite 7008 multichannel amplifiers."
Summary=""
License=""
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.5.0.26]\0A- Remove KH_Control.ctl and replace with SetAll\0A- No longer automatically sets bandwidth=ON and coupling=DC\0A- Remove FGVs"
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
Requires="lvh_toolbox>=2.0.0.35,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_file>=1.1.0.4,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,oglib_appcontrol>=4.1.0.7,oglib_file>=4.0.1.22,levylab_lib_levylab_instruments>=1.5.9.71"
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
Num Files=24
File 0="user.lib/LevyLab/Krohn Hite 7008/Instrument.KH7008.lvclass"
File 1="user.lib/LevyLab/Krohn Hite 7008/Instrument.KH7008.TestLauncher.vi"
File 2="user.lib/LevyLab/Krohn Hite 7008/KH Control.vi"
File 3="user.lib/LevyLab/Krohn Hite 7008/KH_Control.lvproj"
File 4="user.lib/LevyLab/Krohn Hite 7008/Process.vi"
File 5="user.lib/LevyLab/Krohn Hite 7008/typedefs/Channel-Enum.ctl"
File 6="user.lib/LevyLab/Krohn Hite 7008/typedefs/Coupling-Enum.ctl"
File 7="user.lib/LevyLab/Krohn Hite 7008/typedefs/Filter-Enum.ctl"
File 8="user.lib/LevyLab/Krohn Hite 7008/typedefs/Gain-Enum.ctl"
File 9="user.lib/LevyLab/Krohn Hite 7008/typedefs/Input Configuration-Enum.ctl"
File 10="user.lib/LevyLab/Krohn Hite 7008/typedefs/MeasurePresets-Enum.ctl"
File 11="user.lib/LevyLab/Krohn Hite 7008/typedefs/SetAll-Array.ctl"
File 12="user.lib/LevyLab/Krohn Hite 7008/typedefs/SetAll-Cluster.ctl"
File 13="user.lib/LevyLab/Krohn Hite 7008/typedefs/Shunt-Enum.ctl"
File 14="user.lib/LevyLab/Krohn Hite 7008/Private/COM Error Checker.vi"
File 15="user.lib/LevyLab/Krohn Hite 7008/Private/I_Gain.vi"
File 16="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 COM.vi"
File 17="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Set All.vi"
File 18="user.lib/LevyLab/Krohn Hite 7008/Private/KH_config.vi"
File 19="user.lib/LevyLab/Krohn Hite 7008/Private/V_Gain.vi"
File 20="user.lib/LevyLab/Krohn Hite 7008/API/Open.vi"
File 21="user.lib/LevyLab/Krohn Hite 7008/API/Read Channel Setting.vi"
File 22="user.lib/LevyLab/Krohn Hite 7008/API/Read Gain.vi"
File 23="user.lib/LevyLab/Krohn Hite 7008/API/Write Channel Setting.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_krohn_hite_7008_1.mnu"
File 1="_functions_levylab_lib_krohn_hite_7008_2.mnu"
File 2="functions_LevyLab_lib_Krohn_Hite_7008.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
