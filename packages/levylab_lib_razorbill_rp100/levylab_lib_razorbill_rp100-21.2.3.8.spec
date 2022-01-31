[Package]
Name="levylab_lib_razorbill_rp100"
Version="21.2.3.8"
Release=""
ID=c10feed8977900c586702429ebee9b69
File Format="vip"
Format Version="2017"
Display Name="Razorbill RP100"


[Description]
Description="Divers for Razorbill RP100 HV amplifier"
Summary=""
License=""
Copyright="Copyright (c) 2022, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[21.2.4]\0A- Update to  IF 1.11.1.15"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="FALSE"


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
Requires="jdp_science_jsontext>=1.6.7.107,jdp_science_lib_common_utilities>=1.3.0.14,jdp_science_postgresql>=0.3.5.23,jki_lib_caraya>=1.2.1.131,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.2.112,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_lvtoitx>=3.3.6.11,levylab_lib_xy_utilities>=1.4.0.17,mgi_lib_1d_array>=1.0.2.3,mgi_lib_error_handling>=1.1.1.3,mgi_lib_numeric>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_levylab_instruments>=1.11.1.15"
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
Num Files=36
File 0="user.lib/Levylab/Razorbill RP100/razorbill.lvproj"
File 1="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Process.vi"
File 2="user.lib/Levylab/Razorbill RP100/SMOs/RP100/RP100.lvclass"
File 3="user.lib/Levylab/Razorbill RP100/SMOs/RP100/RP100.TestLauncher.vi"
File 4="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Commands--Enum.ctl"
File 5="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/getAll.ctl"
File 6="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Output Channel--Enum.ctl"
File 7="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/Output State--Enum.ctl"
File 8="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/setLevel--Cluster.ctl"
File 9="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Typedefs/SetStrain--Cluster.ctl"
File 10="user.lib/Levylab/Razorbill RP100/SMOs/RP100/private/convert V to d.vi"
File 11="user.lib/Levylab/Razorbill RP100/SMOs/RP100/private/RP100.Remote Client.vim"
File 12="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO Name.vi"
File 13="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO PGSQL Log Paths.vi"
File 14="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO Port.vi"
File 15="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Get SMO Public API.vi"
File 16="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Handle Command.vi"
File 17="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Methods (Overrides)/Handle getAll.vi"
File 18="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.CLS.vi"
File 19="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Get Level.vi"
File 20="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Get Output State.vi"
File 21="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Get Slew.vi"
File 22="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.IDN.vi"
File 23="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Measure Current.vi"
File 24="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Measure Voltage.vi"
File 25="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.RST.vi"
File 26="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Set Level.vi"
File 27="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Set Output State.vi"
File 28="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/RP100.Set Slew.vi"
File 29="user.lib/Levylab/Razorbill RP100/SMOs/RP100/Drivers/subVIs/RP100.VISA RW.vi"
File 30="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Close.vi"
File 31="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Get Level.vi"
File 32="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Get Strain.vi"
File 33="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Open.vi"
File 34="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Set Level.vi"
File 35="user.lib/Levylab/Razorbill RP100/SMOs/RP100/API/Set Strain.vi"


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
