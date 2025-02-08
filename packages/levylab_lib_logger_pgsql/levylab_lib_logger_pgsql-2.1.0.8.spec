[Package]
Name="levylab_lib_logger_pgsql"
Version="2.1.0.8"
Release=""
ID=bf06ff7bc9dca924322f34b69b15ddad
File Format="vip"
Format Version="2017"
Display Name="Logger.PGSQL"


[Description]
Description="postgreSQL datalogger class."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[2.1.0]\0A- #144: new method Write Variable Multiline"
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
Requires=""
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
Num Files=25
File 0="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL.lvlib"
File 1="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/CreatePrivateEvents.vi"
File 2="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/CreatePublicEvents.vi"
File 3="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/DestroyPrivateEvents.vi"
File 4="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/DestroyPublicEvents.vi"
File 5="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.GetPrivateEvents.vi"
File 6="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.PGSQL.GetPublicEvents.vi"
File 7="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.PGSQL.lvclass"
File 8="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.PGSQL.ReadVariable.vi"
File 9="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.PGSQL.TestLauncher.vi"
File 10="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.PGSQL.WriteVariable.vi"
File 11="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.PGSQL.WriteVariableMultiline.vi"
File 12="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Logger.ReadVariable.vi"
File 13="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Process.vi"
File 14="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Read from PGSQL.vi"
File 15="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Shorten Cluster.vi"
File 16="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Test PGSQL.vi"
File 17="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Write Or Not.vi"
File 18="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Typedefs/PrivateEvents--Cluster.ctl"
File 19="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Read Variable.ctl"
File 20="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Set Address.ctl"
File 21="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Write Variable Multiline.ctl"
File 22="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Typedefs/PrivateEvents--Logger.PGSQL.Write Variable.ctl"
File 23="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Typedefs/PublicEvents--Cluster.ctl"
File 24="user.lib/Levylab/Logger.PGSQL/Logger.PGSQL/Typedefs/PublicEvents--Logger.PGSQL.Read Variable.ctl"


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
