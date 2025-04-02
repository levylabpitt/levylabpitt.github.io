[Package]
Name="oxford_lib_ips120"
Version="1.3.1.16"
Release=""
ID=5023aa94f0ffa21a88b9361a6f71d8f7
File Format="vip"
Format Version="2017"
Display Name="Oxford IPS120"


[Description]
Description="Application and drivers for Oxford IPS 120-10 superconducting magnet power supply that is used on the DR200 dilution refrigerator."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, Oxford"
Distribution=""
Vendor="Oxford"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.3.1.16]\0A- SMO was excluded from previous build"
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
Requires="jki_statemachineobjects>=1.3.0.56,oglib_appcontrol>=4.1.0.7,oglib_error>=4.2.0.23,oglib_time>=4.0.1.3,levylab_lib_levylab_instruments>=1.4.1.52"
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
Num Files=60
File 0="user.lib/Oxford/IPS120/IPS-120.lvlib"
File 1="user.lib/Oxford/IPS120/Oxford-IPS120-Main.lvproj"
File 2="user.lib/Oxford/IPS120/SMOs/IPS120/IPS120.lvclass"
File 3="user.lib/Oxford/IPS120/SMOs/IPS120/IPS120.TestLauncher.vi"
File 4="user.lib/Oxford/IPS120/SMOs/IPS120/Oxford-IPS120-Main.vi"
File 5="user.lib/Oxford/IPS120/SMOs/IPS120/Process.vi"
File 6="user.lib/Oxford/IPS120/SMOs/IPS120/API/Get Magnet Field.vi"
File 7="user.lib/Oxford/IPS120/SMOs/IPS120/API/Set Magnet Field.vi"
File 8="user.lib/Oxford/IPS120/IPS120/Typedefs/Read Activity - Enum.ctl"
File 9="user.lib/Oxford/IPS120/IPS120/Typedefs/Read Mode 1 - Enum.ctl"
File 10="user.lib/Oxford/IPS120/IPS120/Typedefs/Read Mode 2 - Enum.ctl"
File 11="user.lib/Oxford/IPS120/IPS120/Typedefs/Read Switch Heater - Enum.ctl"
File 12="user.lib/Oxford/IPS120/IPS120/Typedefs/Read System 1 - Enum.ctl"
File 13="user.lib/Oxford/IPS120/IPS120/Typedefs/Read System 2 - Enum.ctl"
File 14="user.lib/Oxford/IPS120/IPS120/Typedefs/Read X - Cluster.ctl"
File 15="user.lib/Oxford/IPS120/IPS120/Typedefs/Set Activity - Enum.ctl"
File 16="user.lib/Oxford/IPS120/IPS120/Typedefs/Set Control - Enum.ctl"
File 17="user.lib/Oxford/IPS120/IPS120/Typedefs/Set Switch Heater - Enum.ctl"
File 18="user.lib/Oxford/IPS120/IPS120/DSC/IPS120_to_DSC.vi"
File 19="user.lib/Oxford/IPS120/IPS120/DSC/NetVarWrite_dbl.vi"
File 20="user.lib/Oxford/IPS120/IPS120/DSC/NetVarWrite_str.vi"
File 21="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Examine Status.vi"
File 22="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Parse Status.vi"
File 23="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Parse Switch Heater.vi"
File 24="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read Magnet Current.vi"
File 25="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read Magnet Field.vi"
File 26="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read PS Current.vi"
File 27="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read PS Field.vi"
File 28="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read PS Voltage.vi"
File 29="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read Switch Heater Current.vi"
File 30="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read Target Current Sweep Rate.vi"
File 31="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read Target Current.vi"
File 32="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read Target Field Sweep Rate.vi"
File 33="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Read Target Field.vi"
File 34="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Set Activity.vi"
File 35="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Set Control.vi"
File 36="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Set Switch Heater.vi"
File 37="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Set Target Current Sweep Rate.vi"
File 38="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Set Target Current.vi"
File 39="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Set Target Field Sweep Rate.vi"
File 40="user.lib/Oxford/IPS120/IPS120/Drivers/IPS Set Target Field.vi"
File 41="user.lib/Oxford/IPS120/IPS120/Drivers/NI USB GPIB Command.vi"
File 42="user.lib/Oxford/IPS120/Application/Oxford-IPS120-Main.vi"
File 43="user.lib/Oxford/IPS120/API/IPS-120-API.lvlib"
File 44="user.lib/Oxford/IPS120/API/IPS120_GoToField.vi"
File 45="user.lib/Oxford/IPS120/API/Typedefs/Status - Cluster.ctl"
File 46="user.lib/Oxford/IPS120/API/Typedefs/Targets - Cluster.ctl"
File 47="user.lib/Oxford/IPS120/API/subVIs/IPS120_GoToField_SubVI.vi"
File 48="user.lib/Oxford/IPS120/API/subVIs/Set Hold - Check & Resend.vi"
File 49="user.lib/Oxford/IPS120/API/subVIs/Set Target - Check & Resend.vi"
File 50="user.lib/Oxford/IPS120/API/subVIs/Set To Set - Check & Resend.vi"
File 51="user.lib/Oxford/IPS120/API/FGV/FGV_PSP - IPS120 Actions.vi"
File 52="user.lib/Oxford/IPS120/API/FGV/FGV_PSP - IPS120 Activity Status.vi"
File 53="user.lib/Oxford/IPS120/API/FGV/FGV_PSP - IPS120 Mode Status.vi"
File 54="user.lib/Oxford/IPS120/API/FGV/FGV_PSP - IPS120 Remote.vi"
File 55="user.lib/Oxford/IPS120/API/FGV/FGV_PSP - IPS120 Status.vi"
File 56="user.lib/Oxford/IPS120/API/FGV/FGV_PSP - IPS120 Targets.vi"
File 57="user.lib/Oxford/IPS120/API/Access/ReadPowerSupplyField.vi"
File 58="user.lib/Oxford/IPS120/API/Access/ReadTargetField.vi"
File 59="user.lib/Oxford/IPS120/API/Access/ReadTargetFieldRate.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_Oxford_lib_IPS120.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
