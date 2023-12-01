[Package]
Name="levylab_lib_logger_syslog"
Version="1.0.0.2"
Release=""
ID=34324b7dd27c5d9b62387cbcea1fafb3
File Format="vip"
Format Version="2017"
Display Name="Logger.syslog"


[Description]
Description="syslog datalogger class."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2023, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.0.0]\0A- first build as stand-alone package"
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
Requires="jki_lib_state_machine>=2018.0.7.45,jki_statemachineobjects>=1.4.0.69,lava_lib_ui_tools>=1.4.1.74,mgi_lib_1d_array>=1.0.2.3,mgi_lib_application_control>=1.1.1.10,mgi_lib_cluster>=1.1.0.1,mgi_lib_error_handling>=1.1.1.3,mgi_lib_error_reporter>=1.0.2.5,mgi_lib_file>=1.1.0.4,mgi_lib_numeric>=1.1.0.2,mgi_lib_picture_&_image>=1.0.2.1,mgi_lib_read_write_anything>=2.1.4.4,mgi_lib_string>=1.1.1.5,ni_lib_seh>=2.1.10.1,nise_syslog>=1.3.3.27,oglib_appcontrol>=4.1.0.7,oglib_array>=4.1.1.14,oglib_error>=4.2.0.23,oglib_file>=4.0.1.22,oglib_lvdata>=5.0.0.27,oglib_numeric>=4.1.0.8,oglib_string>=5.0.0.25,levylab_lib_build_support>=1.2.5.1"
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
File 0="user.lib/Levylab/Logger.syslog/CreatePrivateEvents.vi"
File 1="user.lib/Levylab/Logger.syslog/DestroyPrivateEvents.vi"
File 2="user.lib/Levylab/Logger.syslog/Example - Error Handler.vi"
File 3="user.lib/Levylab/Logger.syslog/Example - JKI SM MGI Error Log.vi"
File 4="user.lib/Levylab/Logger.syslog/Example - Syslog Collector.vi"
File 5="user.lib/Levylab/Logger.syslog/Example - Syslog Device.vi"
File 6="user.lib/Levylab/Logger.syslog/Logger.syslog.GetPrivateEvents.vi"
File 7="user.lib/Levylab/Logger.syslog/Logger.syslog.lvclass"
File 8="user.lib/Levylab/Logger.syslog/Logger.syslog.lvproj"
File 9="user.lib/Levylab/Logger.syslog/Logger.syslog.syslogmessage.vi"
File 10="user.lib/Levylab/Logger.syslog/Logger.syslog.TestLauncher.vi"
File 11="user.lib/Levylab/Logger.syslog/Process.vi"
File 12="user.lib/Levylab/Logger.syslog/Report Event or Error.vi"
File 13="user.lib/Levylab/Logger.syslog/Typedefs/PrivateEvents--Cluster.ctl"
File 14="user.lib/Levylab/Logger.syslog/Typedefs/PrivateEvents--Logger.syslog.syslog message.ctl"


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
