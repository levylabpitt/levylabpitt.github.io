[Package]
Name="levylab_lib_oxford_vrm_api"
Version="21.5.12.2"
Release=""
ID=1f07e660b22d87837ec9bcf05758df83
File Format="vip"
Format Version="2017"
Display Name="Oxford-VRM"


[Description]
Description="VIs for controlling the Oxford VRM PS that controls the CF900's 3D magnet"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="- Initial build"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


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
Requires="jdp_science_postgresql>=0.3.4.22,jki_lib_caraya>=1.1.0.119,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,jki_statemachineobjects>=1.3.0.56,labview-zmq>=3.5.1.109,lava_lib_ui_tools>=1.4.1.74,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_lvtoitx>=3.0.6.14,levylab_lib_postgresql>=1.4.0.22,levylab_lib_xy_utilities>=1.4.0.17,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5"
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
Num Files=80
File 0="user.lib/Levylab/Oxford-VRM/Oxford-VRM-Main-Launcher.vi"
File 1="user.lib/Levylab/Oxford-VRM/Oxford-VRM.lvproj"
File 2="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Handle Error.vi"
File 3="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Instrument.OxfordVRM UI.lvclass"
File 4="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/OxfordVRM UI.TestLauncher.vi"
File 5="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Process.vi"
File 6="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Typedefs/Customize Meter.vi"
File 7="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Typedefs/Meter 2.ctl"
File 8="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Typedefs/Meter.ctl"
File 9="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Private/StarTrekIndicator.vi"
File 10="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Private/VRM Field Graphs.vi"
File 11="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM UI/Private/VRM State History.vi"
File 12="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/AppLauncher.vi"
File 13="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Instrument.Oxford1820.TestLauncher.vi"
File 14="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Instrument.OxfordVRM.lvclass"
File 15="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Process.vi"
File 16="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/getAll.ctl"
File 17="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/Instrument.VRM.Commands-combo.ctl"
File 18="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/Instrument.VRM.Commands-enum.ctl"
File 19="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/Instrument.VRM.setMagnet-cluster.ctl"
File 20="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PrivateEvents--Cluster.ctl"
File 21="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PrivateEvents--Instrument.Oxford1820.AbortSequence.ctl"
File 22="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PrivateEvents--Instrument.Oxford1820.SequenceSetMagnetField.ctl"
File 23="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PublicEvents--Cluster.ctl"
File 24="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/PublicEvents--Instrument.Oxford1820.ProcessStatus.ctl"
File 25="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/VRM Action-Axis--Cluster.ctl"
File 26="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/VRM Magnet Axis--Enum.ctl"
File 27="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Typedefs/VRM Targets--Cluster.ctl"
File 28="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Inheritance test.vi"
File 29="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Open Close.vi"
File 30="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Open IPS.vi"
File 31="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Ramp Field.vi"
File 32="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Test Set PSU.vi"
File 33="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Tests/Unit Test.vi"
File 34="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Instrument.Oxford1820.GetPrivateEvents.vi"
File 35="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Instrument.Oxford1820.ProcessStatus.vi"
File 36="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Instrument.Oxford1820.SequenceSetMagnetField.vi"
File 37="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/IPS Reply to PGSQL.vi"
File 38="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Open IPS.vi"
File 39="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/VRM Calculate Sweep Rates.vi"
File 40="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Ramp PSU to Target.vi"
File 41="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Current Voltage.vi"
File 42="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Field.vi"
File 43="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Group Current Voltage.vi"
File 44="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS PSU Target.vi"
File 45="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Read IPS Status.vi"
File 46="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Set IPS Action.vi"
File 47="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Private/Handle Command/Set IPS PSU Target.vi"
File 48="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Close Instrument.vi"
File 49="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/CreatePrivateEvents.vi"
File 50="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/CreatePublicEvents.vi"
File 51="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/DestroyPrivateEvents.vi"
File 52="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO Name.vi"
File 53="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO PGSQL Log Paths.vi"
File 54="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO Port.vi"
File 55="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Get SMO Public API.vi"
File 56="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/getAll.vi"
File 57="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Handle Command.vi"
File 58="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Methods (Overrides)/Open Instrument.vi"
File 59="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Action Status to Text.vi"
File 60="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Calculate Sweep ETA.vi"
File 61="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Clamp.vi"
File 62="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/FloatApprox (Array).vi"
File 63="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/FloatApprox.vi"
File 64="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Get Field.vi"
File 65="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Get Status.vi"
File 66="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Get Target.vi"
File 67="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Hold.vi"
File 68="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Instrument.OxfordVRM.Client.vi"
File 69="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Ramp to Set.vi"
File 70="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Ramp to Zero.vi"
File 71="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Set Target.vi"
File 72="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/Variant to Reply String.vi"
File 73="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/VRM Cartesian to Spherical.vi"
File 74="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/Community/VRM Spherical to Cartesian.vi"
File 75="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Get Magnet Field.vi"
File 76="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Instrument.Oxford1820.AbortSequence.vi"
File 77="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Instrument.Oxford1820.GetPublicEvents.vi"
File 78="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Set Magnet Field.vi"
File 79="user.lib/Levylab/Oxford-VRM/SMOs/Instrument.OxfordVRM/API/Set Magnet Vector Field.vi"


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
