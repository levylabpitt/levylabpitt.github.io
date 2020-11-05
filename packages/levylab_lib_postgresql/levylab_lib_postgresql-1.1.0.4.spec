[Package]
Name="levylab_lib_postgresql"
Version="1.1.0.4"
Release=""
ID=fa8e522855ae5b0668346944ed96c83f
File Format="vip"
Format Version="2017"
Display Name="postgreSQL/timescaleDB/S3"


[Description]
Description="VIs for interacting with postgreSQL /timescaleDB/S3"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2020, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin, Jack Maier, Phil Shenk"
Demo="FALSE"
Release Notes="- Add Data.S3.lvclass for intereacting with AWS S3"
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
Requires="i3_external_encryption>=1.0.0.8,jdp_science_postgresql>=0.1.1.10,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,levylab_lib_fileutilities>=1.2.5.12,levylab_lib_graph_utilities>=2.1.2.4,levylab_lib_lvtoitx>=3.0.4.11,levylab_lib_xy_utilities>=1.2.0.12,mgi_lib_numeric>=1.1.0.2,ni_cloud_toolkit_for_aws>=1.1.0.1,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=4.2.0.21,oglib_lvzip>=4.0.1,oglib_md5>=4.1.1.10,oglib_numeric>=4.1.0.8,oglib_string>=4.1.0.12,oglib_time>=4.0.1.3"
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
Num Files=61
File 0="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/Data.S3.lvclass"
File 1="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/Tree.vi"
File 2="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/private/recursively populate tree ctl.vi"
File 3="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/private/split object path to hierarchy.vi"
File 4="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Download File.vi"
File 5="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/List Bucket Contents.vi"
File 6="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Populate Tree Ctl from Bucket.vi"
File 7="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Read Credentials from File.vi"
File 8="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Read.vi"
File 9="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Set Bucket.vi"
File 10="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Upload File.vi"
File 11="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Verify File.vi"
File 12="user.lib/LevyLab/postgreSQL-timescaleDB/Data.S3/API/Write.vi"
File 13="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Data.PGSQL.lvclass"
File 14="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Tree.vi"
File 15="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Typedefs/Connection Info--cluster.ctl"
File 16="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Typedefs/Datatypes--enum.ctl"
File 17="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Typedefs/Errors--enum.ctl"
File 18="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Build Path.vi"
File 19="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Parse Path Name.vi"
File 20="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Parse path.vi"
File 21="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Parse Variant.vi"
File 22="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/password_prompt.vi"
File 23="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Path flags.vi"
File 24="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Paths to String with Commas.vi"
File 25="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Push Backup to DB.vi"
File 26="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/SQL Time to Timestamp.vi"
File 27="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/String Array to String with Commas.vi"
File 28="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/subVIs/Timestamp to SQL Time.vi"
File 29="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Convert Dictionary to ITEMs and VALUEs.vi"
File 30="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Error Handler.vi"
File 31="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Execute SQL.vi"
File 32="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Format SQL CREATE TABLE.vi"
File 33="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Format SQL INSERT Dictionary.vi"
File 34="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Format SQL INSERT.vi"
File 35="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/Handle INSERT Error.vi"
File 36="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Private/INSERT.vi"
File 37="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Overrides/Close.vi"
File 38="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Overrides/Open.vi"
File 39="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Overrides/Read.vi"
File 40="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Overrides/Write.vi"
File 41="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/Get Trace (example).vi"
File 42="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/INSERT (example).vi"
File 43="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/INSERT PPMS4 (example).vi"
File 44="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/move large data(wip) for real.vi"
File 45="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/dev/new copy speed test.vi"
File 46="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Column Path.vi"
File 47="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Columns.vi"
File 48="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Path GUI.vi"
File 49="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Paths Array GUI.vi"
File 50="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Table Path.vi"
File 51="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Tables.vi"
File 52="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Get Users.vi"
File 53="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Trace.vi"
File 54="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Read Variable.vi"
File 55="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Set Connection Info.vi"
File 56="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/API/Write Variable.vi"
File 57="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Admin_DB/Administer Tables GUI.vi"
File 58="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Admin_DB/Create Column.vi"
File 59="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Admin_DB/Create Table.vi"
File 60="user.lib/LevyLab/postgreSQL-timescaleDB/Data.PG/Admin_DB/Create User GUI.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=11
File 0="_functions_levylab_lib_postgresql_1.mnu"
File 1="_functions_levylab_lib_postgresql_10.mnu"
File 2="_functions_levylab_lib_postgresql_2.mnu"
File 3="_functions_levylab_lib_postgresql_3.mnu"
File 4="_functions_levylab_lib_postgresql_4.mnu"
File 5="_functions_levylab_lib_postgresql_5.mnu"
File 6="_functions_levylab_lib_postgresql_6.mnu"
File 7="_functions_levylab_lib_postgresql_7.mnu"
File 8="_functions_levylab_lib_postgresql_8.mnu"
File 9="_functions_levylab_lib_postgresql_9.mnu"
File 10="functions_LevyLab_lib_postgreSQL.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
