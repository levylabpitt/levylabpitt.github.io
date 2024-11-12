[Package]
Name="levylab_lib_krohn_hite_7008"
Version="2.0.0.6"
Release=""
ID=b35b5336ea0a23a9e4a100d339ceb7fe
File Format="vip"
Format Version="2017"
Display Name="Krohn-Hite-7008"


[Description]
Description="Drivers and UI for Krohn-Hite 7008 multichannel amplifiers."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2024, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="first release with Krohn-Hite UI inheriting from Instrument Framework"
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
Requires="ftdi_lib_d2xx>=1.1.0.4,jdp_science_jsontext>=1.8.2.122,jdp_science_lib_common_utilities>=1.4.1.18,jdp_science_postgresql>=0.6.0.43,jki_lib_caraya>=1.4.3.147,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.3.113,labview_open_source_lib_epoch_datetime>=1.2.0.6,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.10.3,levylab_lib_krohn_hite_7008>=1.7.9.1,levylab_lib_lvtoitx>=3.8.2.4,levylab_lib_xy_utilities>=1.5.4.1,lvh_toolbox>=2.0.0.35,mgi_lib_1d_array>=1.0.2.3,mgi_lib_numeric>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_boolean>=4.0.0.7,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_levylab_instruments>=1.13.0.10"
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
Num Files=86
File 0="user.lib/LevyLab/Krohn Hite 7008/Krohn-Hite-7008.lvproj"
File 1="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/KH7008.lvlib"
File 2="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/allChannelProperties--Array.ctl"
File 3="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/channel--enum.ctl"
File 4="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/channelProperties--Cluster.ctl"
File 5="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/couple--Enum.ctl"
File 6="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/Filter--Enum.ctl"
File 7="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/gain--enum.ctl"
File 8="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/Input--Enum.ctl"
File 9="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/typedefs/shunt--enum.ctl"
File 10="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/tests/test string.vi"
File 11="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/private/COM Error Checker.vi"
File 12="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/private/COM.vi"
File 13="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/private/Create Command String.vi"
File 14="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/private/Enum Shunt to Gain.vi"
File 15="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/private/Enum to Gain.vi"
File 16="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/private/Get Installed SR Type.vi"
File 17="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/private/Parse Response String.vi"
File 18="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/API/Close.vi"
File 19="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/API/Get All Channel Gains.vi"
File 20="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/API/Get All Channels.vi"
File 21="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/API/Get Channel.vi"
File 22="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/API/Open.vi"
File 23="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/API/Set All Channels.vi"
File 24="user.lib/LevyLab/Krohn Hite 7008/SMOs/KH7008/API/Set Channel.vi"
File 25="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Documentation.vi"
File 26="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Inst.Krohn-Hite-7008.AppLauncher.vi"
File 27="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Inst.Krohn-Hite-7008.lvclass"
File 28="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Process.vi"
File 29="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/test_json.vi"
File 30="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/getAllChannelsDatabase--Cluster.ctl"
File 31="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/getAllChannelsResponse--Cluster.ctl"
File 32="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/getChannelRequest--Cluster.ctl"
File 33="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/Inst.Krohn-Hite-7008.device--Cluster.ctl"
File 34="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/Inst.Krohn-Hite-7008.getAll--Cluster.ctl"
File 35="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/Inst.Krohn-Hite-7008.ProtectedCommands--Enum.ctl"
File 36="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/Inst.Krohn-Hite-7008.PublicCommands--Enum.ctl"
File 37="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/Inst.Krohn-Hite-7008.setAll--Array.ctl"
File 38="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/Inst.Krohn-Hite-7008.setChannel-Cluster.ctl"
File 39="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/MeasurePresets-Enum.ctl"
File 40="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/PrivateEvents--Cluster.ctl"
File 41="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/PrivateEvents--Inst.Krohn-Hite-7008.MessageToProcess.ctl"
File 42="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/PublicEvents--Cluster.ctl"
File 43="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/PublicEvents--Inst.Krohn-Hite-7008.MessageFromProcess.ctl"
File 44="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/setAllChannelsRequest--Cluster.ctl"
File 45="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Typedefs/setChannelRequest--Cluster.ctl"
File 46="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/Convert_allChannelProperties_to_JSON.vi"
File 47="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/Convert_JSON_to_allChannelProperties.vi"
File 48="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/Inst.Krohn-Hite-7008.GetPrivateEvents.vi"
File 49="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/Inst.Krohn-Hite-7008.handleGetCommand.vi"
File 50="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/Inst.Krohn-Hite-7008.handleSetCommand.vi"
File 51="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/Inst.Krohn-Hite-7008.MessageFromProcess.vi"
File 52="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/Inst.Krohn-Hite-7008.ReplaceChannelProperty.vi"
File 53="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Private/sandbox.vi"
File 54="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Close Hardware.vi"
File 55="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Configuration Window.vi"
File 56="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/CreatePrivateEvents.vi"
File 57="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/CreatePublicEvents.vi"
File 58="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/DestroyPrivateEvents.vi"
File 59="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/DestroyPublicEvents.vi"
File 60="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Get SMO Address.vi"
File 61="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Get SMO Name.vi"
File 62="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Get SMO PGSQL Log Paths.vi"
File 63="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Get SMO Port.vi"
File 64="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Get SMO Public API.vi"
File 65="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Get SMO RC Type.vi"
File 66="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Handle Command.vi"
File 67="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Handle Error.vi"
File 68="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Handle getAll.vi"
File 69="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Open Hardware.vi"
File 70="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Read Configuration File.vi"
File 71="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/Overrides/Write Configuration File.vi"
File 72="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/Close.vi"
File 73="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/getAllChannels.vi"
File 74="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/getChannel.vi"
File 75="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/Inst.Krohn-Hite-7008.GetPublicEvents.vi"
File 76="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/Inst.Krohn-Hite-7008.MessageToProcess.vi"
File 77="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/Open.vi"
File 78="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/setAllChannels.vi"
File 79="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst.Krohn-Hite-7008/API/setChannel.vi"
File 80="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst UI.Krohn-Hite-7008/Inst UI.Krohn-Hite-7008.lvclass"
File 81="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst UI.Krohn-Hite-7008/Inst UI.Krohn-Hite-7008.TestLauncher.vi"
File 82="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst UI.Krohn-Hite-7008/Inst UI.Krohn-Hite-7008.UI--Cluster.ctl"
File 83="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst UI.Krohn-Hite-7008/KH7008.png"
File 84="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst UI.Krohn-Hite-7008/Process.vi"
File 85="user.lib/LevyLab/Krohn Hite 7008/SMOs/Inst UI.Krohn-Hite-7008/SR Disable.vi"


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
