[Package]
Name="levylab_lib_d2xx_lv"
Version="1.2.0.6"
Release=""
ID=e51ec3982217f30bcccb0e8040ad7dab
File Format="vip"
Format Version="2017"
Display Name="D2XX-LV"


[Description]
Description="This library provides an interface to FTDI's D2XX drivers, designed to align more closely with LabVIEW programming conventions."
Summary="Improved LabVIEW interface for FTDI D2XX drivers"
License="BSD-3"
Copyright="Copyright (c) 2024, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/D2XX"
Packager="Patrick Irvin / LevyLab"
Demo="FALSE"
Release Notes="- add support for 64 bit library (Issue #4)"
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
Requires="ftdi_lib_d2xx>=1.2.0.5"
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
Num Files=33
File 0="user.lib/Levylab/D2XX-LV/D2XX-lv.lvlib"
File 1="user.lib/Levylab/D2XX-LV/typedefs/Device Info.ctl"
File 2="user.lib/Levylab/D2XX-LV/Tests/Test D2XX.vi"
File 3="user.lib/Levylab/D2XX-LV/private/FT_Status to Error.vi"
File 4="user.lib/Levylab/D2XX-LV/private/Open Device (index).vi"
File 5="user.lib/Levylab/D2XX-LV/private/Open Device (serial number).vi"
File 6="user.lib/Levylab/D2XX-LV/private/Read Data (Byte Array).vi"
File 7="user.lib/Levylab/D2XX-LV/private/Read Data (String).vi"
File 8="user.lib/Levylab/D2XX-LV/private/Write Data (Byte Array).vi"
File 9="user.lib/Levylab/D2XX-LV/private/Write Data (String).vi"
File 10="user.lib/Levylab/D2XX-LV/example/List Devices Example.vi"
File 11="user.lib/Levylab/D2XX-LV/example/Read Write String Data Example.vi"
File 12="user.lib/Levylab/D2XX-LV/API/Close Device.vi"
File 13="user.lib/Levylab/D2XX-LV/API/Count Devices.vi"
File 14="user.lib/Levylab/D2XX-LV/API/Get Device COM Port.vi"
File 15="user.lib/Levylab/D2XX-LV/API/Get Device Description.vi"
File 16="user.lib/Levylab/D2XX-LV/API/Get Device Info.vi"
File 17="user.lib/Levylab/D2XX-LV/API/Get Device Serial Number.vi"
File 18="user.lib/Levylab/D2XX-LV/API/Get Driver Version.vi"
File 19="user.lib/Levylab/D2XX-LV/API/List Devices.vi"
File 20="user.lib/Levylab/D2XX-LV/API/Open Device.vi"
File 21="user.lib/Levylab/D2XX-LV/API/Purge Device Buffers.vi"
File 22="user.lib/Levylab/D2XX-LV/API/Read Data.vi"
File 23="user.lib/Levylab/D2XX-LV/API/Read EEPROM User Area.vi"
File 24="user.lib/Levylab/D2XX-LV/API/Reset Device.vi"
File 25="user.lib/Levylab/D2XX-LV/API/Set Device Baud Rate.vi"
File 26="user.lib/Levylab/D2XX-LV/API/Set Device Bit Mode.vi"
File 27="user.lib/Levylab/D2XX-LV/API/Set Device Data Characteristics.vi"
File 28="user.lib/Levylab/D2XX-LV/API/Set Device DTR.vi"
File 29="user.lib/Levylab/D2XX-LV/API/Set Device Flow Control.vi"
File 30="user.lib/Levylab/D2XX-LV/API/Set Device RTS.vi"
File 31="user.lib/Levylab/D2XX-LV/API/Write Data.vi"
File 32="user.lib/Levylab/D2XX-LV/API/Write EEPROM User Area.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=3
File 0="_functions_levylab_lib_d2xx_lv_1.mnu"
File 1="_functions_levylab_lib_d2xx_lv_2.mnu"
File 2="functions_Levylab_lib_D2XX_LV.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
