[Package]
Name="levylab_lib_d2xx_lv"
Version="1.4.0.9"
Release=""
ID=c70ca5af0151f5e05611b0ff67ebfaaa
File Format="vip"
Format Version="2017"
Display Name="D2XX-LV"


[Description]
Description="This library provides an interface to FTDI's D2XX drivers, designed to align more closely with LabVIEW programming conventions."
Summary="Improved LabVIEW interface for FTDI D2XX drivers"
License="BSD-3"
Copyright="Copyright (c) 2026, Levylab"
Distribution=""
Vendor="Levylab"
URL="https://github.com/levylabpitt/D2XX"
Packager="Patrick Irvin / LevyLab"
Demo="FALSE"
Release Notes="Issue #7\0A- improved list devices when multiple devices are present but some are already open"
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
Exclusive_OS="Windows NT"


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
Requires="ftdi_lib_d2xx>=1.3.0.8"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="2"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=33
File 0="instr.lib/_D2XX/D2XX-LV/D2XX-lv.lvlib"
File 1="instr.lib/_D2XX/D2XX-LV/typedefs/Device Info.ctl"
File 2="instr.lib/_D2XX/D2XX-LV/Tests/Test D2XX.vi"
File 3="instr.lib/_D2XX/D2XX-LV/private/FT_Status to Error.vi"
File 4="instr.lib/_D2XX/D2XX-LV/API/Close Device.vi"
File 5="instr.lib/_D2XX/D2XX-LV/API/Count Devices.vi"
File 6="instr.lib/_D2XX/D2XX-LV/API/Get Device COM Port.vi"
File 7="instr.lib/_D2XX/D2XX-LV/API/Get Device Description.vi"
File 8="instr.lib/_D2XX/D2XX-LV/API/Get Device Info.vi"
File 9="instr.lib/_D2XX/D2XX-LV/API/Get Device Serial Number.vi"
File 10="instr.lib/_D2XX/D2XX-LV/API/Get Driver Version.vi"
File 11="instr.lib/_D2XX/D2XX-LV/API/List Devices.vi"
File 12="instr.lib/_D2XX/D2XX-LV/API/Open Device (index).vi"
File 13="instr.lib/_D2XX/D2XX-LV/API/Open Device (serial number).vi"
File 14="instr.lib/_D2XX/D2XX-LV/API/Open Device.vi"
File 15="instr.lib/_D2XX/D2XX-LV/API/Purge Device Buffers.vi"
File 16="instr.lib/_D2XX/D2XX-LV/API/Read Data (Byte Array).vi"
File 17="instr.lib/_D2XX/D2XX-LV/API/Read Data (String).vi"
File 18="instr.lib/_D2XX/D2XX-LV/API/Read Data.vi"
File 19="instr.lib/_D2XX/D2XX-LV/API/Read EEPROM User Area.vi"
File 20="instr.lib/_D2XX/D2XX-LV/API/Reset Device.vi"
File 21="instr.lib/_D2XX/D2XX-LV/API/Set Device Baud Rate.vi"
File 22="instr.lib/_D2XX/D2XX-LV/API/Set Device Bit Mode.vi"
File 23="instr.lib/_D2XX/D2XX-LV/API/Set Device Data Characteristics.vi"
File 24="instr.lib/_D2XX/D2XX-LV/API/Set Device DTR.vi"
File 25="instr.lib/_D2XX/D2XX-LV/API/Set Device Flow Control.vi"
File 26="instr.lib/_D2XX/D2XX-LV/API/Set Device RTS.vi"
File 27="instr.lib/_D2XX/D2XX-LV/API/Write Data (Byte Array).vi"
File 28="instr.lib/_D2XX/D2XX-LV/API/Write Data (String).vi"
File 29="instr.lib/_D2XX/D2XX-LV/API/Write Data.vi"
File 30="instr.lib/_D2XX/D2XX-LV/API/Write EEPROM User Area.vi"
File 31="examples/D2XX/D2XX-LV/example/List Devices Example.vi"
File 32="examples/D2XX/D2XX-LV/example/Read Write String Data Example.vi"


[File Group 1]
Target Dir="<instr.lib>/D2XX"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_d2xx_lv_1.mnu"
File 1="functions_Levylab_lib_D2XX_LV.mnu"
