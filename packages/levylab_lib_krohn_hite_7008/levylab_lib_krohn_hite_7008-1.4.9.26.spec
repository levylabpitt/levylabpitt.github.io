[Package]
Name="levylab_lib_krohn_hite_7008"
Version="1.4.9.26"
Release=""
ID=9a57378ad03077ba230a20738b19ac56
File Format="vip"
Format Version="2017"
Display Name="Krohn-Hite 7008 Drivers"


[Description]
Description="Drivers and control interface for Krohn-Hite 7008 multichannel amplifiers."
Summary=""
License=""
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick"
Demo="FALSE"
Release Notes="[1.4.9.26]\0A- Show front panel when called as subVI; close afterwards\0A- change the way VI refernces are closed after calling"
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
Requires="lvh_toolbox>=2.0.0.35,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_file>=1.1.0.4,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,oglib_appcontrol>=4.1.0.7,oglib_file>=4.0.1.22,levylab_lib_levylab_instruments>=1.2.4.37"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="5"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=29
File 0="user.lib/LevyLab/Krohn Hite 7008/Create KH Control.vi"
File 1="user.lib/LevyLab/Krohn Hite 7008/Instrument.KH7008.lvclass"
File 2="user.lib/LevyLab/Krohn Hite 7008/Instrument.KH7008.TestLauncher.vi"
File 3="user.lib/LevyLab/Krohn Hite 7008/KH Control.vi"
File 4="user.lib/LevyLab/Krohn Hite 7008/KH_Control.lvproj"
File 5="user.lib/LevyLab/Krohn Hite 7008/Process.vi"
File 6="user.lib/LevyLab/Krohn Hite 7008/Read Channel Setting.vi"
File 7="user.lib/LevyLab/Krohn Hite 7008/Read Gain.vi"
File 8="user.lib/LevyLab/Krohn Hite 7008/Write Address.vi"
File 9="user.lib/LevyLab/Krohn Hite 7008/Write Channel Setting.vi"
File 10="user.lib/LevyLab/Krohn Hite 7008/typedefs/Channel-Enum.ctl"
File 11="user.lib/LevyLab/Krohn Hite 7008/typedefs/Coupling-Enum.ctl"
File 12="user.lib/LevyLab/Krohn Hite 7008/typedefs/Filter-Enum.ctl"
File 13="user.lib/LevyLab/Krohn Hite 7008/typedefs/Gain-Enum.ctl"
File 14="user.lib/LevyLab/Krohn Hite 7008/typedefs/Input Configuration-Enum.ctl"
File 15="user.lib/LevyLab/Krohn Hite 7008/typedefs/KH_control.ctl"
File 16="user.lib/LevyLab/Krohn Hite 7008/typedefs/KH_control_array.ctl"
File 17="user.lib/LevyLab/Krohn Hite 7008/typedefs/Measure-Enum.ctl"
File 18="user.lib/LevyLab/Krohn Hite 7008/typedefs/SetAll-Cluster.ctl"
File 19="user.lib/LevyLab/Krohn Hite 7008/typedefs/Shunt-Enum.ctl"
File 20="user.lib/LevyLab/Krohn Hite 7008/subVIs/COM Error Checker.vi"
File 21="user.lib/LevyLab/Krohn Hite 7008/subVIs/I_Gain.vi"
File 22="user.lib/LevyLab/Krohn Hite 7008/subVIs/KH7008 COM.vi"
File 23="user.lib/LevyLab/Krohn Hite 7008/subVIs/KH7008 Set All.vi"
File 24="user.lib/LevyLab/Krohn Hite 7008/subVIs/V_Gain.vi"
File 25="user.lib/LevyLab/Krohn Hite 7008/globals/config.ini"
File 26="user.lib/LevyLab/Krohn Hite 7008/globals/FGV - KH Gain.vi"
File 27="user.lib/LevyLab/Krohn Hite 7008/globals/FGV - KH Settings.vi"
File 28="user.lib/LevyLab/Krohn Hite 7008/globals/KH_config.vi"


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


[File Group 3]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_krohn_hite_7008_1.mnu"
File 1="controls_LevyLab_lib_Krohn_Hite_7008.mnu"


[File Group 4]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
