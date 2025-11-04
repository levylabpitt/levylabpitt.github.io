[Package]
Name="levylab_lib_ah2500a"
Version="1.4.1.10"
Release=""
ID=e17f57ef6faad645b91a4143a79d28a8
File Format="vip"
Format Version="2017"
Display Name="AH2500A"


[Description]
Description="LabVIEW drivers for Andeen-Hagerling 2500A capacitance bridge"
Summary=""
License=""
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.4.0]\0A- build with pgsql/3.10.2.11"
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
Requires="levylab_lib_instrument_type>=1.1.2.9"
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
Num Files=59
File 0="user.lib/Levylab/AH2500A/Inst.AH2500/Documentation.vi"
File 1="user.lib/Levylab/AH2500A/Inst.AH2500/Inst.AH2500.AppLauncher.vi"
File 2="user.lib/Levylab/AH2500A/Inst.AH2500/Inst.AH2500.lvclass"
File 3="user.lib/Levylab/AH2500A/Inst.AH2500/Process.vi"
File 4="user.lib/Levylab/AH2500A/Inst.AH2500/Typedefs/Inst.AH2500.Commands--Enum.ctl"
File 5="user.lib/Levylab/AH2500A/Inst.AH2500/Typedefs/Inst.AH2500.Configuration--Cluster.ctl"
File 6="user.lib/Levylab/AH2500A/Inst.AH2500/Typedefs/Inst.AH2500.getAll--Cluster.ctl"
File 7="user.lib/Levylab/AH2500A/Inst.AH2500/Typedefs/PrivateEvents--Cluster.ctl"
File 8="user.lib/Levylab/AH2500A/Inst.AH2500/Typedefs/PrivateEvents--Inst.AH2500.MessageToProcess.ctl"
File 9="user.lib/Levylab/AH2500A/Inst.AH2500/Typedefs/PublicEvents--Cluster.ctl"
File 10="user.lib/Levylab/AH2500A/Inst.AH2500/Typedefs/PublicEvents--Inst.AH2500.MessageFromProcess.ctl"
File 11="user.lib/Levylab/AH2500A/Inst.AH2500/Private/Inst.AH2500.getAll.vi"
File 12="user.lib/Levylab/AH2500A/Inst.AH2500/Private/Inst.AH2500.GetPrivateEvents.vi"
File 13="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Close Hardware.vi"
File 14="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Configuration Window.vi"
File 15="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/CreatePrivateEvents.vi"
File 16="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/CreatePublicEvents.vi"
File 17="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/DestroyPrivateEvents.vi"
File 18="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/DestroyPublicEvents.vi"
File 19="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Get SMO Address.vi"
File 20="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Get SMO Database Paths.vi"
File 21="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Get SMO Name.vi"
File 22="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Get SMO Port.vi"
File 23="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Get SMO Public API.vi"
File 24="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Get SMO Serial Number.vi"
File 25="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Get SMO Vendor.vi"
File 26="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Handle Command.vi"
File 27="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Handle getAll.vi"
File 28="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Handle setAllData.vi"
File 29="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Handle setConfiguration.vi"
File 30="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Open Hardware.vi"
File 31="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Read Configuration File.vi"
File 32="user.lib/Levylab/AH2500A/Inst.AH2500/Overrides/Write Configuration File.vi"
File 33="user.lib/Levylab/AH2500A/Inst.AH2500/API/Close.vi"
File 34="user.lib/Levylab/AH2500A/Inst.AH2500/API/getCapacitance.vi"
File 35="user.lib/Levylab/AH2500A/Inst.AH2500/API/getExcitation.vi"
File 36="user.lib/Levylab/AH2500A/Inst.AH2500/API/getLoss.vi"
File 37="user.lib/Levylab/AH2500A/Inst.AH2500/API/Inst.AH2500.GetPublicEvents.vi"
File 38="user.lib/Levylab/AH2500A/Inst.AH2500/API/Inst.AH2500.MessageToProcess.vi"
File 39="user.lib/Levylab/AH2500A/Inst.AH2500/API/Open.vi"
File 40="user.lib/Levylab/AH2500A/Inst UI.AH2500/Inst UI.AH2500.lvclass"
File 41="user.lib/Levylab/AH2500A/Inst UI.AH2500/Inst UI.AH2500.TestLauncher.vi"
File 42="user.lib/Levylab/AH2500A/Inst UI.AH2500/Inst UI.AH2500.UI--Cluster.ctl"
File 43="user.lib/Levylab/AH2500A/Inst UI.AH2500/Process.vi"
File 44="user.lib/Levylab/AH2500A/AH2500/AH2500.lvlib"
File 45="user.lib/Levylab/AH2500A/AH2500/AVERAGE.vi"
File 46="user.lib/Levylab/AH2500A/AH2500/BIAS.vi"
File 47="user.lib/Levylab/AH2500A/AH2500/Close.vi"
File 48="user.lib/Levylab/AH2500A/AH2500/Open.vi"
File 49="user.lib/Levylab/AH2500A/AH2500/RST.vi"
File 50="user.lib/Levylab/AH2500A/AH2500/SHOW SPECIAL.vi"
File 51="user.lib/Levylab/AH2500A/AH2500/SHOW STATUS.vi"
File 52="user.lib/Levylab/AH2500A/AH2500/SINGLE.vi"
File 53="user.lib/Levylab/AH2500A/AH2500/UNITS.vi"
File 54="user.lib/Levylab/AH2500A/AH2500/VOLTAGE.vi"
File 55="user.lib/Levylab/AH2500A/AH2500/Private/Parse SHOW SPECIAL.vi"
File 56="user.lib/Levylab/AH2500A/AH2500/Private/Parse SHOW STATUS.vi"
File 57="user.lib/Levylab/AH2500A/AH2500/Private/Parse SINGLE.vi"
File 58="user.lib/Levylab/AH2500A/AH2500/Private/RW.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_ah2500a_1.mnu"
File 1="functions_Levylab_lib_AH2500A.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
