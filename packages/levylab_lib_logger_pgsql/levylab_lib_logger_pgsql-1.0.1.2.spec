[Package]
Name="levylab_lib_logger_pgsql"
Version="1.0.1.2"
Release=""
ID=633a8c398045a0d0ff0d4ce68f275d1d
File Format="vip"
Format Version="2017"
Display Name="Logger.PGSQL"


[Description]
Description="postgreSQL datalogger class."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2024, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.1]\0A- add functional method API for reading variables\0A- update dependencies"
System Package="FALSE"
Sub Package="FALSE"
License Agreement="TRUE"


[LabVIEW]
close labview before install="FALSE"
restart labview after install="FALSE"
skip mass compile after install="FALSE"
install into global environment="FALSE"


[Platform]
Exclusive_LabVIEW_Version="LabVIEW x86>=19.0"
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
Requires="jdp_science_postgresql>=0.3.1.20,jki_lib_caraya>=1.4.3.147,jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,levylab_lib_control_vi>=1.3.0.11,levylab_lib_fileutilities>=1.2.6.13,levylab_lib_graph_utilities>=2.1.10.3,levylab_lib_lvtoitx>=3.7.2.1,levylab_lib_xy_utilities>=1.5.4.1,mgi_lib_1d_array>=1.0.2.3,mgi_lib_numeric>=1.1.0.2,national_instruments_lib_guid_generator>=1.0.2.3,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_dictionary>=4.0.0.4,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,oglib_time>=4.0.1.3"
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
Num Files=35
File 0="user.lib/Levylab/Logger.PGSQL/CreatePrivateEvents.vi"
File 1="user.lib/Levylab/Logger.PGSQL/CreatePublicEvents.vi"
File 2="user.lib/Levylab/Logger.PGSQL/DestroyPrivateEvents.vi"
File 3="user.lib/Levylab/Logger.PGSQL/DestroyPublicEvents.vi"
File 4="user.lib/Levylab/Logger.PGSQL/Logger.GetPrivateEvents.vi"
File 5="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL.GetPublicEvents.vi"
File 6="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL.lvclass"
File 7="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL.lvproj"
File 8="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL.ReadVariable.vi"
File 9="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL.TestLauncher.vi"
File 10="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL.WriteVariable.vi"
File 11="user.lib/Levylab/Logger.PGSQL/Logger.ReadVariable.vi"
File 12="user.lib/Levylab/Logger.PGSQL/Process.vi"
File 13="user.lib/Levylab/Logger.PGSQL/Read from PGSQL.vi"
File 14="user.lib/Levylab/Logger.PGSQL/Shorten Cluster.vi"
File 15="user.lib/Levylab/Logger.PGSQL/Test PGSQL.vi"
File 16="user.lib/Levylab/Logger.PGSQL/Write Cluster to PGSQL.vi"
File 17="user.lib/Levylab/Logger.PGSQL/Write Or Not.vi"
File 18="user.lib/Levylab/Logger.PGSQL/Write to PGSQL.vi"
File 19="user.lib/Levylab/Logger.PGSQL/Typedefs/PrivateEvents--Cluster.ctl"
File 20="user.lib/Levylab/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Read Variable.ctl"
File 21="user.lib/Levylab/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Set Address.ctl"
File 22="user.lib/Levylab/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Write Variable.ctl"
File 23="user.lib/Levylab/Logger.PGSQL/Typedefs/PublicEvents--Cluster.ctl"
File 24="user.lib/Levylab/Logger.PGSQL/Typedefs/PublicEvents--Logger.PGSQL.Read Variable.ctl"
File 25="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DECreate Logger.vi"
File 26="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DEDestroy Logger.vi"
File 27="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DELogger.lvclass"
File 28="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DELogger.TestLauncher.vi"
File 29="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DEProcess_DoNotRun.vi"
File 30="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DERead Debug Mode.vi"
File 31="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DERead path.vi"
File 32="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DEState History.vi"
File 33="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DEWrite Debug Mode.vi"
File 34="user.lib/Levylab/_Logger_internal_deps/367B3B2005C08EFAA8F502D5C54B62DEWrite path.vi"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_logger_pgsql.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
