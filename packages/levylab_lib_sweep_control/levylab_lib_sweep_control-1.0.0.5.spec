[Package]
Name="levylab_lib_sweep_control"
Version="1.0.0.5"
Release=""
ID=2a052468cb23470d94b3922b877f7722
File Format="vip"
Format Version="2017"
Display Name="Sweep Control"


[Description]
Description="[SweepControl.lvclass]\0A- Sweep Control.vi:\0A  - Sequencer for stepping multiple parameters. Calls VIs in Transport.lvclass\0A- Continuous B sweep.vi:\0A  - Sweep B continuously while asynchronously calling VIs in Transport.lvclass"
Summary=""
License=""
Copyright="Copyright (c) 2023, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="SweepControl.lvclass\0A- first build as stand-alone package"
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
Requires="i3_external_encryption>=1.0.0.8,jdp_science_jsontext>=1.7.0.118,jdp_science_lib_common_utilities>=1.4.1.18,jdp_science_postgresql>=0.3.1.20,jki_lib_caraya>=1.4.2.145,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.3.113,labview_open_source_lib_epoch_datetime>=1.2.0.6,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.10.3,levylab_lib_krohn_hite_7008>=1.7.9.1,levylab_lib_lockin_multichannel>=2.15.4.4,levylab_lib_lvtoitx>=3.7.0.2,levylab_lib_plym>=1.0.1.3,levylab_lib_voltage_update>=1.0.3.5,levylab_lib_xy_utilities>=1.5.4.1,lvh_toolbox>=2.0.0.35,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,mgi_lib_tree>=1.0.4.4,national_instruments_lib_guid_generator>=1.0.2.3,ni_cloud_toolkit_for_aws>=1.1.0.1,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_boolean>=4.0.0.7,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_md5>=4.1.1.10,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
Conflicts=""


[Activation]
License File=""
Licensed Library=""


[Files]
Num File Groups="2"
Sub-Packages=""
Namespaces=""


[File Group 0]
Target Dir="<application>"
Replace Mode="Always"
Num Files=35
File 0="user.lib/Levylab/Transport-ControlExperiment/Continuous B sweep.vi"
File 1="user.lib/Levylab/Transport-ControlExperiment/Process.vi"
File 2="user.lib/Levylab/Transport-ControlExperiment/Sweep Control Cartesian.vi"
File 3="user.lib/Levylab/Transport-ControlExperiment/Sweep Control.lvclass"
File 4="user.lib/Levylab/Transport-ControlExperiment/Sweep Control.lvproj"
File 5="user.lib/Levylab/Transport-ControlExperiment/Sweep Control.TestLauncher.vi"
File 6="user.lib/Levylab/Transport-ControlExperiment/Sweep Control.vi"
File 7="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Cluster - ScanControl.ctl"
File 8="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Cluster - ScanParamters.ctl"
File 9="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Cluster - Sweep Control.ctl"
File 10="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Continuous B Sweep JSON--Cluster.ctl"
File 11="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Enum - Action.ctl"
File 12="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Enum - Experiments.ctl"
File 13="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Enum - PostAction.ctl"
File 14="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Enum - Priority.ctl"
File 15="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Lockin Sweep--Cluster.ctl"
File 16="user.lib/Levylab/Transport-ControlExperiment/Typedefs/PostAction.ctl"
File 17="user.lib/Levylab/Transport-ControlExperiment/Typedefs/ScanControl.ctl"
File 18="user.lib/Levylab/Transport-ControlExperiment/Typedefs/ScanParamters.ctl"
File 19="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Sweep Control JSON--Cluster.ctl"
File 20="user.lib/Levylab/Transport-ControlExperiment/Typedefs/Sweep Control.Dependencies--Cluster.ctl"
File 21="user.lib/Levylab/Transport-ControlExperiment/Typedefs/XP Style VISA Control.ctl"
File 22="user.lib/Levylab/Transport-ControlExperiment/subVIs/Create Scan.vi"
File 23="user.lib/Levylab/Transport-ControlExperiment/subVIs/Post action.vi"
File 24="user.lib/Levylab/Transport-ControlExperiment/subVIs/Scan action.vi"
File 25="user.lib/Levylab/Transport-ControlExperiment/subVIs/Sort Scan Parameters.vi"
File 26="user.lib/Levylab/Transport-ControlExperiment/subVIs/Sweep Control Inner Loop.vi"
File 27="user.lib/Levylab/Transport-ControlExperiment/subVIs/Sweep Control Loop.vi"
File 28="user.lib/Levylab/Transport-ControlExperiment/API (file)/Read Continuous B Sweep.json.vi"
File 29="user.lib/Levylab/Transport-ControlExperiment/API (file)/Read Sweep Control.json.vi"
File 30="user.lib/Levylab/Transport-ControlExperiment/API/Read Dependencies.vi"
File 31="user.lib/Levylab/Transport-ControlExperiment/API/Read Sweep Configuration Example.vi"
File 32="user.lib/Levylab/Transport-ControlExperiment/API/Read Sweep Configuration File.vi"
File 33="user.lib/Levylab/Transport-ControlExperiment/API/Take Measurement.vi"
File 34="user.lib/Levylab/Transport-ControlExperiment/API/Write Dependencies.vi"


[File Group 1]
Target Dir="<menus>/Categories"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_sweep_control_1.mnu"
File 1="_functions_levylab_lib_sweep_control_2.mnu"
File 2="_functions_levylab_lib_sweep_control_3.mnu"
File 3="functions_Levylab_lib_sweep_control.mnu"
