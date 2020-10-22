[Package]
Name="levylab_lib_postgresql"
Version="1.0.0.2"
Release=""
ID=63e34818b8ad0d4208313cda0cc4051a
File Format="vip"
Format Version="2017"
Display Name="postgreSQL/timescaleDB"


[Description]
Description="VIs for interacting with postgreSQL /timescaleDB"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="first build"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"


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
Requires="jdp_science_postgresql>=0.1.1.10,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,levylab_lib_fileutilities>=1.2.5.12,levylab_lib_graph_utilities>=2.1.2.4,levylab_lib_lvtoitx>=3.0.4.11,levylab_lib_xy_utilities>=1.2.0.12,mgi_lib_numeric>=1.1.0.2,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3"
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
Num Files=48
File 0="user.lib/LevyLab/postgreSQL/Data.PGSQL.lvclass"
File 1="user.lib/LevyLab/postgreSQL/Tree.vi"
File 2="user.lib/LevyLab/postgreSQL/Typedefs/Connection Info--cluster.ctl"
File 3="user.lib/LevyLab/postgreSQL/Typedefs/Datatypes--enum.ctl"
File 4="user.lib/LevyLab/postgreSQL/Typedefs/Errors--enum.ctl"
File 5="user.lib/LevyLab/postgreSQL/subVIs/Build Path.vi"
File 6="user.lib/LevyLab/postgreSQL/subVIs/Parse Path Name.vi"
File 7="user.lib/LevyLab/postgreSQL/subVIs/Parse path.vi"
File 8="user.lib/LevyLab/postgreSQL/subVIs/Parse Variant.vi"
File 9="user.lib/LevyLab/postgreSQL/subVIs/password_prompt.vi"
File 10="user.lib/LevyLab/postgreSQL/subVIs/Path flags.vi"
File 11="user.lib/LevyLab/postgreSQL/subVIs/Paths to String with Commas.vi"
File 12="user.lib/LevyLab/postgreSQL/subVIs/Push Backup to DB.vi"
File 13="user.lib/LevyLab/postgreSQL/subVIs/SQL Time to Timestamp.vi"
File 14="user.lib/LevyLab/postgreSQL/subVIs/String Array to String with Commas.vi"
File 15="user.lib/LevyLab/postgreSQL/subVIs/Timestamp to SQL Time.vi"
File 16="user.lib/LevyLab/postgreSQL/Private/Convert Dictionary to ITEMs and VALUEs.vi"
File 17="user.lib/LevyLab/postgreSQL/Private/Error Handler.vi"
File 18="user.lib/LevyLab/postgreSQL/Private/Execute SQL.vi"
File 19="user.lib/LevyLab/postgreSQL/Private/Format SQL CREATE TABLE.vi"
File 20="user.lib/LevyLab/postgreSQL/Private/Format SQL INSERT Dictionary.vi"
File 21="user.lib/LevyLab/postgreSQL/Private/Format SQL INSERT.vi"
File 22="user.lib/LevyLab/postgreSQL/Private/Handle INSERT Error.vi"
File 23="user.lib/LevyLab/postgreSQL/Private/INSERT.vi"
File 24="user.lib/LevyLab/postgreSQL/Overrides/Close.vi"
File 25="user.lib/LevyLab/postgreSQL/Overrides/Open.vi"
File 26="user.lib/LevyLab/postgreSQL/Overrides/Read.vi"
File 27="user.lib/LevyLab/postgreSQL/Overrides/Write.vi"
File 28="user.lib/LevyLab/postgreSQL/dev/Get Trace (example).vi"
File 29="user.lib/LevyLab/postgreSQL/dev/INSERT (example).vi"
File 30="user.lib/LevyLab/postgreSQL/dev/INSERT PPMS4 (example).vi"
File 31="user.lib/LevyLab/postgreSQL/dev/move large data(wip) for real.vi"
File 32="user.lib/LevyLab/postgreSQL/dev/new copy speed test.vi"
File 33="user.lib/LevyLab/postgreSQL/API/Get Column Path.vi"
File 34="user.lib/LevyLab/postgreSQL/API/Get Columns.vi"
File 35="user.lib/LevyLab/postgreSQL/API/Get Path GUI.vi"
File 36="user.lib/LevyLab/postgreSQL/API/Get Paths Array GUI.vi"
File 37="user.lib/LevyLab/postgreSQL/API/Get Table Path.vi"
File 38="user.lib/LevyLab/postgreSQL/API/Get Tables.vi"
File 39="user.lib/LevyLab/postgreSQL/API/Get Users.vi"
File 40="user.lib/LevyLab/postgreSQL/API/Read Trace.vi"
File 41="user.lib/LevyLab/postgreSQL/API/Read Variable.vi"
File 42="user.lib/LevyLab/postgreSQL/API/Set Connection Info.vi"
File 43="user.lib/LevyLab/postgreSQL/API/Write Variable.vi"
File 44="user.lib/LevyLab/postgreSQL/Admin_DB/Administer Tables GUI.vi"
File 45="user.lib/LevyLab/postgreSQL/Admin_DB/Create Column.vi"
File 46="user.lib/LevyLab/postgreSQL/Admin_DB/Create Table.vi"
File 47="user.lib/LevyLab/postgreSQL/Admin_DB/Create User GUI.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=7
File 0="_functions_levylab_lib_postgresql_1.mnu"
File 1="_functions_levylab_lib_postgresql_2.mnu"
File 2="_functions_levylab_lib_postgresql_3.mnu"
File 3="_functions_levylab_lib_postgresql_4.mnu"
File 4="_functions_levylab_lib_postgresql_5.mnu"
File 5="_functions_levylab_lib_postgresql_6.mnu"
File 6="functions_LevyLab_lib_postgreSQL.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
