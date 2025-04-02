[Package]
Name="levylab_lib_razorbill_rp100"
Version="1.4.0.1"
Release=""
ID=5af63c654474b9396c515b9c92587cb4
File Format="vip"
Format Version="2017"
Display Name="Razorbill RP100"


[Description]
Description="Divers for Razorbill RP100 HV amplifier"
Summary=""
License=""
Copyright="Copyright (c) 2023, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Update to Instrument Framework v1.13.0.9\0A- Now a proper Instrument:\0A  - separate UI and back end processes\0A  - hardware abstraction in the Inst.RP100:process.vi\0A"
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
Num Files=68
File 0="user.lib/Levylab/Razorbill RP100/razorbill.lvproj"
File 1="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Documentation.vi"
File 2="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Inst.RP100.AppLauncher.vi"
File 3="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Inst.RP100.lvclass"
File 4="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Process.vi"
File 5="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/Commands--Enum.ctl"
File 6="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/getLevel--Cluster.ctl"
File 7="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/Inst.RP100.Commands--Enum.ctl"
File 8="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/Inst.RP100.Configuration--Cluster.ctl"
File 9="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/Inst.RP100.getAll--Cluster.ctl"
File 10="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/Output Channel--Enum.ctl"
File 11="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/Output State--Enum.ctl"
File 12="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/PrivateEvents--Cluster.ctl"
File 13="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/PrivateEvents--Inst.RP100.MessageToProcess.ctl"
File 14="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/PublicEvents--Cluster.ctl"
File 15="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/PublicEvents--Inst.RP100.MessageFromProcess.ctl"
File 16="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/setLevel--Cluster.ctl"
File 17="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/setOutput--Cluster.ctl"
File 18="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Typedefs/SetStrain--Cluster.ctl"
File 19="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Private/Inst.RP100.getAll.vi"
File 20="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Private/Inst.RP100.GetPrivateEvents.vi"
File 21="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Private/Inst.RP100.Remote Client.vim"
File 22="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Private/Inst.RP100.setLevel.vi"
File 23="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Private/Inst.RP100.setState.vi"
File 24="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Private/Inst.RP100.setStrain.vi"
File 25="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Close Hardware.vi"
File 26="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Configuration Window.vi"
File 27="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/CreatePrivateEvents.vi"
File 28="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/CreatePublicEvents.vi"
File 29="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/DestroyPrivateEvents.vi"
File 30="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/DestroyPublicEvents.vi"
File 31="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Get SMO Address.vi"
File 32="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Get SMO Name.vi"
File 33="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Get SMO PGSQL Log Paths.vi"
File 34="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Get SMO Port.vi"
File 35="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Get SMO Public API.vi"
File 36="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Get SMO RC Type.vi"
File 37="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Handle Command.vi"
File 38="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Handle getAll.vi"
File 39="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Handle setConfiguration.vi"
File 40="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Open Hardware.vi"
File 41="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Read Configuration File.vi"
File 42="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Overrides/Write Configuration File.vi"
File 43="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.CLS.vi"
File 44="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Get Level.vi"
File 45="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Get Output State.vi"
File 46="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Get Slew.vi"
File 47="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.IDN.vi"
File 48="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Measure Current.vi"
File 49="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Measure Voltage.vi"
File 50="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.RST.vi"
File 51="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Set Level.vi"
File 52="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Set Output State.vi"
File 53="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/RP100.Set Slew.vi"
File 54="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/Drivers/subVIs/RP100.VISA RW.vi"
File 55="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Close.vi"
File 56="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Get Level.vi"
File 57="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Get Strain.vi"
File 58="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Inst.RP100.GetPublicEvents.vi"
File 59="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Inst.RP100.MessageToProcess.vi"
File 60="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Open.vi"
File 61="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Set Level.vi"
File 62="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Set State.vi"
File 63="user.lib/Levylab/Razorbill RP100/SMOs/Inst.RP100/API/Set Strain.vi"
File 64="user.lib/Levylab/Razorbill RP100/SMOs/Inst UI.RP100/Inst UI.RP100.lvclass"
File 65="user.lib/Levylab/Razorbill RP100/SMOs/Inst UI.RP100/Inst UI.RP100.TestLauncher.vi"
File 66="user.lib/Levylab/Razorbill RP100/SMOs/Inst UI.RP100/Inst UI.RP100.UI--Cluster.ctl"
File 67="user.lib/Levylab/Razorbill RP100/SMOs/Inst UI.RP100/Process.vi"


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
