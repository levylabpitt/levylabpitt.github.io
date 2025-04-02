[Package]
Name="levylab_lib_leiden_fp"
Version="4.57.2.2"
Release=""
ID=bec837c8815349c47db126e422027e46
File Format="vip"
Format Version="2017"
Display Name="LEIDEN FP"


[Description]
Description="Tools used by LevyLab to interact with Leiden Front Panel (FP)\0D\0AAPI:\0APush Button (Start, 3He, 4He, Normal, Recovery, Auto, Reset, LED Test)\0ASet Mode (Auto Off, Start, Condense 3He, Condense 4He, Normal Circulation, Recovery)\0AGet Mode"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="First build"
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
Requires="levylab_lib_levylab_instruments>=1.13.0.10"
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
Num Files=49
File 0="user.lib/LevyLab/Leiden FP/Documentation.vi"
File 1="user.lib/LevyLab/Leiden FP/GHSButtons.vi"
File 2="user.lib/LevyLab/Leiden FP/Inst.FP.lvclass"
File 3="user.lib/LevyLab/Leiden FP/Inst.FP.TestLauncher.vi"
File 4="user.lib/LevyLab/Leiden FP/Process.vi"
File 5="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Buttons--Enum.ctl"
File 6="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Commands--Enum.ctl"
File 7="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Configuration--Cluster.ctl"
File 8="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.DefaultPGSQLPaths--Cluster.ctl"
File 9="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Get Mode--Cluster.ctl"
File 10="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.getAll--Cluster.ctl"
File 11="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Modes(set)--Enum.ctl"
File 12="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Modes--Enum.ctl"
File 13="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Push Button--Cluster.ctl"
File 14="user.lib/LevyLab/Leiden FP/Typedefs/Inst.FP.Type--Enum.ctl"
File 15="user.lib/LevyLab/Leiden FP/Typedefs/PrivateEvents--Cluster.ctl"
File 16="user.lib/LevyLab/Leiden FP/Typedefs/PrivateEvents--Inst.FP.MessageToProcess.ctl"
File 17="user.lib/LevyLab/Leiden FP/Typedefs/PublicEvents--Cluster.ctl"
File 18="user.lib/LevyLab/Leiden FP/Typedefs/PublicEvents--Inst.FP.MessageFromProcess.ctl"
File 19="user.lib/LevyLab/Leiden FP/Private/Inst.FP.GetPrivateEvents.vi"
File 20="user.lib/LevyLab/Leiden FP/Private/Inst.FP.GHSmodeStringToEnum.vi"
File 21="user.lib/LevyLab/Leiden FP/Private/Inst.FP.ParseGHSmode.vi"
File 22="user.lib/LevyLab/Leiden FP/Overrides/Configuration Window.vi"
File 23="user.lib/LevyLab/Leiden FP/Overrides/CreatePrivateEvents.vi"
File 24="user.lib/LevyLab/Leiden FP/Overrides/CreatePublicEvents.vi"
File 25="user.lib/LevyLab/Leiden FP/Overrides/DestroyPrivateEvents.vi"
File 26="user.lib/LevyLab/Leiden FP/Overrides/DestroyPublicEvents.vi"
File 27="user.lib/LevyLab/Leiden FP/Overrides/Get SMO Address.vi"
File 28="user.lib/LevyLab/Leiden FP/Overrides/Get SMO Name.vi"
File 29="user.lib/LevyLab/Leiden FP/Overrides/Get SMO PGSQL Log Paths.vi"
File 30="user.lib/LevyLab/Leiden FP/Overrides/Get SMO Port.vi"
File 31="user.lib/LevyLab/Leiden FP/Overrides/Get SMO Public API.vi"
File 32="user.lib/LevyLab/Leiden FP/Overrides/Get SMO RC Type.vi"
File 33="user.lib/LevyLab/Leiden FP/Overrides/Handle Command.vi"
File 34="user.lib/LevyLab/Leiden FP/Overrides/Handle getAll.vi"
File 35="user.lib/LevyLab/Leiden FP/Overrides/Handle setConfiguration.vi"
File 36="user.lib/LevyLab/Leiden FP/Overrides/Read Configuration File.vi"
File 37="user.lib/LevyLab/Leiden FP/Overrides/Write Configuration File.vi"
File 38="user.lib/LevyLab/Leiden FP/API/Close.vi"
File 39="user.lib/LevyLab/Leiden FP/API/FP to PGSQL.vi"
File 40="user.lib/LevyLab/Leiden FP/API/Get Mode.vi"
File 41="user.lib/LevyLab/Leiden FP/API/Inst.FP.Create.vi"
File 42="user.lib/LevyLab/Leiden FP/API/Inst.FP.GetPublicEvents.vi"
File 43="user.lib/LevyLab/Leiden FP/API/Inst.FP.MessageFromProcess.vi"
File 44="user.lib/LevyLab/Leiden FP/API/Inst.FP.MessageToProcess.vi"
File 45="user.lib/LevyLab/Leiden FP/API/Open.vi"
File 46="user.lib/LevyLab/Leiden FP/API/Push Button.vi"
File 47="user.lib/LevyLab/Leiden FP/API/Set Mode.vi"
File 48="user.lib/LevyLab/Leiden FP/API/Write FP Type.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Leiden_FP.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
