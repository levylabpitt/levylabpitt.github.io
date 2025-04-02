[Package]
Name="levylab_lib_razorbill_rp100"
Version="2.0.0.5"
Release=""
ID=3b8c7d8b11bf686f938d7bc6f13825ba
File Format="vip"
Format Version="2017"
Display Name="Razorbill RP100"


[Description]
Description="Drivers for Razorbill RP100 HV amplifier"
Summary=""
License=""
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Issue #14: Update to Instrument Framework v2"
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
Requires="levylab_lib_levylab_instruments>=2.0.0.26"
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
Num Files=82
File 0="user.lib/Levylab/Razorbill RP100/Inst.RP100.lvlib"
File 1="user.lib/Levylab/Razorbill RP100/RP100/Close.vi"
File 2="user.lib/Levylab/Razorbill RP100/RP100/CLS.vi"
File 3="user.lib/Levylab/Razorbill RP100/RP100/Get Level.vi"
File 4="user.lib/Levylab/Razorbill RP100/RP100/Get Output State.vi"
File 5="user.lib/Levylab/Razorbill RP100/RP100/Get Slew.vi"
File 6="user.lib/Levylab/Razorbill RP100/RP100/IDN.vi"
File 7="user.lib/Levylab/Razorbill RP100/RP100/Measure Current.vi"
File 8="user.lib/Levylab/Razorbill RP100/RP100/Measure Voltage.vi"
File 9="user.lib/Levylab/Razorbill RP100/RP100/Open.vi"
File 10="user.lib/Levylab/Razorbill RP100/RP100/RP100.lvlib"
File 11="user.lib/Levylab/Razorbill RP100/RP100/RST.vi"
File 12="user.lib/Levylab/Razorbill RP100/RP100/Set Level.vi"
File 13="user.lib/Levylab/Razorbill RP100/RP100/Set Output State.vi"
File 14="user.lib/Levylab/Razorbill RP100/RP100/Set Slew.vi"
File 15="user.lib/Levylab/Razorbill RP100/RP100/subVIs/Parse IDN.vi"
File 16="user.lib/Levylab/Razorbill RP100/RP100/subVIs/VISA RW.vi"
File 17="user.lib/Levylab/Razorbill RP100/Inst.RP100/Documentation.vi"
File 18="user.lib/Levylab/Razorbill RP100/Inst.RP100/Inst.RP100.AppLauncher.vi"
File 19="user.lib/Levylab/Razorbill RP100/Inst.RP100/Inst.RP100.lvclass"
File 20="user.lib/Levylab/Razorbill RP100/Inst.RP100/Process.vi"
File 21="user.lib/Levylab/Razorbill RP100/Inst.RP100/TestAPI.vi"
File 22="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/Channel--Num.ctl"
File 23="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/getLevel--Cluster.ctl"
File 24="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/Inst.RP100.Commands--Enum.ctl"
File 25="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/Inst.RP100.Configuration--Cluster.ctl"
File 26="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/Inst.RP100.getAll--Cluster.ctl"
File 27="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/PrivateEvents--Cluster.ctl"
File 28="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/PrivateEvents--Inst.RP100.MessageToProcess.ctl"
File 29="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/PublicEvents--Cluster.ctl"
File 30="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/PublicEvents--Inst.RP100.MessageFromProcess.ctl"
File 31="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/setLevel--Cluster.ctl"
File 32="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/setState--Cluster.ctl"
File 33="user.lib/Levylab/Razorbill RP100/Inst.RP100/Typedefs/State--Enum.ctl"
File 34="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/convert V to d.vi"
File 35="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/Inst.RP100.getAll.vi"
File 36="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/Inst.RP100.GetPrivateEvents.vi"
File 37="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/Inst.RP100.Public API.vi"
File 38="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/Inst.RP100.Remote Client.vim"
File 39="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/Inst.RP100.setLevel.vi"
File 40="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/Inst.RP100.setState.vi"
File 41="user.lib/Levylab/Razorbill RP100/Inst.RP100/Private/Inst.RP100.setStrain.vi"
File 42="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Close Hardware.vi"
File 43="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Configuration Window.vi"
File 44="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/CreatePrivateEvents.vi"
File 45="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/CreatePublicEvents.vi"
File 46="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/DestroyPrivateEvents.vi"
File 47="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/DestroyPublicEvents.vi"
File 48="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO Address.vi"
File 49="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO HELP getAll.vi"
File 50="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO HELP.vi"
File 51="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO Name.vi"
File 52="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO PGSQL Log Paths.vi"
File 53="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO Port.vi"
File 54="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO Public API.vi"
File 55="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO Serial Number.vi"
File 56="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Get SMO Vendor.vi"
File 57="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Handle Command.vi"
File 58="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Handle getAll.vi"
File 59="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Handle setAllData.vi"
File 60="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Handle setConfiguration.vi"
File 61="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Open Hardware.vi"
File 62="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Read Configuration File.vi"
File 63="user.lib/Levylab/Razorbill RP100/Inst.RP100/Overrides/Write Configuration File.vi"
File 64="user.lib/Levylab/Razorbill RP100/Inst.RP100/Deprecated/Get Level.vi"
File 65="user.lib/Levylab/Razorbill RP100/Inst.RP100/Deprecated/Get Strain.vi"
File 66="user.lib/Levylab/Razorbill RP100/Inst.RP100/Deprecated/Set Level.vi"
File 67="user.lib/Levylab/Razorbill RP100/Inst.RP100/Deprecated/Set State.vi"
File 68="user.lib/Levylab/Razorbill RP100/Inst.RP100/Deprecated/Set Strain.vi"
File 69="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/Close.vi"
File 70="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/getLevel.vi"
File 71="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/getStrain.vi"
File 72="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/Inst.RP100.GetPublicEvents.vi"
File 73="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/Inst.RP100.MessageToProcess.vi"
File 74="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/Open.vi"
File 75="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/setLevel.vi"
File 76="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/setState.vi"
File 77="user.lib/Levylab/Razorbill RP100/Inst.RP100/API/setStrain.vi"
File 78="user.lib/Levylab/Razorbill RP100/Inst UI.RP100/Inst UI.RP100.lvclass"
File 79="user.lib/Levylab/Razorbill RP100/Inst UI.RP100/Inst UI.RP100.TestLauncher.vi"
File 80="user.lib/Levylab/Razorbill RP100/Inst UI.RP100/Inst UI.RP100.UI--Cluster.ctl"
File 81="user.lib/Levylab/Razorbill RP100/Inst UI.RP100/Process.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Razorbill_RP100.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
