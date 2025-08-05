[Package]
Name="levylab_lib_transport_server"
Version="0.0.0.1"
Release=""
ID=6cf0856dbfa8e97347bc4f98eac1ae19
File Format="vip"
Format Version="2017"
Display Name="Transport Server"


[Description]
Description="Server used for scripting and performing asynchronous transport measurments."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="0.0.0\0A- Initial release"
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
Requires="levylab_lib_control_experiment>=1.3.4.20,levylab_lib_transport>=1.10.0.19"
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
File 0="user.lib/Levylab/Transport/Transport/Inst.Transport/Documentation.vi"
File 1="user.lib/Levylab/Transport/Transport/Inst.Transport/Inst.Transport.AppLauncher.vi"
File 2="user.lib/Levylab/Transport/Transport/Inst.Transport/Inst.Transport.lvclass"
File 3="user.lib/Levylab/Transport/Transport/Inst.Transport/Process.vi"
File 4="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/Inst.Transport.Configuration--Cluster.ctl"
File 5="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/Inst.Transport.getAll--Cluster.ctl"
File 6="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/Inst.Transport.Methods--Enum.ctl"
File 7="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/Inst.Transport.ProtectedCommands--Enum.ctl"
File 8="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/Inst.Transport.PublicCommands--Enum.ctl"
File 9="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/LockinSweep.png"
File 10="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/LockinTime.png"
File 11="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/LockinTimeDelay.png"
File 12="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/PrivateEvents--Cluster.ctl"
File 13="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/PrivateEvents--MessageToProcess.ctl"
File 14="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/setExptComments--Request--Cluster.ctl"
File 15="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/setExptFolder--Request--Cluster.ctl"
File 16="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/setExptParam--Request--Cluster.ctl"
File 17="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/setSweepConfig--Request--Cluster.ctl"
File 18="user.lib/Levylab/Transport/Transport/Inst.Transport/Typedefs/startTransport--Request--Cluster.ctl"
File 19="user.lib/Levylab/Transport/Transport/Inst.Transport/Tests/Test Notifiers.vi"
File 20="user.lib/Levylab/Transport/Transport/Inst.Transport/Protected/Inst.Transport.Public API.vi"
File 21="user.lib/Levylab/Transport/Transport/Inst.Transport/Private/Inst.Transport.GetPrivateEvents.vi"
File 22="user.lib/Levylab/Transport/Transport/Inst.Transport/Private/Inst.Transport.sendMessageToProcess.vi"
File 23="user.lib/Levylab/Transport/Transport/Inst.Transport/Private/Variant to Display String.vi"
File 24="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/CreatePrivateEvents.vi"
File 25="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/DestroyPrivateEvents.vi"
File 26="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/onStart.vi"
File 27="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/onStop.vi"
File 28="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO Database Paths.vi"
File 29="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO HELP getAll.vi"
File 30="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO HELP.vi"
File 31="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO Name.vi"
File 32="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO Port.vi"
File 33="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO Public API.vi"
File 34="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO Serial Number.vi"
File 35="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/SMO/Get SMO Vendor.vi"
File 36="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Configuration/Configuration Window.vi"
File 37="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Configuration/Read Configuration File.vi"
File 38="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Configuration/Write Configuration File.vi"
File 39="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Commands/Handle Command.vi"
File 40="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Commands/Handle GET.vi"
File 41="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Commands/Handle getAll.vi"
File 42="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Commands/Handle SET.vi"
File 43="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Commands/Handle setAllData.vi"
File 44="user.lib/Levylab/Transport/Transport/Inst.Transport/Overrides/Commands/Handle setConfiguration.vi"
File 45="user.lib/Levylab/Transport/Transport/Inst.Transport/API/appendExptParam.vi"
File 46="user.lib/Levylab/Transport/Transport/Inst.Transport/API/clearExptParam.vi"
File 47="user.lib/Levylab/Transport/Transport/Inst.Transport/API/Close.vi"
File 48="user.lib/Levylab/Transport/Transport/Inst.Transport/API/Open.vi"
File 49="user.lib/Levylab/Transport/Transport/Inst.Transport/API/setExptComments.vi"
File 50="user.lib/Levylab/Transport/Transport/Inst.Transport/API/setExptFolder.vi"
File 51="user.lib/Levylab/Transport/Transport/Inst.Transport/API/setExptParam.vi"
File 52="user.lib/Levylab/Transport/Transport/Inst.Transport/API/setSweepConfig.vi"
File 53="user.lib/Levylab/Transport/Transport/Inst.Transport/API/startTransport.vi"
File 54="user.lib/Levylab/Transport/Transport/Inst.Transport/API/stopTransport.vi"
File 55="user.lib/Levylab/Transport/Transport/Inst UI.Transport/Inst UI.Transport.lvclass"
File 56="user.lib/Levylab/Transport/Transport/Inst UI.Transport/Instrument UI.Transport.TestLauncher.vi"
File 57="user.lib/Levylab/Transport/Transport/Inst UI.Transport/Instrument UI.Transport.UI--Cluster.ctl"
File 58="user.lib/Levylab/Transport/Transport/Inst UI.Transport/Process.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Transport_Server.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
