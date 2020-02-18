[Package]
Name="levylab_lib_oxford_1820_api"
Version="1.1.3.11"
Release=""
ID=d89dcca1879df76f4df24422d679eb6a
File Format="vip"
Format Version="2017"
Display Name="Oxford 1820 API"


[Description]
Description="VIs for controlling the Oxford 18/20 magnet"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="build with Instrument v1.5.7.69"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,oglib_appcontrol>=4.1.0.7,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3"
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
Num Files=101
File 0="user.lib/Levylab/Oxford-1820-Main-Launcher.vi"
File 1="user.lib/Levylab/Oxford-1820-Main.lvproj"
File 2="user.lib/Levylab/Oxford-1820-Main.vi"
File 3="user.lib/Levylab/Oxford-1820-Main_.vi"
File 4="user.lib/Levylab/SMOs/Instrument.Oxford1820 UI/Create UI.vi"
File 5="user.lib/Levylab/SMOs/Instrument.Oxford1820 UI/Instrument.Oxford1820 UI.lvclass"
File 6="user.lib/Levylab/SMOs/Instrument.Oxford1820 UI/Oxford1820 UI.TestLauncher.vi"
File 7="user.lib/Levylab/SMOs/Instrument.Oxford1820 UI/Process.vi"
File 8="user.lib/Levylab/SMOs/Instrument.Oxford1820 UI/Typedefs/Customize Meter.vi"
File 9="user.lib/Levylab/SMOs/Instrument.Oxford1820 UI/Typedefs/Meter 2.ctl"
File 10="user.lib/Levylab/SMOs/Instrument.Oxford1820 UI/Typedefs/Meter.ctl"
File 11="user.lib/Levylab/SMOs/Instrument.Oxford1820/AppLauncher.vi"
File 12="user.lib/Levylab/SMOs/Instrument.Oxford1820/Instrument.Oxford1820.lvclass"
File 13="user.lib/Levylab/SMOs/Instrument.Oxford1820/Instrument.Oxford1820.TestLauncher.vi"
File 14="user.lib/Levylab/SMOs/Instrument.Oxford1820/Process.vi"
File 15="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/Actions.ctl"
File 16="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/Fill Mode-Combo.ctl"
File 17="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/getAll.ctl"
File 18="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/Instrument.Oxford1820.Commands-combo.ctl"
File 19="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/Instrument.Oxford1820.Commands-enum.ctl"
File 20="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/Instrument.Oxford1820.setMagnet-cluster.ctl"
File 21="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/PrivateEvents--Cluster.ctl"
File 22="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/PrivateEvents--Instrument.Oxford1820.SequenceSetMagnetField.ctl"
File 23="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/Status.ctl"
File 24="user.lib/Levylab/SMOs/Instrument.Oxford1820/Typedefs/Targets.ctl"
File 25="user.lib/Levylab/SMOs/Instrument.Oxford1820/public/Mercury_GoToField.vi"
File 26="user.lib/Levylab/SMOs/Instrument.Oxford1820/public/Read_MNK_B_Field.vi"
File 27="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/1820_Calculate_Sweep_Time.vi"
File 28="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/1820_IPS_to_DSC.vi"
File 29="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/1820_ITC_to_DSC.vi"
File 30="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/1820_LPF_ON_duration.vi"
File 31="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/1820_PS_ON_duration.vi"
File 32="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/API Test.vi"
File 33="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/check HOLD and resend.vi"
File 34="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/check RTOS and resend.vi"
File 35="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Instrument.Oxford1820.GetPrivateEvents.vi"
File 36="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Instrument.Oxford1820.SequenceSetMagnetField.vi"
File 37="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/IPSReplytoDSC.vi"
File 38="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/ITCReplytoDSC.vi"
File 39="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Mercury_GoToField_SubVI.vi"
File 40="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/MercuryStateHistory.vi"
File 41="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/NetVarWrite_dbl.vi"
File 42="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/NetVarWrite_str.vi"
File 43="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Open IPS.vi"
File 44="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Open ITC.vi"
File 45="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Ramp PSU to Magnet.vi"
File 46="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Ramp PSU to Target.vi"
File 47="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Set Persistent Mode.vi"
File 48="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/StarTrekIndicator.vi"
File 49="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/wait HOLD.vi"
File 50="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/wait Targets match.vi"
File 51="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Level.vi"
File 52="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Magnet Current.vi"
File 53="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Magnet Field.vi"
File 54="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Magnet Temperature.vi"
File 55="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU Current Voltage.vi"
File 56="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU Field.vi"
File 57="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU Targets.vi"
File 58="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU1 Current Voltage.vi"
File 59="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU2 Current Voltage.vi"
File 60="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU3 Current Voltage.vi"
File 61="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Status.vi"
File 62="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Switch Heater.vi"
File 63="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read ITC LPF Needle Valve.vi"
File 64="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Read ITC LPF Pressure.vi"
File 65="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS Action.vi"
File 66="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS Fill Mode.vi"
File 67="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS PSU Targets.vi"
File 68="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS Switch Heater.vi"
File 69="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Set ITC LPF Needle Valve.vi"
File 70="user.lib/Levylab/SMOs/Instrument.Oxford1820/Private/Handle Command/Set ITC LPF State.vi"
File 71="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/Close Instrument.vi"
File 72="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/CreatePrivateEvents.vi"
File 73="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/Get SMO Name.vi"
File 74="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/Get SMO Port.vi"
File 75="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/Get SMO Public API.vi"
File 76="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/getAll.vi"
File 77="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/Handle Command.vi"
File 78="user.lib/Levylab/SMOs/Instrument.Oxford1820/Methods (Overrides)/Open Instrument.vi"
File 79="user.lib/Levylab/SMOs/Instrument.Oxford1820/FGV/FGV_PSP - Mercury Action Status.vi"
File 80="user.lib/Levylab/SMOs/Instrument.Oxford1820/FGV/FGV_PSP - Mercury Actions.vi"
File 81="user.lib/Levylab/SMOs/Instrument.Oxford1820/FGV/FGV_PSP - Mercury Remote.vi"
File 82="user.lib/Levylab/SMOs/Instrument.Oxford1820/FGV/FGV_PSP - Mercury Status.vi"
File 83="user.lib/Levylab/SMOs/Instrument.Oxford1820/FGV/FGV_PSP - Mercury Targets.vi"
File 84="user.lib/Levylab/SMOs/Instrument.Oxford1820/Examples/Tree.vi"
File 85="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Clamp.vi"
File 86="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Get PSU Field.vi"
File 87="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Get Status.vi"
File 88="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Get Switch Heat.vi"
File 89="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Get Target.vi"
File 90="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Hold.vi"
File 91="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Instrument.1820.FloatApprox.vi"
File 92="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Instrument.Oxford1820.Client.vi"
File 93="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Ramp to Set.vi"
File 94="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Ramp to Zero.vi"
File 95="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Set Fill Mode.vi"
File 96="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Set LPF State.vi"
File 97="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Set Switch Heater.vi"
File 98="user.lib/Levylab/SMOs/Instrument.Oxford1820/Community/Set Target.vi"
File 99="user.lib/Levylab/SMOs/Instrument.Oxford1820/API/Get Magnet Field.vi"
File 100="user.lib/Levylab/SMOs/Instrument.Oxford1820/API/Set Magnet Field.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Oxford_1820_API.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
