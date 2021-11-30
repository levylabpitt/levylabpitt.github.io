[Package]
Name="levylab_lib_leiden_tc"
Version="1.0.2.6"
Release=""
ID=411b83a5f07db7da13d631fca7143ecf
File Format="vip"
Format Version="2017"
Display Name="LEIDEN TC"


[Description]
Description="Tools used by LevyLab to interact with Leiden Temperature Control (TC)\0D\0A\0D\0A[Instrument.TC.MNK.lvclass]\0D\0A[Instrument.TC.CF.lvclass]\0D\0A- APIs that overrides "Get Temperature.vi" method of Instrument.Cryostat.lvclass"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.2]\0D\0A- Fix CF Read T"
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
Requires="jdp_science_jsontext>=1.6.7.107,jdp_science_lib_common_utilities>=1.3.0.14,jdp_science_postgresql>=0.3.5.23,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,jki_statemachineobjects>=1.4.0.63,labview-zmq>=3.6.1.111,lava_lib_ui_tools>=1.4.1.74,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.7.10,levylab_lib_lvtoitx>=3.3.5.10,levylab_lib_xy_utilities>=1.4.0.17,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,national_instruments_lib_guid_generator>=1.0.2.3,ni_lib_stm>=3.1.0.9,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_levylab_instruments>=1.11.1.13"
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
File 0="user.lib/LevyLab/Leiden TC/Instrument.TC.lvproj"
File 1="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Instrument.TC.MNK.lvclass"
File 2="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Instrument.TC.MNK.TestLauncher.vi"
File 3="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Process.vi"
File 4="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/Private/Read_MNK_Temperature.vi"
File 5="user.lib/LevyLab/Leiden TC/Instrument.TC.MNK/API/Get Temperature.vi"
File 6="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Instrument.TC.CF.lvclass"
File 7="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Instrument.TC.CF.TestLauncher.vi"
File 8="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Process.vi"
File 9="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/Private/Read_CF_Temperature.vi"
File 10="user.lib/LevyLab/Leiden TC/Instrument.TC.CF/API/Get Temperature.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=1
File 0="functions_LevyLab_lib_Leiden_TC.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
