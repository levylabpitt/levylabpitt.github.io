[Package]
Name="levylab_lib_krohn_hite_7008"
Version="2.4.1.23"
Release=""
ID=d607f5d5676dd0656439d84aeb5c4eb2
File Format="vip"
Format Version="2017"
Display Name="Krohn-Hite-7008"


[Description]
Description="Drivers and UI for Krohn-Hite 7008 multichannel amplifiers."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.4.1]\0AIssue #5: Fix simulation mode"
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
Requires="levylab_lib_d2xx_lv>=1.3.0.8,levylab_lib_instrument_type>=1.1.3.10"
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
Num Files=98
File 0="user.lib/LevyLab/Krohn Hite 7008/Inst.KH7008.lvlib"
File 1="user.lib/LevyLab/Krohn Hite 7008/KH7008/KH7008.lvlib"
File 2="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/allChannelProperties--Array.ctl"
File 3="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/channel--numeric.ctl"
File 4="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/channelProperties--Cluster.ctl"
File 5="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/couple--Enum.ctl"
File 6="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/Filter--Enum.ctl"
File 7="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/gain--enum.ctl"
File 8="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/Input--Enum.ctl"
File 9="user.lib/LevyLab/Krohn Hite 7008/KH7008/typedefs/shunt--enum.ctl"
File 10="user.lib/LevyLab/Krohn Hite 7008/KH7008/private/COM Error Checker.vi"
File 11="user.lib/LevyLab/Krohn Hite 7008/KH7008/private/COM.vi"
File 12="user.lib/LevyLab/Krohn Hite 7008/KH7008/private/Create Command String.vi"
File 13="user.lib/LevyLab/Krohn Hite 7008/KH7008/private/Enum Shunt to Gain.vi"
File 14="user.lib/LevyLab/Krohn Hite 7008/KH7008/private/Enum to Gain.vi"
File 15="user.lib/LevyLab/Krohn Hite 7008/KH7008/private/Get Installed SR Type.vi"
File 16="user.lib/LevyLab/Krohn Hite 7008/KH7008/private/Parse Response String.vi"
File 17="user.lib/LevyLab/Krohn Hite 7008/KH7008/API/Close.vi"
File 18="user.lib/LevyLab/Krohn Hite 7008/KH7008/API/Get All Channel Gains.vi"
File 19="user.lib/LevyLab/Krohn Hite 7008/KH7008/API/Get All Channels.vi"
File 20="user.lib/LevyLab/Krohn Hite 7008/KH7008/API/Get Channel.vi"
File 21="user.lib/LevyLab/Krohn Hite 7008/KH7008/API/Open.vi"
File 22="user.lib/LevyLab/Krohn Hite 7008/KH7008/API/Set All Channels.vi"
File 23="user.lib/LevyLab/Krohn Hite 7008/KH7008/API/Set Channel.vi"
File 24="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Documentation.vi"
File 25="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Inst.KH7008.AppLauncher.vi"
File 26="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Inst.Krohn-Hite-7008.lvclass"
File 27="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Process.vi"
File 28="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/getAllChannelsDatabase--Cluster.ctl"
File 29="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/getAllChannelsResponse--Cluster.ctl"
File 30="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/getChannelRequest--Cluster.ctl"
File 31="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/getChassisResponse--Cluster.ctl"
File 32="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/getShuntResistorResponse--Cluster.ctl"
File 33="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/Inst.KH7008.Commands--Enum.ctl"
File 34="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/Inst.KH7008.device--Cluster.ctl"
File 35="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/Inst.KH7008.getAll--Cluster.ctl"
File 36="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/Inst.KH7008.ProtectedCommands--Enum.ctl"
File 37="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/PrivateEvents--Cluster.ctl"
File 38="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/PrivateEvents--Inst.KH7008.MessageToProcess.ctl"
File 39="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/PublicEvents--Cluster.ctl"
File 40="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/PublicEvents--Inst.KH7008.MessageFromProcess.ctl"
File 41="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/setAllChannelsRequest--Cluster.ctl"
File 42="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Typedefs/setChannelRequest--Cluster.ctl"
File 43="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Convert_allChannelProperties_to_JSON.vi"
File 44="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Convert_ChannelProperty_to_JSON.vi"
File 45="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Convert_JSON_to_allChannelProperties.vi"
File 46="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Device Error Dialog.vi"
File 47="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Inst.KH7008.CreateSMOs.vi"
File 48="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Inst.KH7008.GetPrivateEvents.vi"
File 49="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Inst.KH7008.handleGetCommand.vi"
File 50="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Inst.KH7008.handleSetCommand.vi"
File 51="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Inst.KH7008.InitSimChannels.vi"
File 52="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Inst.KH7008.MessageFromProcess.vi"
File 53="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/Inst.KH7008.ReplaceChannelProperty.vi"
File 54="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/sandbox.vi"
File 55="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Private/VISA Dialog.vi"
File 56="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Close Hardware.vi"
File 57="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Configuration Window.vi"
File 58="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/CreatePrivateEvents.vi"
File 59="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/CreatePublicEvents.vi"
File 60="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/DestroyPrivateEvents.vi"
File 61="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/DestroyPublicEvents.vi"
File 62="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO Address.vi"
File 63="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO Database Paths.vi"
File 64="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO HELP getAll.vi"
File 65="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO HELP.vi"
File 66="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO Name.vi"
File 67="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO Port.vi"
File 68="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO Public API.vi"
File 69="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO Serial Number.vi"
File 70="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Get SMO Vendor.vi"
File 71="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Handle Command.vi"
File 72="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Handle getAll.vi"
File 73="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Handle setAllData.vi"
File 74="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Open Hardware.vi"
File 75="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Read Configuration File.vi"
File 76="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/Overrides/Write Configuration File.vi"
File 77="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Close.vi"
File 78="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/getAllChannels.vi"
File 79="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/getChannel.vi"
File 80="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.getAllChannels.vi"
File 81="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.getChannel.vi"
File 82="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.getChassis.vi"
File 83="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.GetPublicEvents.vi"
File 84="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.getShuntResistor.vi"
File 85="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.MessageToProcess.vi"
File 86="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.Open.vi"
File 87="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.Read Index.vi"
File 88="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.setAllChannels.vi"
File 89="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Inst.KH7008.setChannel.vi"
File 90="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/Open.vi"
File 91="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/setAllChannels.vi"
File 92="user.lib/LevyLab/Krohn Hite 7008/Inst.Krohn-Hite-7008/API/setChannel.vi"
File 93="user.lib/LevyLab/Krohn Hite 7008/Inst UI.Krohn-Hite-7008/Inst UI.KH7008.TestLauncher.vi"
File 94="user.lib/LevyLab/Krohn Hite 7008/Inst UI.Krohn-Hite-7008/Inst UI.KH7008.UI--Cluster.ctl"
File 95="user.lib/LevyLab/Krohn Hite 7008/Inst UI.Krohn-Hite-7008/Inst UI.Krohn-Hite-7008.lvclass"
File 96="user.lib/LevyLab/Krohn Hite 7008/Inst UI.Krohn-Hite-7008/Process.vi"
File 97="user.lib/LevyLab/Krohn Hite 7008/Inst UI.Krohn-Hite-7008/SR Disable.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_krohn_hite_7008_1.mnu"
File 1="functions_LevyLab_lib_Krohn_Hite_7008.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
