[Package]
Name="levylab_lib_krohn_hite_7008"
Version="1.7.9.1"
Release=""
ID=91cf27814cebd47dadaadea7bd45499f
File Format="vip"
Format Version="2017"
Display Name="Krohn-Hite 7008 Drivers"


[Description]
Description="Drivers and UI for Krohn-Hite 7008 multichannel amplifiers."
Summary=""
License=""
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Issue #2: Display KH address when running as a remote panel\0A- Update 500/10M detection algoithm to minimise unecessary changes to an already configured instrument."
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires="levylab_lib_levylab_instruments>=1.13.0.9"
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
Num Files=35
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
File 15="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 COM Error Checker.vi"
File 16="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 COM.vi"
File 17="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Create Command String.vi"
File 18="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Enum Shunt to Gain.vi"
File 19="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Enum to Gain.vi"
File 20="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Get All Channel Gains.vi"
File 21="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Get All Channels.vi"
File 22="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Get Channel.vi"
File 23="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Parse Response String.vi"
File 24="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Set All Channels.vi"
File 25="user.lib/LevyLab/Krohn Hite 7008/Private/KH7008 Set Channel.vi"
File 26="user.lib/LevyLab/Krohn Hite 7008/Overrides/Read Configuration File.vi"
File 27="user.lib/LevyLab/Krohn Hite 7008/Overrides/Write Configuration File.vi"
File 28="user.lib/LevyLab/Krohn Hite 7008/API/Close.vi"
File 29="user.lib/LevyLab/Krohn Hite 7008/API/Open.vi"
File 30="user.lib/LevyLab/Krohn Hite 7008/API/Read Channel Setting.vi"
File 31="user.lib/LevyLab/Krohn Hite 7008/API/Read Gain.vi"
File 32="user.lib/LevyLab/Krohn Hite 7008/API/Shunt - 500 or 10M Control Disable.vi"
File 33="user.lib/LevyLab/Krohn Hite 7008/API/Shunt - Check 500 or 10M.vi"
File 34="user.lib/LevyLab/Krohn Hite 7008/API/Write Channel Setting.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=5
File 0="_functions_levylab_lib_krohn_hite_7008_1.mnu"
File 1="_functions_levylab_lib_krohn_hite_7008_2.mnu"
File 2="_functions_levylab_lib_krohn_hite_7008_3.mnu"
File 3="_functions_levylab_lib_krohn_hite_7008_4.mnu"
File 4="functions_LevyLab_lib_Krohn_Hite_7008.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
