[Package]
Name="levylab_lib_oxford_vrm_api"
Version="1.7.1.5"
Release=""
ID=eb5872e491af277bed929348049f3a4b
File Format="vip"
Format Version="2017"
Display Name="Oxford-VRM"


[Description]
Description="VIs for controlling the Oxford VRM PS that controls the CF900's 3D magnet"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.7.1]\0A- Mercury drivers not included"
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
PostInstall="<OS User Documents>\\GitHub\\Oxford-VRM\\build support\\Post-Install Custom Action.vi"
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
Num Files=84
File 0="user.lib/Levylab/Oxford-VRM/Oxford-VRM-Main-Launcher.vi"
File 1="user.lib/Levylab/Oxford-VRM/Oxford-VRM.lvproj"
File 2="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Instrument.OxfordVRM UI.lvclass"
File 3="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/OxfordVRM UI.TestLauncher.vi"
File 4="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Process.vi"
File 5="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Typedefs/Customize Meter.vi"
File 6="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Typedefs/Meter 2.ctl"
File 7="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Typedefs/Meter.ctl"
File 8="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Private/StarTrekIndicator.vi"
File 9="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Private/VRM Field Graphs.vi"
File 10="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Private/VRM State History.vi"
File 11="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/AppLauncher.vi"
File 12="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Instrument.OxfordVRM.lvclass"
File 13="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Instrument.OxfordVRM.TestLauncher.vi"
File 14="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Process.vi"
File 15="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/getAll.ctl"
File 16="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/Instrument.VRM.Commands-combo.ctl"
File 17="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/Instrument.VRM.Commands-enum.ctl"
File 18="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/Instrument.VRM.setMagnet-cluster.ctl"
File 19="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PrivateEvents--Cluster.ctl"
File 20="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PrivateEvents--Instrument.OxfordVRM.AbortSequence.ctl"
File 21="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PrivateEvents--Instrument.OxfordVRM.SequenceSetMagnetField.ctl"
File 22="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PublicEvents--Cluster.ctl"
File 23="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PublicEvents--Instrument.OxfordVRM.ProcessStatus.ctl"
File 24="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/VRM Action-Axis--Cluster.ctl"
File 25="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/VRM Magnet Axis--Enum.ctl"
File 26="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/VRM Targets--Cluster.ctl"
File 27="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Inheritance test.vi"
File 28="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Open Close.vi"
File 29="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Open IPS.vi"
File 30="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Ramp Field.vi"
File 31="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Set PSU.vi"
File 32="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Unit Test.vi"
File 33="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Instrument.OxfordVRM.GetPrivateEvents.vi"
File 34="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Instrument.OxfordVRM.ProcessStatus.vi"
File 35="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Instrument.OxfordVRM.SequenceSetMagnetField.vi"
File 36="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/IPS Reply to PGSQL.vi"
File 37="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Open IPS.vi"
File 38="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/VRM Calculate Sweep Rates.vi"
File 39="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Ramp PSU to Target.vi"
File 40="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Current Voltage.vi"
File 41="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Field.vi"
File 42="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Group Current Voltage.vi"
File 43="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Target.vi"
File 44="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS Status.vi"
File 45="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Set IPS Action.vi"
File 46="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Set IPS PSU Target.vi"
File 47="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Close Hardware.vi"
File 48="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/CreatePrivateEvents.vi"
File 49="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/CreatePublicEvents.vi"
File 50="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/DestroyPrivateEvents.vi"
File 51="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO Name.vi"
File 52="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO PGSQL Log Paths.vi"
File 53="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO Port.vi"
File 54="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO Public API.vi"
File 55="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Handle Command.vi"
File 56="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Handle getAll.vi"
File 57="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Open Hardware.vi"
File 58="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Read Configuration File.vi"
File 59="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Write Configuration File.vi"
File 60="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Action Status to Text.vi"
File 61="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Calculate Sweep ETA.vi"
File 62="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Clamp.vi"
File 63="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Get Field.vi"
File 64="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Get Status.vi"
File 65="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Get Target.vi"
File 66="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Hold.vi"
File 67="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Instrument.OxfordVRM.FloatApprox (Array).vi"
File 68="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Instrument.OxfordVRM.FloatApprox.vi"
File 69="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Instrument.OxfordVRM.Remote Client.vim"
File 70="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Ramp to Set.vi"
File 71="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Ramp to Zero.vi"
File 72="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Set Target.vi"
File 73="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Variant to Reply String.vi"
File 74="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/VRM Cartesian to Spherical.vi"
File 75="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/VRM Spherical to Cartesian.vi"
File 76="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Close.vi"
File 77="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Get Magnet Vector Field.vi"
File 78="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Get Magnet.vi"
File 79="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Instrument.OxfordVRM.AbortSequence.vi"
File 80="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Instrument.OxfordVRM.GetPublicEvents.vi"
File 81="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Open.vi"
File 82="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Set Magnet Vector Field.vi"
File 83="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Set Magnet.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_Oxford_VRM_API.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
