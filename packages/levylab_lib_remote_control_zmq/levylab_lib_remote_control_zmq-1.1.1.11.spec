[Package]
Name="levylab_lib_remote_control_zmq"
Version="1.1.1.11"
Release=""
ID=e163a53d674b9a7fd12e55e90358f571
File Format="vip"
Format Version="2017"
Display Name="RemoteControl.ZMQ"


[Description]
Description="Override library implementing ZMQ lazy pirate reliable request reply (RRR) protocal using RemoteControl SMO framework."
Summary=""
License="BSD-3"
Copyright="Copyright (c) 2024, LevyLab"
Distribution=""
Vendor="LevyLab"
URL="https://github.com/levylabpitt/Instrument-Framework"
Packager="Patrick Irvin"
Demo="FALSE"
Release Notes="[1.1.1]\0A- Update install location\0A- Update default timeout for ZMQ read"
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
Num Files=24
File 0="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ.lvclass"
File 1="user.lib/Levylab/RemoteControl.ZMQ/RemoteControl.ZMQ.lvproj"
File 2="user.lib/Levylab/RemoteControl.ZMQ/Typedefs/ZMQ Config.ctl"
File 3="user.lib/Levylab/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestClient.vi"
File 4="user.lib/Levylab/RemoteControl.ZMQ/Tests/RemoteControl.ZMQ.TestServer.vi"
File 5="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ Rep Test.vi"
File 6="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ Req Test.vi"
File 7="user.lib/Levylab/RemoteControl.ZMQ/Tests/ZMQ sandbox.vi"
File 8="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Bind REP Socket.vi"
File 9="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Connect REQ Socket.vi"
File 10="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Context.vi"
File 11="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Read.vi"
File 12="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test REP Socket.vi"
File 13="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test REQ Socket.vi"
File 14="user.lib/Levylab/RemoteControl.ZMQ/Tests/Unit Tests/Test Write.vi"
File 15="user.lib/Levylab/RemoteControl.ZMQ/private/Build Endpoint.vi"
File 16="user.lib/Levylab/RemoteControl.ZMQ/private/ZMQ.Connect.vi"
File 17="user.lib/Levylab/RemoteControl.ZMQ/private/ZMQ.Handle Error.vi"
File 18="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Close Connection.vi"
File 19="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Get Connections.vi"
File 20="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Open Client Connection.vi"
File 21="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Open Server Connection.vi"
File 22="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Read Message.vi"
File 23="user.lib/Levylab/RemoteControl.ZMQ/Methods (Overrides)/Send Message.vi"


[File Group 1]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="Always"
Num Files=5
File 0="_functions_levylab_lib_remote_control_zmq_1.mnu"
File 1="_functions_levylab_lib_remote_control_zmq_2.mnu"
File 2="_functions_levylab_lib_remote_control_zmq_3.mnu"
File 3="_functions_levylab_lib_remote_control_zmq_4.mnu"
File 4="functions_Levylab_lib_remote_control_zmq.mnu"


[File Group 2]
Target Dir="<menus>/Categories/LevyLab/RemoteControl"
Replace Mode="If Newer"
Num Files=1
File 0="dir.mnu"
