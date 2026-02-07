[Package]
Name="levylab_lib_database_viewer"
Version="2026.2.7.9"
Release=""
ID=c20431080db8cac211c465a13f56aa46
File Format="vip"
Format Version="2017"
Display Name="Database Viewer"


[Description]
Description="Visualize data from database (postgres/timescale)"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2026, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin, Jack Maier, Yun-Yi Pai"
Demo="FALSE"
Release Notes="- build with pgsql/3.12.1.15 (hotfix for connection key)"
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
Requires="levylab_lib_configuration>=1.1.0.6,levylab_lib_lvtdatpgsql>=3.12.0.14"
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
File 2="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/DELETE_Database--enum.ctl"
File 3="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/Time Bucket--enum.ctl"
File 4="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/Time Mode--enum.ctl"
File 5="user.lib/LevyLab/Database Viewer/Database Viewer/typedefs/UI Controls--cluster.ctl"
File 6="user.lib/LevyLab/Database Viewer/Database Viewer/private/Calculate Optimal Timebucket.vi"
File 7="user.lib/LevyLab/Database Viewer/Database Viewer/private/Construct SQL.vi"
File 8="user.lib/LevyLab/Database Viewer/Database Viewer/private/Convert Times to Interval and Span.vi"
File 9="user.lib/LevyLab/Database Viewer/Database Viewer/private/Execute SQL.vi"
File 10="user.lib/LevyLab/Database Viewer/Database Viewer/private/Filter Traces.vi"
File 11="user.lib/LevyLab/Database Viewer/Database Viewer/private/Get Traces.vi"
File 12="user.lib/LevyLab/Database Viewer/Database Viewer/private/Median Filter.vi"
File 13="user.lib/LevyLab/Database Viewer/Database Viewer/private/PG Path to Plot Label From Cursor.vi"
File 14="user.lib/LevyLab/Database Viewer/Database Viewer/private/PG Path to Plot Label.vi"
File 15="user.lib/LevyLab/Database Viewer/Database Viewer/private/Remove Bad Points.vi"
File 16="user.lib/LevyLab/Database Viewer/Database Viewer/private/Set Time Graph X Axis.vi"
File 17="user.lib/LevyLab/Database Viewer/Database Viewer/private/SQL Results to Trace.vi"
File 18="user.lib/LevyLab/Database Viewer/Database Viewer/private/SQL Time to Timestamp.vi"
File 19="user.lib/LevyLab/Database Viewer/Database Viewer/private/State History.vi"
File 20="user.lib/LevyLab/Database Viewer/Database Viewer/private/test_list.vi"
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
