[Package]
Name="levylab_lib_ah2500a"
Version="1.1.1.4"
Release=""
ID=1f011e60b6ea7c9ebe64e68646851760
File Format="vip"
Format Version="2017"
Display Name="AH2500A"


[Description]
Description="LabVIEW drivers for Andeen-Hagerling 2500A capacitance bridge"
Summary=""
License=""
Copyright="Copyright (c) 2021, Levylab"
Distribution=""
Vendor="Levylab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.1.1]\0A- Update to LV2019 and Instrument Framework v1.11.0"
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
Requires="jdp_science_jsontext>=1.6.5.105,jdp_science_lib_common_utilities>=1.3.0.14,jdp_science_postgresql>=0.3.5.23,jki_lib_caraya>=1.2.1.131,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.63,labview-zmq>=3.6.1.111,lava_lib_ui_tools>=1.4.1.74,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_lvtoitx>=3.3.3.7,levylab_lib_xy_utilities>=1.4.0.17,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_levylab_instruments>=1.11.0.10"
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
Num Files=11
File 0="user.lib/Levylab/AH2500A/AH2500A.lvproj"
File 1="user.lib/Levylab/AH2500A/SMOs/AH2500A/AH2500A.lvclass"
File 2="user.lib/Levylab/AH2500A/SMOs/AH2500A/AH2500A.TestLauncher.vi"
File 3="user.lib/Levylab/AH2500A/SMOs/AH2500A/Process.vi"
File 4="user.lib/Levylab/AH2500A/SMOs/AH2500A/Typedefs/AH2500A Measurement--Cluster.ctl"
File 5="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Read Instrument.vi"
File 6="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set Average Time.vi"
File 7="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set DC Bias.vi"
File 8="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set Max AC voltage.vi"
File 9="user.lib/Levylab/AH2500A/SMOs/AH2500A/drivers/Set Units.vi"
File 10="user.lib/Levylab/AH2500A/SMOs/AH2500A/API/Get Capacitance.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_AH2500A.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
