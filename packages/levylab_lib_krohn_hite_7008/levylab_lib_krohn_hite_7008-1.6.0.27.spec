[Package]
Name="levylab_lib_krohn_hite_7008"
Version="1.6.0.27"
Release=""
ID=a85868982def52ff66df059e953a13b0
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
Release Notes="[1.6.0]\0A- enable new shunt resistor configuration:\0A-- A variant: open/50/500/5k/50k\0A-- B variant: open/50/5k/50k/10M\0A- APIs are provided for enabling one or the other mode\0A- updated package dependencies"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,labview-zmq>=3.5.1.109,lava_lib_ui_tools>=1.4.1.74,lvh_toolbox>=2.0.0.35,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_levylab_instruments>=1.5.9.71"
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
Num Files=27
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
File 14="user.lib/LevyLab/Krohn Hite 7008/Tests/Test SR configuration.vi"
File 15="user.lib/LevyLab/Krohn Hite 7008/Private/COM Error Checker.vi"
File 16="user.lib/LevyLab/Krohn Hite 7008/Private/I_Gain.vi"
File 17="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 COM.vi"
File 18="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Set All.vi"
File 19="user.lib/LevyLab/Krohn Hite 7008/Private/KH_config.vi"
File 20="user.lib/LevyLab/Krohn Hite 7008/Private/V_Gain.vi"
File 21="user.lib/LevyLab/Krohn Hite 7008/API/Open.vi"
File 22="user.lib/LevyLab/Krohn Hite 7008/API/Read Channel Setting.vi"
File 23="user.lib/LevyLab/Krohn Hite 7008/API/Read Gain.vi"
File 24="user.lib/LevyLab/Krohn Hite 7008/API/Shunt - 500 or 10M Control Disable.vi"
File 25="user.lib/LevyLab/Krohn Hite 7008/API/Shunt - Check 500 or 10M.vi"
File 26="user.lib/LevyLab/Krohn Hite 7008/API/Write Channel Setting.vi"


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
