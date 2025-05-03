[Package]
Name="levylab_lib_database_viewer"
Version="2025.5.2.4"
Release=""
ID=c1fd4f0c5c4e644c1996136f59faf18b
File Format="vip"
Format Version="2017"
Display Name="Database Viewer"


[Description]
Description="Visualize data from database (postgres/timescale)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin, Jack Maier, Yun-Yi Pai"
Demo="FALSE"
Release Notes="- build with Epoch 1.3\0A- build with g-cli\0A- add Configuration.lvclass as package dependency"
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
Requires="i3_external_encryption>=1.0.0.8,jdp_science_lib_common_utilities>=1.4.2.19,jdp_science_postgresql>=0.6.2.48,jki_lib_caraya>=1.4.3.147,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,labview_open_source_lib_epoch_datetime>=1.3.0.8,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.11.4,levylab_lib_lvtdatpgsql>=3.9.2.7,levylab_lib_lvtoitx>=3.9.2.7,levylab_lib_xy_utilities>=1.6.0.6,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_numeric>=1.1.0.2,mgi_lib_string>=1.1.1.5,mgi_lib_tree>=1.0.4.4,national_instruments_lib_guid_generator>=1.0.2.3,ni_cloud_toolkit_for_aws>=1.1.0.1,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_md5>=4.1.1.10,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5,levylab_lib_configuration>=1.1.0.6"
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
Num Files=22
File 0="user.lib/LevyLab/Database Viewer/Database Viewer/Database Viewer.lvclass"
File 1="user.lib/LevyLab/Database Viewer/Database Viewer/Database Viewer.vi"
File 2="user.lib/LevyLab/Database Viewer/Database Viewer/test.vi"
File 3="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/DELETE_Database--enum.ctl"
File 4="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/Time Bucket--enum.ctl"
File 5="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/Time Mode--enum.ctl"
File 6="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/UI Controls--cluster.ctl"
File 7="user.lib/LevyLab/Database Viewer/Database Viewer/private/Calculate Optimal Timebucket.vi"
File 8="user.lib/LevyLab/Database Viewer/Database Viewer/private/Construct SQL.vi"
File 9="user.lib/LevyLab/Database Viewer/Database Viewer/private/Convert Times to Interval and Span.vi"
File 10="user.lib/LevyLab/Database Viewer/Database Viewer/private/Execute SQL.vi"
File 11="user.lib/LevyLab/Database Viewer/Database Viewer/private/Filter Traces.vi"
File 12="user.lib/LevyLab/Database Viewer/Database Viewer/private/Get Traces.vi"
File 13="user.lib/LevyLab/Database Viewer/Database Viewer/private/Median Filter.vi"
File 14="user.lib/LevyLab/Database Viewer/Database Viewer/private/PG Path to Plot Label From Cursor.vi"
File 15="user.lib/LevyLab/Database Viewer/Database Viewer/private/PG Path to Plot Label.vi"
File 16="user.lib/LevyLab/Database Viewer/Database Viewer/private/Remove Bad Points.vi"
File 17="user.lib/LevyLab/Database Viewer/Database Viewer/private/Set Time Graph X Axis.vi"
File 18="user.lib/LevyLab/Database Viewer/Database Viewer/private/SQL Results to Trace.vi"
File 19="user.lib/LevyLab/Database Viewer/Database Viewer/private/SQL Time to Timestamp.vi"
File 20="user.lib/LevyLab/Database Viewer/Database Viewer/private/State History.vi"
File 21="user.lib/LevyLab/Database Viewer/Database Viewer/private/Var_Axis.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=2
File 0="_functions_levylab_lib_database_viewer_1.mnu"
File 1="functions_LevyLab_lib_database_viewer.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
