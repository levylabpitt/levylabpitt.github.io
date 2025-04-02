[Package]
Name="levylab_lib_relay_box"
Version="1.1.0.8"
Release=""
ID=abfc12d2aaa0cbd28e3ded8d0fbdfc2f
File Format="vip"
Format Version="2017"
Display Name="Relay Box"


[Description]
Description=""
Summary=""
License=""
Copyright="Copyright (c) 2019, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="John Maier"
Demo="FALSE"
Release Notes="JKI State Machine version (old version of Set Resistor is still included)\0AUpdated GUI, now with better timing\0ARelay Control is now polymorphic\0A--Comments on read relay and relay control\0A--JKI State Machine is now recognized\0A--Set resistor VI can now be wired to\0A--fixed icon, added terminals for error wiring\0A--Added Read Relay VI\0A--Made Gohm default resistor"
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
Requires=""
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
Num Files=27
File 0="user.lib/LevyLab/Relay Box/Read Resistor.vi"
File 1="user.lib/LevyLab/Relay Box/RelayBox.lvproj"
File 2="user.lib/LevyLab/Relay Box/Set Resistor.vi"
File 3="user.lib/LevyLab/Relay Box/USB Relay Control.vi"
File 4="user.lib/LevyLab/Relay Box/Type_defs/Resistor--enum.ctl"
File 5="user.lib/LevyLab/Relay Box/sub-VIs/Display_EEPROM.vi"
File 6="user.lib/LevyLab/Relay Box/sub-VIs/FT_Close_Device.vi"
File 7="user.lib/LevyLab/Relay Box/sub-VIs/FT_EEPROM_Read.vi"
File 8="user.lib/LevyLab/Relay Box/sub-VIs/FT_EEPROM_Write.vi"
File 9="user.lib/LevyLab/Relay Box/sub-VIs/FT_Get_Device_Description_By_Index.vi"
File 10="user.lib/LevyLab/Relay Box/sub-VIs/FT_Open_Device_By_Index.vi"
File 11="user.lib/LevyLab/Relay Box/sub-VIs/FT_Purge.vi"
File 12="user.lib/LevyLab/Relay Box/sub-VIs/FT_Read_FT232-FT245R_EEPROM.vi"
File 13="user.lib/LevyLab/Relay Box/sub-VIs/FT_Reset_Device.vi"
File 14="user.lib/LevyLab/Relay Box/sub-VIs/FT_Set_Baud_Rate.vi"
File 15="user.lib/LevyLab/Relay Box/sub-VIs/FT_Set_Bit_Mode.vi"
File 16="user.lib/LevyLab/Relay Box/sub-VIs/FT_Set_Data_Characteristics.vi"
File 17="user.lib/LevyLab/Relay Box/sub-VIs/FT_Set_DTR.vi"
File 18="user.lib/LevyLab/Relay Box/sub-VIs/FT_Set_Flow_Control.vi"
File 19="user.lib/LevyLab/Relay Box/sub-VIs/FT_Set_RTS.vi"
File 20="user.lib/LevyLab/Relay Box/sub-VIs/FT_Write_String_Data.vi"
File 21="user.lib/LevyLab/Relay Box/sub-VIs/ftd2xx.dll"
File 22="user.lib/LevyLab/Relay Box/sub-VIs/Port Index Search.vi"
File 23="user.lib/LevyLab/Relay Box/sub-VIs/Read_relay.vi"
File 24="user.lib/LevyLab/Relay Box/sub-VIs/USB Relay Control 256.vi"
File 25="user.lib/LevyLab/Relay Box/sub-VIs/USB Relay Control bool.vi"
File 26="user.lib/LevyLab/Relay Box/old-VIs/Set Resistor old.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_relay_box_1.mnu"
File 1="_functions_levylab_lib_relay_box_2.mnu"
File 2="functions_LevyLab_lib_Relay_Box.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"


[File Group 3]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_controls_levylab_lib_relay_box_1.mnu"
File 1="controls_LevyLab_lib_Relay_Box.mnu"


[File Group 4]
Target Dir="<menus>/Controls/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
