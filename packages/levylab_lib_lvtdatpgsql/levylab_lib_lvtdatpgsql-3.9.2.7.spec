[Package]
Name="levylab_lib_lvtdatpgsql"
Version="3.9.2.7"
Release=""
ID=2fe31fec750b484f6163d4368e374712
File Format="vip"
Format Version="2017"
Display Name="LV-Data-PGSQL"


[Description]
Description="- Database management and Selects and Insert macros to PostgreSQL/timescaleDB.\0D"
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL=""
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[3.9.2]\0A- Issue #120 fix buttons in PGPASS.ConnectionMgr.vi\0D\0A- updated dependencies\0A- Timestamp to SQL Time.vi uses timezone offset rather than UTC offset"
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
Requires="i3_external_encryption>=1.0.0.8,jdp_science_lib_common_utilities>=1.4.1.18,jdp_science_postgresql>=0.6.2.48,jki_lib_caraya>=1.4.3.147,jki_lib_json_serialization>=1.1.10.37,jki_lib_serialization>=1.0.1.14,jki_lib_state_machine>=2018.0.7.45,jki_lib_unicode>=1.0.0.7,labview_open_source_lib_epoch_datetime>=1.2.0.6,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.11.4,levylab_lib_lvtoitx>=3.9.2.7,levylab_lib_xy_utilities>=1.6.0.6,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_string>=1.1.1.5,mgi_lib_timing>=1.1.0.2,mgi_lib_tree>=1.0.4.4,national_instruments_lib_guid_generator>=1.0.2.3,ni_cloud_toolkit_for_aws>=1.1.0.1,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_md5>=4.1.1.10,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3,wireflow_ab_lib_wf_progressbar>=1.0.2.56"
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
Num Files=115
File 0="user.lib/LevyLab/LV-Data/LV-Data.PG/LV-Data.PGSQL.lvclass"
File 1="user.lib/LevyLab/LV-Data/LV-Data.PG/Tree.vi"
File 2="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Convert Dictionary to ITEMs and VALUEs.vi"
File 3="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Format SQL CREATE TABLE.vi"
File 4="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Format SQL INSERT Dictionary.vi"
File 5="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Read.vi"
File 6="user.lib/LevyLab/LV-Data/LV-Data.PG/unused/Write.vi"
File 7="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Configuration--cluster.ctl"
File 8="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Datatypes--combo.ctl"
File 9="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Datatypes--enum.ctl"
File 10="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Errors--enum.ctl"
File 11="user.lib/LevyLab/LV-Data/LV-Data.PG/Typedefs/Time.Datatype--enum.ctl"
File 12="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV Date Time to Timestamp.vi"
File 13="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV PRE-Process Files with Queues.vi"
File 14="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV Process Files with Queues.vi"
File 15="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV Process Files.vi"
File 16="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV Process Path.vi"
File 17="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV to PGSQL Choose Column Dialog.vi"
File 18="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV to PGSQL Record Processed.vi"
File 19="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/DSC TSV to PGSQL.vi"
File 20="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/PQ Test Get Datatype.vi"
File 21="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/PQ Test Invalid User.vi"
File 22="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/PQ Test List Tables.vi"
File 23="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/PQ Test Time Conversion.vi"
File 24="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/PQ Test Valid User.vi"
File 25="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/PQ Unit Tests.vi"
File 26="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Data.vi"
File 27="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test MultiValue INSERT format.vi"
File 28="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test MultiValue INSERT.vi"
File 29="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test PQ modes.vi"
File 30="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Switch Tables 2.vi"
File 31="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Switch Tables.vi"
File 32="user.lib/LevyLab/LV-Data/LV-Data.PG/Tests/Test Write and Read Data.vi"
File 33="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Add Time to Map.vi"
File 34="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Change Column Name.vi"
File 35="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Change Column Units.vi"
File 36="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Configuration Path.vi"
File 37="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Convert Double to String.vi"
File 38="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Create Table.vi"
File 39="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Create User.vi"
File 40="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Data Type Enum to Data Type String.vi"
File 41="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Delete Column.vi"
File 42="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Delete Table.vi"
File 43="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Error Code.vi"
File 44="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Execute SQL.vi"
File 45="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Format SQL INSERT Multivalue.vi"
File 46="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Format SQL INSERT.vi"
File 47="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Get Data Type from Path.vi"
File 48="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Get Data Type Prefix.vi"
File 49="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Get Users.vi"
File 50="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Handle INSERT Error.vi"
File 51="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/INSERT Multivalue.vi"
File 52="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/INSERT.vi"
File 53="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Map to SQL Insert.vi"
File 54="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Path flags.vi"
File 55="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Path Variant to Path Array.vi"
File 56="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Paths and Data to Map.vi"
File 57="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Paths to Map.vi"
File 58="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Paths to String with Commas.vi"
File 59="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Push Backup to DB.vi"
File 60="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Read Configuration.vi"
File 61="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Rename Table.vi"
File 62="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/SQL Time to Timestamp.vi"
File 63="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/String Array to String with Commas.vi"
File 64="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Switch Tables.vi"
File 65="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Timestamp to SQL Time.vi"
File 66="user.lib/LevyLab/LV-Data/LV-Data.PG/Private/Write Configuration.vi"
File 67="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.Connection Information.ctl"
File 68="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.ConnectionMgr.vi"
File 69="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.default path.vi"
File 70="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.Format Connection String with Password.vi"
File 71="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.Format Connection String.vi"
File 72="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.lvlib"
File 73="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.Read.vi"
File 74="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.Select Connection.vi"
File 75="user.lib/LevyLab/LV-Data/LV-Data.PG/PGPASS/PGPASS.Write.vi"
File 76="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/Get Trace (example).vi"
File 77="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/INSERT (example).vi"
File 78="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/INSERT PPMS4 (example).vi"
File 79="user.lib/LevyLab/LV-Data/LV-Data.PG/Example/Multi-Table Insert.vi"
File 80="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Copy Speed Test.vi"
File 81="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Read Traces.vi"
File 82="user.lib/LevyLab/LV-Data/LV-Data.PG/dev/Test Move Columns.vi"
File 83="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Build Path.vi"
File 84="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Check existence.vi"
File 85="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Close.vi"
File 86="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Compare Previous INSERT.vi"
File 87="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Copy (Data).vi"
File 88="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Copy (File).vi"
File 89="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Copy (String Data).vi"
File 90="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Create Column.vi"
File 91="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Execute SQL Statement.vi"
File 92="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Column Datatype.vi"
File 93="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Column Path.vi"
File 94="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Table Path.vi"
File 95="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Get Table Time datatype.vi"
File 96="user.lib/LevyLab/LV-Data/LV-Data.PG/API/List Columns.vi"
File 97="user.lib/LevyLab/LV-Data/LV-Data.PG/API/List Tables.vi"
File 98="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Parse path.vi"
File 99="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Parse Variant.vi"
File 100="user.lib/LevyLab/LV-Data/LV-Data.PG/API/PGSQL.Open.vi"
File 101="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Trace.vi"
File 102="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable (boolean).vi"
File 103="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable (double).vi"
File 104="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable (integer).vi"
File 105="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable (string).vi"
File 106="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Read Variable.vi"
File 107="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Result to Trace.vi"
File 108="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Write Variable (multirow).vi"
File 109="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Write Variable (one-row).vi"
File 110="user.lib/LevyLab/LV-Data/LV-Data.PG/API/Write Variable.vi"
File 111="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Administer Tables UI.vi"
File 112="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Create User UI.vi"
File 113="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Get Path UI.vi"
File 114="user.lib/LevyLab/LV-Data/LV-Data.PG/admin/Get Paths Array UI.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="Always"
Num Files=10
File 0="_functions_levylab_lib_lvtdatpgsql_1.mnu"
File 1="_functions_levylab_lib_lvtdatpgsql_2.mnu"
File 2="_functions_levylab_lib_lvtdatpgsql_3.mnu"
File 3="_functions_levylab_lib_lvtdatpgsql_4.mnu"
File 4="_functions_levylab_lib_lvtdatpgsql_5.mnu"
File 5="_functions_levylab_lib_lvtdatpgsql_6.mnu"
File 6="_functions_levylab_lib_lvtdatpgsql_7.mnu"
File 7="_functions_levylab_lib_lvtdatpgsql_8.mnu"
File 8="_functions_levylab_lib_lvtdatpgsql_9.mnu"
File 9="functions_levylab_lib_lvtdatpgsql.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
