[Package]
Name="levylab_lib_postgresql"
Version="1.3.3.21"
Release=""
ID=3a74907a53582f8d1b3f1828093f3395
File Format="vip"
Format Version="2017"
Display Name="postgreSQL/timescaleDB/S3"


[Description]
Description="VIs for interacting with postgreSQL /TimescaleDB/S3"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2021, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin, Jack Maier, Phil Shenk"
Demo="FALSE"
Release Notes="- Fix issue with read/write authentication\0A- Fix issue with PG backup authentication"
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
Requires="jdp_science_postgresql>=0.1.1.10,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.3.0.56,lava_lib_ui_tools>=1.4.1.74,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.2.4,levylab_lib_lvtoitx>=3.0.5.13,levylab_lib_xy_utilities>=1.3.2.16,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,mgi_lib_tree>=1.0.4.4,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_lvzip>=4.0.1,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,oglib_variantconfig>=4.0.0.5"
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
Num Files=78
File 0="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/Data.S3.lvclass"
File 1="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/Tree.vi"
File 2="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/Typedefs/S3 Backup--cluster.ctl"
File 3="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/private/Handle S3 Error.vi"
File 4="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/private/recursively populate tree ctl.vi"
File 5="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/private/split object path to hierarchy.vi"
File 6="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Download File.vi"
File 7="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/List Bucket Contents.vi"
File 8="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Populate Tree Ctl from Bucket.vi"
File 9="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Read Credentials from File.vi"
File 10="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Read.vi"
File 11="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Set Bucket.vi"
File 12="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Upload File.vi"
File 13="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Verify File.vi"
File 14="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Write.vi"
File 15="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Data.PGSQL.lvclass"
File 16="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Tree.vi"
File 17="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/unused/Convert Dictionary to ITEMs and VALUEs.vi"
File 18="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/unused/Format SQL CREATE TABLE.vi"
File 19="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/unused/Format SQL INSERT Dictionary.vi"
File 20="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/unused/Read.vi"
File 21="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/unused/Write.vi"
File 22="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Typedefs/Configuration--cluster.ctl"
File 23="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Typedefs/Datatypes--enum.ctl"
File 24="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Typedefs/Errors--enum.ctl"
File 25="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Change Column Name.vi"
File 26="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Change Column Units.vi"
File 27="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Configuration Path.vi"
File 28="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Configuration Window.vi"
File 29="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Convert Double to String.vi"
File 30="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Create Column.vi"
File 31="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Create Table.vi"
File 32="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Create User.vi"
File 33="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Error Handler.vi"
File 34="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Execute SQL.vi"
File 35="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Format SQL INSERT.vi"
File 36="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Get Column Path.vi"
File 37="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Get Configuration.vi"
File 38="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Get Data Type from Path.vi"
File 39="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Get Data Type Prefix.vi"
File 40="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Get Table Path.vi"
File 41="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Get Users.vi"
File 42="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Handle INSERT Error.vi"
File 43="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/INSERT.vi"
File 44="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Parse Path Name.vi"
File 45="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Parse Variant.vi"
File 46="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/password_prompt.vi"
File 47="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Path flags.vi"
File 48="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Paths to String with Commas.vi"
File 49="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Push Backup to DB.vi"
File 50="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Read Configuration.vi"
File 51="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/SQL Time to Timestamp.vi"
File 52="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/String Array to String with Commas.vi"
File 53="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Timestamp to SQL Time.vi"
File 54="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Write Configuration.vi"
File 55="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/Get Trace (example).vi"
File 56="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/INSERT (example).vi"
File 57="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/INSERT PPMS4 (example).vi"
File 58="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/new copy speed test.vi"
File 59="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Build Path.vi"
File 60="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Close.vi"
File 61="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Copy csv.vi"
File 62="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Columns.vi"
File 63="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Tables.vi"
File 64="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Open.vi"
File 65="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Parse path.vi"
File 66="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read SQL.vi"
File 67="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Trace.vi"
File 68="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Traces.vi"
File 69="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Variable (boolean).vi"
File 70="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Variable (double).vi"
File 71="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Variable (string).vi"
File 72="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Variable.vi"
File 73="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Write Variable.vi"
File 74="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/admin/Administer Tables UI.vi"
File 75="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/admin/Create User UI.vi"
File 76="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/admin/Get Path UI.vi"
File 77="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/admin/Get Paths Array UI.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=9
File 0="_functions_levylab_lib_postgresql_1.mnu"
File 1="_functions_levylab_lib_postgresql_2.mnu"
File 2="_functions_levylab_lib_postgresql_3.mnu"
File 3="_functions_levylab_lib_postgresql_4.mnu"
File 4="_functions_levylab_lib_postgresql_5.mnu"
File 5="_functions_levylab_lib_postgresql_6.mnu"
File 6="_functions_levylab_lib_postgresql_7.mnu"
File 7="_functions_levylab_lib_postgresql_8.mnu"
File 8="functions_LevyLab_lib_postgreSQL.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
