[Package]
Name="levylab_lib_oxford_1820_api"
Version="1.3.6.2"
Release=""
ID=353a9265df0913559b62c239a0fed1b4
File Format="vip"
Format Version="2017"
Display Name="Oxford-1820"


[Description]
Description="VIs for controlling the Oxford 18/20 magnet"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2022, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Change Get Magnet.vi to directly ask SMO for value (backup to asking PGSQL)\0A- Change UI from 2.5 to 2.0 s getAll timout\0A- Update to Instrument Framework v1.11.3.2 (fixes issues with PGSQL logging)\0A- Minor changes to Handle Command variant to string"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


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
Requires="levylab_lib_levylab_instruments>=1.11.2.1"
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
Num Files=99
File 0="user.lib/Levylab/Oxford-1820/Oxford-1820-Main-Launcher.vi"
File 1="user.lib/Levylab/Oxford-1820/Oxford-1820.lvproj"
File 2="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Instrument UI.Oxford1820.lvclass"
File 3="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Level Color.vi"
File 4="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Oxford1820 UI.TestLauncher.vi"
File 5="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Process.vi"
File 6="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Time-Y Circ Buffer.vi"
File 7="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Typedefs/Customize Meter.vi"
File 8="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Typedefs/Meter 2.ctl"
File 9="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820 UI/Typedefs/Meter.ctl"
File 10="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/AppLauncher.vi"
File 11="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Instrument.Oxford1820.lvclass"
File 12="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Instrument.Oxford1820.TestLauncher.vi"
File 13="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Process.vi"
File 14="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/Actions.ctl"
File 15="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/Fill Mode-Combo.ctl"
File 16="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/getAll.ctl"
File 17="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/Instrument.Oxford1820.Commands-combo.ctl"
File 18="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/Instrument.Oxford1820.Commands-enum.ctl"
File 19="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/PrivateEvents--Cluster.ctl"
File 20="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/PrivateEvents--Instrument.Oxford1820.AbortSequence.ctl"
File 21="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/PrivateEvents--Instrument.Oxford1820.SequenceSetMagnetField.ctl"
File 22="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/PublicEvents--Cluster.ctl"
File 23="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/PublicEvents--Instrument.Oxford1820.ProcessStatus.ctl"
File 24="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Typedefs/Status.ctl"
File 25="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Tests/Inheritance test.vi"
File 26="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Tests/Test Open Close.vi"
File 27="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/1820 State History.vi"
File 28="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Instrument.Oxford1820.GetPrivateEvents.vi"
File 29="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Instrument.Oxford1820.ProcessStatus.vi"
File 30="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Instrument.Oxford1820.SetSequence.vi"
File 31="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/IPS Reply to PGSQL.vi"
File 32="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/ITC Reply to PGSQL.vi"
File 33="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Open IPS.vi"
File 34="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Open ITC.vi"
File 35="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/StarTrekIndicator.vi"
File 36="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Ramp PSU to Magnet.vi"
File 37="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Ramp PSU to Target.vi"
File 38="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Level.vi"
File 39="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Magnet Current.vi"
File 40="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Magnet Field.vi"
File 41="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU Current Voltage.vi"
File 42="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU Field.vi"
File 43="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU Targets.vi"
File 44="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU1 Current Voltage.vi"
File 45="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU2 Current Voltage.vi"
File 46="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS PSU3 Current Voltage.vi"
File 47="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Status.vi"
File 48="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Switch Heater.vi"
File 49="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read IPS Temperature.vi"
File 50="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read ITC LPF Needle Valve.vi"
File 51="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read ITC LPF Pressure.vi"
File 52="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Read ITC Temperature.vi"
File 53="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS Action.vi"
File 54="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS Fill Mode.vi"
File 55="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS PSU Targets.vi"
File 56="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Set IPS Switch Heater.vi"
File 57="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Set ITC LPF Needle Valve.vi"
File 58="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Private/Handle Command/Set ITC LPF State.vi"
File 59="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Close Hardware.vi"
File 60="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/CreatePrivateEvents.vi"
File 61="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/CreatePublicEvents.vi"
File 62="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/DestroyPrivateEvents.vi"
File 63="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Get SMO Name.vi"
File 64="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Get SMO PGSQL Log Paths.vi"
File 65="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Get SMO Port.vi"
File 66="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Get SMO Public API.vi"
File 67="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Handle Command.vi"
File 68="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Handle getAll.vi"
File 69="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Methods (Overrides)/Open Hardware.vi"
File 70="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/1820 LPF ON duration.vi"
File 71="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/1820 PS Heat duration.vi"
File 72="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/1820 Sweep ETA.vi"
File 73="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Action Status to Text.vi"
File 74="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Clamp.vi"
File 75="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Get Field.vi"
File 76="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Get PSU Field.vi"
File 77="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Get Status.vi"
File 78="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Get Switch Heat.vi"
File 79="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Get Target.vi"
File 80="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Hold.vi"
File 81="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Instrument.1820.FloatApprox.vi"
File 82="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Instrument.Oxford1820.Remote Client.vim"
File 83="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Ramp to Set.vi"
File 84="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Ramp to Zero.vi"
File 85="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Set Fill Mode.vi"
File 86="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Set LPF State.vi"
File 87="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Set Needle Valve.vi"
File 88="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Set Switch Heater.vi"
File 89="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Set Target.vi"
File 90="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Switch Status String to Boolean.vi"
File 91="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/Community/Variant to Reply String.vi"
File 92="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/API/Close.vi"
File 93="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/API/Get Magnet.vi"
File 94="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/API/Instrument.Oxford1820.AbortSequence.vi"
File 95="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/API/Instrument.Oxford1820.Get All.vi"
File 96="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/API/Instrument.Oxford1820.GetPublicEvents.vi"
File 97="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/API/Open.vi"
File 98="user.lib/Levylab/Oxford-1820/SMOs/Instrument.Oxford1820/API/Set Magnet.vi"


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
