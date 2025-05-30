[Package]
Name="levylab_lib_transport"
Version="1.9.0.11"
Release=""
ID=db9955d551d5bdb6f63d38718ed495a4
File Format="vip"
Format Version="2017"
Display Name="Transport"


[Description]
Description="VIs for scripting and performing transport measurments.\0A\0A[Transport.lvclass]\0ABasic transport measurments:\0A- Lockin vs time (Lockin_time.vi)\0A- Lockin Sweep Mode (Lockin_sweep.vi)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.9.0]\0A- #93/#94: Updates related to Instrument Framework"
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
Requires="ftdi_lib_d2xx>=1.2.0.5,i3_external_encryption>=1.0.0.8,jdp_science_jsontext>=1.9.1.125,jdp_science_lib_common_utilities>=1.4.2.19,jdp_science_postgresql>=0.6.2.48,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,jki_statemachineobjects>=1.4.0.69,labview-zmq>=3.6.3.113,labview_open_source_lib_epoch_datetime>=1.3.0.8,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_instrument_type>=1.1.0.7,levylab_lib_krohn_hite_7008>=2.2.1.15,levylab_lib_lockin_multichannel>=2.20.1.9,levylab_lib_lvtdatpgsql>=3.10.0.8,levylab_lib_lvtoitx>=3.10.0.9,levylab_lib_plym>=1.0.1.3,levylab_lib_xy_utilities>=1.6.0.6,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,mgi_lib_tree>=1.0.4.4,national_instruments_lib_guid_generator>=1.0.2.3,ni_cloud_toolkit_for_aws>=1.1.0.1,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_boolean>=4.0.0.7,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_md5>=4.1.1.10,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,prirvin_lib_json_rpc>=1.2.6.15,prirvin_lib_json_schema>=0.1.4.8,wireflow_ab_lib_wf_progressbar>=1.0.2.56,levylab_lib_control_experiment>=1.2.0.10"
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
Num Files=23
File 0="user.lib/Levylab/Transport/Transport/Lockin_AIWFM_time.vi"
File 1="user.lib/Levylab/Transport/Transport/Lockin_sweep.vi"
File 2="user.lib/Levylab/Transport/Transport/Lockin_time.vi"
File 3="user.lib/Levylab/Transport/Transport/Sweep_AIWFM_time.vi"
File 4="user.lib/Levylab/Transport/Transport/THz_TimeDelay.vi"
File 5="user.lib/Levylab/Transport/Transport/Transport.lvclass"
File 6="user.lib/Levylab/Transport/Transport/Typedefs/Lockin_Sweep JSON--Cluster.ctl"
File 7="user.lib/Levylab/Transport/Transport/Typedefs/Transport.Dependencies--Cluster.ctl"
File 8="user.lib/Levylab/Transport/Transport/Private/Calculate R and G (Four Terminal).vi"
File 9="user.lib/Levylab/Transport/Transport/Private/Calculate R and G (Two Terminal).vi"
File 10="user.lib/Levylab/Transport/Transport/Private/Calculate R and G 2.vi"
File 11="user.lib/Levylab/Transport/Transport/Private/Exec State to Append.vi"
File 12="user.lib/Levylab/Transport/Transport/Private/Graph Lockin vs Parameter.vi"
File 13="user.lib/Levylab/Transport/Transport/Private/Graph R and G vs Parameter.vi"
File 14="user.lib/Levylab/Transport/Transport/Private/Results (2D) to X and Y Arrays.vi"
File 15="user.lib/Levylab/Transport/Transport/Private/Results (Dictionary) to X and Y Arrays.vi"
File 16="user.lib/Levylab/Transport/Transport/Private/State History.vi"
File 17="user.lib/Levylab/Transport/Transport/API (file)/Read Lockin_Sweep.json.vi"
File 18="user.lib/Levylab/Transport/Transport/API (class)/Read Dependencies.vi"
File 19="user.lib/Levylab/Transport/Transport/API (class)/Write Configure Sweep.vi"
File 20="user.lib/Levylab/Transport/Transport/API (class)/Write Dependencies.vi"
File 21="user.lib/Levylab/Transport/Transport/API (class)/Write notifier.vi"
File 22="user.lib/Levylab/Transport/Transport/API (class)/Write Sweep Table.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="Always"
Num Files=4
File 0="_functions_levylab_lib_transport_1.mnu"
File 1="_functions_levylab_lib_transport_2.mnu"
File 2="_functions_levylab_lib_transport_3.mnu"
File 3="functions_Levylab_lib_Transport.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/Transport"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
