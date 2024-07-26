[Package]
Name="levylab_lib_relay_box"
Version="1.3.0.4"
Release=""
ID=48e9f6b17577e416c833b3954cdca877
File Format="vip"
Format Version="2017"
Display Name="Relay Box"


[Description]
Description="Software to control resistor relay box"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2024, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="John Maier / Patrick Irvin"
Demo="FALSE"
Release Notes="- this release calls the D2XX-LV library rather than D2XX directly"
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
Num Files=45
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
File 12="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CClose Device.vi"
File 13="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CCount Devices.vi"
File 14="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CCurrent VIs Parents Ref__ogtk.vi"
File 15="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CD2XX-lv.lvlib"
File 16="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CD2XX.lvlib"
File 17="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFit VI window to Largest Dec__ogtk.vi"
File 18="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Close_Device.vi"
File 19="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Get_COM_Port_Number.vi"
File 20="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Get_Device_Description_By_Index.vi"
File 21="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Get_Device_Info.vi"
File 22="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Get_Device_Serial_Number_By_Index.vi"
File 23="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Get_Library_Version.vi"
File 24="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Get_Number_of_Devices.vi"
File 25="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Open_Device_By_Serial_Number.vi"
File 26="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Read_EEPROM_User_Area.vi"
File 27="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Set_Baud_Rate.vi"
File 28="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Set_Bit_Mode.vi"
File 29="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Status to Error.vi"
File 30="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Write_EEPROM_User_Area.vi"
File 31="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFT_Write_String_Data.vi"
File 32="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CFTDI_Status_Explanation.vi"
File 33="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CGet Device COM Port.vi"
File 34="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CGet Device Description.vi"
File 35="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CGet Device Info.vi"
File 36="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CGet Device Serial Number.vi"
File 37="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CGet Driver Version.vi"
File 38="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CList Devices.vi"
File 39="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104COpen Device (serial number).vi"
File 40="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CRead EEPROM User Area.vi"
File 41="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CSet Device Baud Rate.vi"
File 42="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CSet Device Bit Mode.vi"
File 43="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CWrite Data (String).vi"
File 44="user.lib/LevyLab/_Relay Box_internal_deps/8E2AB065DB06BB2AA6B360AEF936104CWrite EEPROM User Area.vi"


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
