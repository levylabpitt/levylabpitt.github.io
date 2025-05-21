[Package]
Name="levylab_lib_logger_syslog"
Version="1.0.1.3"
Release=""
ID=d811ac16e67741c0a4220300b665aee7
File Format="vip"
Format Version="2017"
Display Name="Logger.syslog"


[Description]
Description="syslog datalogger class."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2025, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.1]\0A- build with LLV Logger 1.1.2 dependency"
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
Requires="levylab_lib_logger>=1.1.2.11"
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
Num Files=15
File 0="user.lib/Levylab/Logger.syslog/Logger.syslog.lvlib"
File 1="user.lib/Levylab/Logger.syslog/Logger.syslog/CreatePrivateEvents.vi"
File 2="user.lib/Levylab/Logger.syslog/Logger.syslog/DestroyPrivateEvents.vi"
File 3="user.lib/Levylab/Logger.syslog/Logger.syslog/Example - Error Handler.vi"
File 4="user.lib/Levylab/Logger.syslog/Logger.syslog/Example - JKI SM MGI Error Log.vi"
File 5="user.lib/Levylab/Logger.syslog/Logger.syslog/Example - Syslog Collector.vi"
File 6="user.lib/Levylab/Logger.syslog/Logger.syslog/Example - Syslog Device.vi"
File 7="user.lib/Levylab/Logger.syslog/Logger.syslog/Logger.syslog.GetPrivateEvents.vi"
File 8="user.lib/Levylab/Logger.syslog/Logger.syslog/Logger.syslog.lvclass"
File 9="user.lib/Levylab/Logger.syslog/Logger.syslog/Logger.syslog.syslogmessage.vi"
File 10="user.lib/Levylab/Logger.syslog/Logger.syslog/Logger.syslog.TestLauncher.vi"
File 11="user.lib/Levylab/Logger.syslog/Logger.syslog/Process.vi"
File 12="user.lib/Levylab/Logger.syslog/Logger.syslog/Report Event or Error.vi"
File 13="user.lib/Levylab/Logger.syslog/Logger.syslog/Typedefs/PrivateEvents--Cluster.ctl"
File 14="user.lib/Levylab/Logger.syslog/Logger.syslog/Typedefs/PrivateEvents--Logger.syslog.syslog message.ctl"


[File Group 1]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="Always"
Num Files=1
File 0="functions_Levylab_lib_logger_syslog.mnu"


[File Group 2]
Target Dir="<menus>/Categories/Levylab"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
